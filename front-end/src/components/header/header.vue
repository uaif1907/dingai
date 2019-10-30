<template>
  <div class="header-box">
<!--      左边icon-->
      <div class="icon" @click="tomenu">
          <i class="el-icon-s-fold" :class="{'icon-rotate':isCollapse}"></i>
      </div>
<!--      右面-->
      <el-menu class="el-menu-demo" mode="horizontal" @select="handleSelect">
<!--        消息-->
          <el-submenu index="1">
            <template slot="title">
                <i class="el-icon-bell"></i>
                <span>消息</span>
            </template>
            <el-menu-item index="1-1">
                <div class="left">
                    <i class="el-icon-bell"></i>
                </div>
                <div class="right">
                    <p>新功能上线通知</p>
                    <span>2018-08-10</span>
                </div>
            </el-menu-item>
            <el-menu-item index="1-2">
            <div class="left">
                <i class="el-icon-bell"></i>
            </div>
            <div class="right">
                <p>新功能上线通知</p>
                <span>2018-08-10</span>
            </div>
        </el-menu-item>
            <el-menu-item index="1-3">
            <div class="left">
                <i class="el-icon-bell"></i>
            </div>
            <div class="right">
                <p>新功能上线通知</p>
                <span>2018-08-10</span>
            </div>
        </el-menu-item>
          </el-submenu>
<!--            管理员-->
          <el-submenu index="2">
            <template slot="title">
                <i class="el-icon-s-custom"></i>
                <span>管理员</span>
            </template>
            <el-menu-item index="2-1">
                <i class="iconfont icon-xiugaimima"></i>
                <span>修改密码</span>
            </el-menu-item>
            <el-menu-item index="2-2" class="user-box">
                <i class="el-icon-edit-outline"></i>
                <span>修改资料</span>
            </el-menu-item>
            <el-menu-item index="2-3">
                <i class="el-icon-switch-button"></i>
                <span>退出登录</span>
            </el-menu-item>
          </el-submenu>
<!--          帮助-->
          <el-submenu index="3">
            <template slot="title">
                <i class="el-icon-question"></i>
                <span>帮助</span>
            </template>
            <el-menu-item index="3-1">
                <i class="el-icon-question"></i>
                <span>帮助中心</span>
            </el-menu-item>
            <el-menu-item index="3-2">
                <i class="el-icon-document"></i>
                <span>使用手册</span>
            </el-menu-item>
          </el-submenu>

      </el-menu>
  </div>
</template>

<script>
export default {
    name: 'Aside',
    props: {
        isCollapse:Boolean
    },
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1',
      };
    },
    methods: {
        handleSelect() {
            // console.log(key, keyPath);
        },
        tomenu(){
            this.$emit("togger")
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.icon{
    color: #2f3e4e;
    float: left;
    font-size: 20px;
    height: 60px;
    line-height: 60px;
    text-align: center;
    width: 60px;
    cursor: pointer;
}
.el-menu-demo{
    float: right;
    border: none;
}
/*消息下面*/
.el-menu-item{
    height: auto!important;
    display: flex;
}
.left{
    width: 36px;
    height: 36px;
    margin: 7px 10px 7px 0;
}
.el-menu-item .left i{
    background-color: #f2f2f2;
    border-radius: 50%;
    height: 100%;
    line-height: 36px;
    text-align: center;
    width: 100%;
}
.right{
    height: 40px;
    line-height: 20px;
    margin: 5px 0;
    font-size: 12px;
}
/*管理员下面*/
.el-menu-item i{
    font-size: 18px;
    margin-right: 5px;
    text-align: center;
    vertical-align: middle;
    width: 24px;
    line-height: 36px;
}
i{
    transition:all .5s;
}
.icon-rotate{
    transform: rotate(90deg);
}

</style>
