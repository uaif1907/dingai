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
        val = []
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

        for item0 in propers:
            selec['value']=item0.__dict__['uid']
            selec['label']=item0.__dict__['name']
            select.append(selec)



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

            showTime1 = item.__dict__['time1'].strftime('%Y-%m-%d %H:%M:%S')
            # time1 = item.__dict__['time1']
            # timeStamp = 1381419600
            # dateArray1 = time1.utcfromtimestamp(timeStamp)
            # showTime1 = dateArray1.strftime("%Y-%m-%d %H:%M:%S") #报修时间



            try:
                showTime2 =  item.__dict__['time2'].strftime('%Y-%m-%d %H:%M:%S')


                # time2 = item.__dict__['time2']
                # dateArray2 = time2.utcfromtimestamp(timeStamp)
                # showTime2 = dateArray2.strftime("%Y-%m-%d %H:%M:%S") #维修时间
                # item.__dict__['time2'] = showTime2
            except:
                now = datetime.datetime.now()
                item.__dict__['time2'] = now.strftime('%Y-%m-%d %H:%M:%S')

                # item.__dict__['time2'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
            price = item.__dict__['price']
            item.__dict__['time2'] = showTime2
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
            a+=1

        b=0
        for itee2 in val:

            if(b%2==0):
                itee2['name']=names[b%2]
                result.append(itee2)

            b+=1
        # 处理资产产状态的拼接

        for item in result:
            pro = session.query(Propertys).filter_by(uid='%s' % item['uid']).one().__dict__
            data0.append(pro['status'])
            prop.append(pro['name'])


        nu=0
        for item3 in result:
            item3['status'] = data0[nu]
            item3['prop'] = prop[nu]
            del item3['_sa_instance_state']
            resultEnd.append(item3)
            nu+=1


        return jsonify({'data':resultEnd,'prop':select})


    def post(self):
        dataBack = request.get_json(silent=True)
        if dataBack['edit']==1:
            data = session.query(Main).filter_by(id=dataBack['id']).first()
            session.delete(data)
            session.commit()


            # class 'str'> 2019-11-01 19:42: 48

            #zt时间处理
            c1 = time.mktime(time.strptime(dataBack['time1'], "%Y-%m-%d %H:%M:%S"))
            t1 = datetime.datetime.fromtimestamp(c1)

            c2 = time.mktime(time.strptime(dataBack['time2'], "%Y-%m-%d %H:%M:%S"))
            t2 = datetime.datetime.fromtimestamp(c2)

            print(t1,t2)






            update = Main(uid=dataBack['uid'],people=dataBack['people'],time1=t1,time2=t2,explain=dataBack['explain'],explain2=dataBack['explain2'],price=dataBack['price'].replace('￥',''),pid=dataBack['pid'])


            session.add(update)
            session.commit()
            session.close()
        elif dataBack['edit']==0:
            # data = session.query(Main).filter_by(uid=dataBack['pop']['uid']).first()

            add = Main(uid=dataBack['pop']['uid'],people='待定',pid=dataBack['pop']['did'],time1=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),explain=dataBack['collar_remarks'],price=0,time2=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            session.add(add)
            session.commit()
            session.close()

            print(dataBack)
        return 'success'



