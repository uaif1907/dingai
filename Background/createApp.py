from flask import Flask
# restful
from flask_restful import Api
# URI
from .uri.UserApi import User
from .uri.AdminApi import Admin
from .uri.CompanyApi import Company
from .uri.DepartmentApi import Department
from .uri.PropertyApi import Property

def getApp():
    # 创建应用
    app = Flask(__name__)
    # 配置信息
    app.config.from_object("config")
    api = Api(app)
    api.add_resource(User,"/api/user/<int:cid>/<int:did>",endpoint="user")
    api.add_resource(Admin, "/api/admin", endpoint="admin")
    api.add_resource(Company, "/api/company", endpoint="company")
    api.add_resource(Department, "/api/department", endpoint="department")
    api.add_resource(Property, "/api/property", endpoint="property")

    return app