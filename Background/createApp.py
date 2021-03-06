from flask import Flask
# restful
from flask_restful import Api
# URI
from .uri.UserApi import User
from .uri.ChangeApi import Change
from .uri.CancellingApi import Cancelling
from .uri.changesApi import Changes
from .uri.AdminApi import Admin
from .uri.CompanyApi import Company
from .uri.DepartmentApi import Department
from .uri.PropertyApi import Property








from .uri.MaintainApi import Maintain
from .uri.OptionApi import Option

def getApp():
    # 创建应用
    app = Flask(__name__)
    # 配置信息
    app.config.from_object("config")

    api = Api(app)



    # 注册接口
    api.add_resource(Option,"/api/option", endpoint="Option")
    api.add_resource(User,"/api/user/<int:cid>/<int:did>",endpoint="user")
    api.add_resource(Cancelling,"/api/cancelling/<int:aid>/<int:area>/<int:rid>",endpoint="cancelling")
    api.add_resource(Admin, "/api/admin", endpoint="admin")
    api.add_resource(Company, "/api/company", endpoint="company")
    api.add_resource(Department, "/api/department", endpoint="department")
    api.add_resource(Property, "/api/property", endpoint="property")
    api.add_resource(Change, "/api/change", endpoint="change")

    api.add_resource(Changes, "/api/changes", endpoint="changes")
    api.add_resource(Maintain, "/api/maintain/<int:uid>", endpoint="maintain")

    # api.add_resource(Maintain, "/api/maintain", endpoint="maintain")


    return app