from Background.createApp import getApp


app = getApp()


# 创建路由
@app.route("/")
def index():
    return "123"


if __name__ == "__main__":
    app.run()