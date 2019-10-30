from flask import Flask
# restful
from flask_restful import Api
# URI
from .uri.UserApi import User
from .uri.CancellingApi import Cancelling


def getApp():
    # 创建应用
    app = Flask(__name__)
    # 配置信息
    app.config.from_object("config")
    api = Api(app)

    # 注册接口
    api.add_resource(User,"/api/user/<int:cid>/<int:did>",endpoint="user")
    api.add_resource(Cancelling,"/api/cancelling/<int:aid>/<int:area>/<int:rid>",endpoint="cancelling")


    return app