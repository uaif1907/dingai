from flask import Flask
# restful
from flask_restful import Api
# URI
from .uri.UserApi import User
from .uri.CancellingApi import Cancelling


from .uri.AdminApi import Admin
from .uri.CompanyApi import Company
from .uri.DepartmentApi import Department
from .uri.PropertyApi import Property
from .uri.MaintainApi import Maintain
def getApp():
    # 创建应用
    app = Flask(__name__)
    # 配置信息
    app.config.from_object("config")
    api = Api(app)

    # 注册接口
    api.add_resource(User,"/api/user/<int:cid>/<int:did>",endpoint="user")
    api.add_resource(Cancelling,"/api/cancelling/<int:aid>/<int:area>/<int:rid>",endpoint="cancelling")
    api.add_resource(Admin, "/api/admin", endpoint="admin")
    api.add_resource(Company, "/api/company", endpoint="company")
    api.add_resource(Department, "/api/department", endpoint="department")
    api.add_resource(Property, "/api/property", endpoint="property")

    api.add_resource(Maintain, "/api/maintain/<int:uid>", endpoint="maintain")
    return app