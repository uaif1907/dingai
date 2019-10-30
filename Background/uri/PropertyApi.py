from flask_restful import Resource

class Property(Resource):
    def get(self):
        """
        获取资产登记
        :return:返回全部资产登记

        """
        return {"code":200,"msg":"ok"}