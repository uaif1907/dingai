from flask_restful import Resource

class Company(Resource):
    def get(self):
        """
        获取全部公司
        :return:返回全部公司

        """
        return {"code":200,"msg":"ok"}