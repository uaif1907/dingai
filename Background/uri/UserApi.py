from flask_restful import Resource

class User(Resource):
    def get(self,cid,did):
        """
        获取用户信息
        :param cid: 公司id
        :param did: 部门id
        :return:  返回此部门下所有的用户
        """
        return {"code":200,"msg":'ok'}