from Background.createApp import getApp
from flask import Flask, request
from flask_cors import CORS  # 解决跨域的问题



app = getApp()
cors = CORS(app, resources={"/api/maintain/2": {"origins": "*"}})
@app.route('/api/maintain/2', methods=['post'])
def test():
    data = request.get_json(silent=True)
    print(data['aa'])

# 创建路由
@app.route("/")
def index():
    return "123"




if __name__ == "__main__":
    app.run()