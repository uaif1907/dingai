from flask_restful import Resource
# from ..database.property import Cancellings as cl

class Cancelling(Resource):
    def get(self,aid,area,rid):
        """
        获取用户信息
        :param aid: 退库处理人
        :param time: 退库时间
        :param area: 退库仓库
        :param explain: 退库说明
        :param rid: 领用表
        :return:  返回此表所有信息
        """
        # print(cl.aid)
        print("2333")
        return {"code":200,"msg":'ok'}


