from flask_restful import Resource,fields,marshal,reqparse
from Background.database.db import session
from flask import jsonify,request
from Background.database.maintain import Main
from Background.database.property import Propertys
from Background.database.User import Users
import time,datetime


class Maintain(Resource):
    def get(self):
        lis = []
        dic={}
        val = [] #链表存储
        val1 = []
        prop =[] #拼接的所需的资产名字
        result = [] #结果存储
        resultEnd = []#最终返回结果
        names = [] #姓名联合查询存储
        data0 =[]#资产表内容存储
        select = [] #下拉选择的资产名字
        selec = {} #资产下拉寄存器

        data= session.query(Main).all()  #维修管理表单个查询
        data1 = session.query(Main,Users).join(Main,Users.uid==Main.uid).all() #通过报修人信息的级联查询
        propers = session.query(Propertys).all() #资产查询

        for item0 in propers: #资产下拉选项
            selec['value']=item0.__dict__['uid']
            selec['label']=item0.__dict__['name']
            select.append(selec)
            selec={}



        num = 0 #级联表计数器
        name=''
        for item1 in data1:
            for ite1 in item1:
                if(num==1):
                    name = ite1.__dict__['name']
                num+=1
                val.append(ite1.__dict__)
        for item in data:
            val1.append(dic)
            showTime1 = str(item.__dict__['time1'])
            item.__dict__['time1']= showTime1#报修时间



            try:  #判断是否有维修时间

                showTime2 = str((item.__dict__['time2']))
                item.__dict__['time2'] = showTime2

            except:
                now = datetime.datetime.now()
                item.__dict__['time2'] = now.strftime('%Y-%m-%d %H:%M:%S')


            price = item.__dict__['price']

            item.__dict__['time1']=showTime1
            item.__dict__['price']=str(price)+'￥'
            i = 0
            for ite in item.__dict__:
                if(i>0):
                    dic[ite] = item.__dict__[ite]

                i += 1

            dic['name']=name
            lis.append(dic)

        # 处理级联查询后的结果拼接
        # 处理报修人信息的拼接
        a=0 #拼接计数器
        for itee in val:
            if(a%2!=0):
                names.append(itee['name'])
                # print('全部名字', itee['name'])
            a+=1


        b=0
        length = len(val)
        l = 0
        for itee2 in val: #名字序列化存储
            if(b%2==0 and l<=length):
                itee2['name']=names[l]
                result.append(itee2)
                l+=1

            b+=1

        # 处理资产产状态的拼接

        try:
            for item in result: #资产序列化存储
                pro = session.query(Propertys).filter_by(uid='%s' % item['uid']).all()[0].__dict__
                data0.append(pro['status'])
                prop.append(pro['name'])
        except BaseException as bas:
            print(bas)

        try:
            nu=0
            for item3 in result:
                item3['status'] = data0[nu]
                item3['prop'] = prop[nu]
                del item3['_sa_instance_state']
                resultEnd.append(item3)
                nu+=1
        except BaseException as bas:
            print(bas)


        return jsonify({'data':resultEnd,'prop':select})


    def post(self):
        dataBack = request.get_json(silent=True)
        if dataBack['edit']==1:
            data = session.query(Main).filter_by(id=dataBack['id']).first()


            #zt时间处理


            print('time1', dataBack['time1'])
            print('time2', dataBack['time2'])


            #报修时间处理
            try:
                c1 = time.mktime(time.strptime(dataBack['time1'], "%Y-%m-%d")) #未修改点击确认的格式
                t1 = datetime.datetime.fromtimestamp(c1)
                data.time1 = t1
            except:
                c1 = time.mktime(time.strptime(dataBack['time1'], "%Y-%m-%dT%H:%M:%S.000Z")) #修改后点击确认的格式
                t1 = datetime.datetime.fromtimestamp(c1)
                data.time1 = t1


            #维修时间处理
            try:
                c2 = time.mktime(time.strptime(dataBack['time2'], "%Y-%m-%d")) #未修改点击确认的格式
                t2 = datetime.datetime.fromtimestamp(c2)
                data.time1 = t2
            except:
                c2 = time.mktime(time.strptime(dataBack['time2'], "%Y-%m-%dT%H:%M:%S.000Z")) #修改后点击确认的格式
                t2 = datetime.datetime.fromtimestamp(c2)
                data.time1 = t2


            data.explain =dataBack['explain']
            data.explain2=dataBack['explain2']
            data.uid=dataBack['uid']
            data.price=dataBack['price'].replace('￥','')
            data.num=dataBack['num']
            data.pid =dataBack['pid']
            data.id=data.id
            session.commit()






        elif dataBack['edit']==0:

            add = Main(uid=dataBack['pop']['uid'],people='待定',pid=dataBack['pop']['did'],time1=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),explain=dataBack['collar_remarks'],price=0,time2=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),num=dataBack['handle_name'])
            session.add(add)
            session.commit()
            session.close()

            print(dataBack)
        elif dataBack['edit']==2:
            data = session.query(Main).filter_by(id=dataBack['id']).first()
            session.delete(data)
            session.commit()
            session.close()
        return 'success'



