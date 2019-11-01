from Background.createApp import getApp
<<<<<<< HEAD
from flask import jsonify,request




=======
from flask import request,jsonify
from Background.database.db import session
from Background.database.property import Admins
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
>>>>>>> ad693b392890a7ea272972a04419257b59ca9a2b
app = getApp()


# 创建路由
@app.route("/api/login",methods=['POST'])
def login():
    data = request.json
    username = data.get("username",None)
    password = data.get("password",None)
    if username and password:
        user = session.query(Admins).filter(Admins.username==username).first()
        if user:
            if user.password==password:
                # 创建token
                s = Serializer(app.config['SECRET_KEY'],expires_in=60*10)

                # 用户信息保留在 session 会话
                # 返回 {'code':200,'msg':'yes','token':''}
                return jsonify({'code':200,'msg':'yes','token':s.dumps({'id':user.id})})

    return jsonify({'code':'200','msg':'no'})




if __name__ == "__main__":
    app.run()