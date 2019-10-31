from flask_restful import Resource
from Background.database.db import session
from Background.database.property import Propertys

class Property(Resource):
    def get(self):
        """
        获取资产登记
        :return:返回全部资产登记

        """
        data = session.query(Propertys).all()

        return {"code":200,"msg":"ok"}