from flask_restful import Resource,fields,marshal
from Background.database.db import session
from Background.database.Department import Departments
departments_fields={
    'id':fields.Integer,
    'cid':fields.Integer,
    'name':fields.String
}
class Department(Resource):
    def get(self):
        """
        获取公司对应部门
        :param cid:
        :return: 部门信息
        """
        data = session.query(Departments).all()
        arr = [(marshal(item,departments_fields)) for item in data]
        return {"code":200,"data":arr}