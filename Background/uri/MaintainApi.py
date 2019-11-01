from flask_restful import Resource,fields,marshal,reqparse
from Background.database.db import session
from flask import jsonify
from Background.database.maintain import Main
from Background.database.property import Propertys
from Background.database.User import Users


class Maintain(Resource):
    def get(self,uid):
        lis = []
        dic={}
        val = []
        val1 = []
        prop =[] #资产名字
        result = [] #结果存储
        resultEnd = []#最终返回结果
        names = [] #姓名联合查询存储
        data0 =[]#资产表内容存储



        data= session.query(Main).all()  #维修管理表单个查询
        data1 = session.query(Main,Users).join(Main,Users.uid==Main.uid).all() #通过报修人信息的级联查询
        # print(data1[0][0].__dict__,'\n',data1[0][1].__dict__,'\n',dir(data1[0][0]))


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
            time1 = item.__dict__['time1']
            timeStamp = 1381419600
            dateArray1 = time1.utcfromtimestamp(timeStamp)
            showTime1 = dateArray1.strftime("%Y-%m-%d") #报修时间

            print(showTime1)
            time2 = item.__dict__['time2']
            dateArray2 = time2.utcfromtimestamp(timeStamp)
            showTime2 = dateArray2.strftime("%Y-%m-%d") #维修时间

            price = item.__dict__['price']
            item.__dict__['time2']=showTime2
            item.__dict__['time1']=showTime1
            item.__dict__['price']=str(price)+'￥'
            i = 0
            for ite in item.__dict__:
                if(i>0):
                    dic[ite] = item.__dict__[ite]
                else:
                    print(i)
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
            else:
                print('........')
            b+=1
        # 处理产状态的拼接
        for item in result:
            pro= session.query(Propertys).filter_by(uid='%s'%item['uid']).one().__dict__
            data0.append(pro['status'])
            prop.append(pro['name'])


        nu=0
        for item3 in result:
            item3['status'] = data0[nu]
            item3['prop'] = prop[nu]
            del item3['_sa_instance_state']
            resultEnd.append(item3)
            nu+=1
        print(resultEnd)
            # print(lis)
            # print(dir(item.__dict__))

        return jsonify({'data':resultEnd})


    def post(self,uid):
        print(uid)


