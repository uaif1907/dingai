from flask_restful import Resource,fields,marshal
from Background.database.db import session
from Background.database.property import Propertys
from Background.database.Admin import Admins
propertys_fields = {
    'id':fields.Integer,
    'status':fields.Integer,
    'bar_codes':fields.String,
    'name':fields.String,
    'type':fields.Integer,
    'model':fields.String,
    'sn':fields.Integer,
    'unit':fields.String,
    'price':fields.Float,
    'time':fields.Integer,
    'area':fields.Integer,
    'deadline':fields.Integer,
    'source':fields.Integer,
    'remark':fields.String,
    'img':fields.String,
    'supplier':fields.String,
    'linkman':fields.String,
    'tel':fields.String,
    'expir':fields.DateTime,
    'info':fields.String,
    'aid':fields.Integer,
    'cid':fields.Integer,
    'uid':fields.Integer,
    'did':fields.Integer,
    'username':fields.String
}
class Property(Resource):
    def get(self):
        """
        获取资产登记
        :return:返回全部资产登记
        """

        data = session.query(Propertys).all()
        for item in data:
            item.username = item.admin.username

        data = [ marshal(item,propertys_fields) for item in data]

        return {'msg':'ok','data':data}