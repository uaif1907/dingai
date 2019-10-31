from flask_restful import Resource,fields,marshal,reqparse
from Background.database.db import session
from Background.database.Admin import Admins
admins_fields={
    'id':fields.Integer,
    'username':fields.String,
    'password':fields.Integer,
    'type':fields.Integer
}
class Admin(Resource):
    def get(self):
        """
        :return: 管理员
        """

        data= session.query(Admins).all()
        arr = [(marshal(item,admins_fields)) for item in data]

        return {"code":200,"data":arr}