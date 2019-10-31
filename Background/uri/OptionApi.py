from flask_restful import Resource,fields,marshal,reqparse
from Background.database.db import session
from flask import jsonify
from Background.database.Department import Departments
from Background.database.Company import Companys
from Background.database.User import Users

class Option(Resource):
    def get(self,):
        uss = []
        comm = []
        dee = []
        result = []
        user = session.query(Companys).all()
        company = session.query(Users).all()
        department = session.query(Departments).all()
        for us in user:
            del us.__dict__['_sa_instance_state']
            uss.append(us.__dict__)
            # print(us.__dict__)
        for de in department:
            del de.__dict__['_sa_instance_state']
            dee.append(de.__dict__)
        for co in company:
            del co.__dict__['_sa_instance_state']
            comm.append(co.__dict__)
            # print(co.__dict__)

        for u in uss:
            for c in comm:
                if (u['id']==c['uid']):
                    result.append(u)
                    result.append(c)

        # print(result)

        #计数器
        num=0
        result1=[]
        for item in result:
            if(num%2==0):
                result[num+1]['company']=item['name']
                result1.append(result[num+1])
            num+=1


        result2=[]
        dic ={}
        for i in range(len(result1)):
            for dep in dee:
                if(dep['cid']==result1[i]['uid']):
                    result1[i]['department']=dep['name']
                    dic=result1[i]
            result2.append(dic)

        print('返回的',result2)
        return {'data':result2}
