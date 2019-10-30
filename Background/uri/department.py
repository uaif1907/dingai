from flask_restful import Resource

class Department(Resource):
    def get(self,id):
        """
        获取公司对应部门
        :param id:  公司id
        :return:  此公司下所有部门
        """
        pass