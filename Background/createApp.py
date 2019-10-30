from flask import Flask
# restful
from flask_restful import Api
# URI
from .uri.UserApi import User



def getApp():
    # 创建应用
    app = Flask(__name__)
    # 配置信息
    app.config.from_object("config")
    api = Api(app)
    api.add_resource(User,"/api/user/<int:cid>/<int:did>",endpoint="user")


    return app