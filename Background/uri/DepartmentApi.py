from flask_restful import Resource

class Department(Resource):
    def get(self):
        """
        获取公司对应部门
        :param cid:
        :return: 部门信息
        """
        return {"code":200,"msg":"ok"}