from Background.createApp import getApp

from flask import jsonify,request
import json




from flask import request,jsonify
from Background.database.db import session
from Background.database.property import Admins
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

app = getApp()


# 创建路由
@app.route("/api/login",methods=['POST'])
def login():
    data = request.json
    data = dict(data)
    # username = data.get("username",None)
    # password = data.get("password",None)
    username = data['username']
    password = data['password']
    if username and password:
        user = session.query(Admins).filter(Admins.username==username).first()
        if user:
            if user.password==password:
                # 创建token
                # s = Serializer(app.config['SECRET_KEY'],expires_in=60*10)
                s = Serializer(app.config['SECRET_KEY'], expires_in=60 * 10)
                token = str(s.__dict__['secret_key']).replace("b'",'').replace("'",'')
                # print(s,s.__dict__['secret_key'])

                # 用户信息保留在 session 会话
                # 返回 {'code':200,'msg':'yes','token':''}
                # return jsonify({'code':200,'msg':'yes','token':s.dumps({'id':user.id})})
                return jsonify({'code': 200, 'msg': 'yes', 'token': token})


    return jsonify({'code':'300','msg':'no'})




if __name__ == "__main__":
    app.run()