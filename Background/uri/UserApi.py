from flask_restful import Resource,fields,marshal,reqparse
from Background.database.db import session
from Background.database.property import Users
user_fields={
    'uid':fields.Integer,
    'num':fields.Integer,
    'name':fields.String,
    'cid':fields.Integer,
    'did':fields.Integer,
    'email':fields.String,
    'tel':fields.Integer
}
class User(Resource):
    def get(self,cid,did):
        """
        获取用户信息
        :param cid: 公司id
        :param did: 部门id
        :return:  返回此部门下所有的用户
        """
        data= session.query(Users).all()
        data = [ marshal(item,user_fields) for item in data]

        return {"code":200,"data":data}