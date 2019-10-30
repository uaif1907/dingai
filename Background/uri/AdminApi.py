from flask_restful import Resource,fields,marshal,reqparse
# from .database.db import session
# from .database.property import Admins
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
        # data= session.query(Admins).all()

        return {"code":200,"msg":"ok"}