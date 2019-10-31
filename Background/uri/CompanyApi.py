from flask_restful import Resource,fields,marshal
from Background.database.db import session
from Background.database.Company import Companys
companys_fields={
    'id':fields.Integer,
    'name':fields.String,
}

class Company(Resource):
    def get(self):
        """
        获取全部公司
        :return:返回全部公司

        """
        data = session.query(Companys).all()
        arr = [(marshal(item,companys_fields)) for item in data]
        return {"code":200,"data":arr}