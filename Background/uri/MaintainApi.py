from flask_restful import Resource,fields,marshal,reqparse
from Background.database.db import session
from flask import jsonify
from Background.database.maintain import Main
from Background.database.property import Propertys,Users

class Maintain(Resource):
    def get(self,uid):
        lis = []
        dic={}
        val = []
        val1 = []
        result = []
        names = []
        data= session.query(Main).all()

        # print(data0)
        data1 = session.query(Main,Users).join(Main,Users.uid==Main.uid).all() #报修人信息的及联查询
        # print(data1[0][0].__dict__,'\n',data1[0][1].__dict__,'\n',dir(data1[0][0]))


        num = 0
        name=''
        for item1 in data1:
            for ite1 in item1:
                if(num==1):
                    name = ite1.__dict__['name']
                # print(num,ite1.__dict__,name)
                num+=1
                val.append(ite1.__dict__)
        for item in data:
            val1.append(dic)
            time1 = item.__dict__['time1']
            # print(item.__dict__['time1'])
            time2 = item.__dict__['time2']
            price = item.__dict__['price']
            item.__dict__['time2']=str(time2)
            item.__dict__['time1']=str(time1)
            item.__dict__['price']=str(price)
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
        a=0
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
            data0 = session.query(Propertys).filter_by(uid='%d' % item['uid']).one()
            print(data0)
        print(result)
            # print(lis)
            # print(dir(item.__dict__))

        return jsonify({'data':lis})
