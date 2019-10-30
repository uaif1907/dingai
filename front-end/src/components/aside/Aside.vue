<template>
  <div class="aside-box">
      <div class="logo-box">
          <div class="logo-icon"></div>
          <p v-show="!isCollapse">丁艾资产</p>
      </div>
      <el-col :span="24">
          <el-menu
              default-active=""
              class="el-menu-vertical-demo"
              @open="handleOpen"
              @close="handleClose"
              background-color="#2f3e4e"
              text-color="#fff"
              :collapse="isCollapse"
              >
              <el-menu-item index="1">
                  <router-link tag="div" :to="{name:'Dashboard'}" style="display: flex">
                      <i class="iconfont icon-yibiaopan"></i>
                      <span>仪表盘</span>
                  </router-link>
              </el-menu-item>

              <el-menu-item index="2">
                  <router-link tag="div" :to="{name:'Register'}" style="display: flex">
                      <i class="iconfont icon-qianyuejilu"></i>
                      <span>资产登记</span>
                  </router-link>
              </el-menu-item>

              <el-menu-item index="3">
                  <router-link tag="div" :to="{name:'Collar'}" style="display: flex">
                      <i class="iconfont icon-jiekuanchulizhong2"></i>
                      <span>领用退库</span>
                  </router-link>
              </el-menu-item>

              <el-menu-item index="4">
                  <router-link tag="div" :to="{name:'Borrow'}" style="display: flex">
                      <i class="iconfont icon-dayin"></i>
                      <span>借用归还</span>
                  </router-link>
              </el-menu-item>

              <el-menu-item index="5">
                  <router-link tag="div" :to="{name:'Modify'}" style="display: flex">
                      <i class="iconfont icon-web-icon-"></i>
                      <span>信息修改</span>
                  </router-link>
              </el-menu-item>

              <el-menu-item index="6">
                  <router-link tag="div" :to="{name:'Repair'}" style="display: flex">
                      <i class="iconfont icon-weixiuguanli"></i>
                      <span>维修管理</span>
                  </router-link>
              </el-menu-item>

              <el-menu-item index="7">
                  <router-link tag="div" :to="{name:'Scrap'}" style="display: flex">
                      <i class="iconfont icon-19icon"></i>
                      <span>报废管理</span>
                  </router-link>
              </el-menu-item>

              <el-submenu index="8" class="zc-box">
                <template slot="title">
<!--                    <router-link tag="div" :to="{name:'Census'}" style="display: flex">-->
                    <div style="padding-left: 6px!important;">
                        <i class="iconfont icon-huaban"></i>
                        <span>资产统计</span>
                    </div>

<!--                    </router-link>-->
                </template>
                <el-menu-item-group>
                    <el-menu-item index="8-1">
                        <router-link tag="div" :to="{name:'Bill'}" style="display: flex">
                            <i class="iconfont icon-yuancircle46"></i>
                            <span>资产清单</span>
                        </router-link>
                    </el-menu-item>
                </el-menu-item-group>
              </el-submenu>

          </el-menu>
      </el-col>
  </div>
</template>

<script>
export default {
    name: 'Aside',
    props: {
        isCollapse:Boolean
    },

 methods: {
    handleOpen() {
        // console.log(key, keyPath);
    },
    handleClose() {
        // console.log(key, keyPath);
  },

 }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.logo-box{
    width: 100%;
    height: 56px;
    display: flex;
}
.logo-box p{
    font-size: 22px;
    line-height: 56px;
    color: white!important;
}
.logo-icon{
    width: 36px;
    height: 36px;
    background: url("../../assets/login/logoicon.png") no-repeat;
    background-size: contain;
    margin: 12px 5px 10px 16px;
}
.el-menu{
    width: auto;
    border: none;
}
.el-menu-item{
    text-align: left;
}
.el-menu-item i,.zc-box i{
    font-size: 18px;
    margin-right: 5px;
    text-align: center;
    vertical-align: middle;
    width: 24px;
}
.zc-box{
    text-align: left!important;
}

/*.el-menu{*/
/*    width: auto;*/
/*}*/


</style>
