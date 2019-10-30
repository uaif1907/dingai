<template>
  <div class="index-box" >
    <el-container>
<!--        侧导航-->
        <el-aside  :style="{width:isCollapse?'auto':'200px'}">
            <Aside :isCollapse="isCollapse" ></Aside>
        </el-aside>
<!--        右侧-->
        <el-main class="right-box">
            <el-container>
                <el-header>
                    <Header v-model="isCollapse" v-on:togger="togger" :isCollapse="isCollapse"></Header>
                </el-header>
                <el-main class="bottom-box">
                    <router-view></router-view>
                </el-main>
            </el-container>
        </el-main>
    </el-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Aside from '@/components/aside/Aside.vue'
import Header from '@/components/header/header.vue'

export default {
    name: 'index',
    components: {
      Aside,
      Header,
    },
    data(){
      return {
          isCollapse:false
      }
    },
    methods:{
        togger(){
            this.isCollapse=!this.isCollapse
        }
    }
}
</script>
<style>
    .index-box{
        width: auto;
        height: 100%;
    }
    .el-container{
        height: 100%;
    }
    .el-aside{
        /*width: auto!important;*/
        background-color: rgb(47, 62, 78);
        transition: all 0.5s!important;
    }
    .el-header{
        background-color: #ffffff;
        transition: all 0.5s linear;
        border-bottom: 1px solid #e6e6e6;
    }
    .bottom-box{
        background-color: #ffffff;
    }
    .right-box{
        padding: 0;
    }
    .el-menu-item-group__title{
        padding: 0!important;
    }
    .el-header{
        padding: 0!important;
    }
    .icon-rotate{
        transform: rotate(90deg);
    }
    .el-submenu__title{
        height: 59px!important;
    }
    .el-upload--text{
        height: 100px!important;
        border: 1px dashed #d9d9d9!important;
    }
    .el-dialog__header{
        text-align: left!important;
    }
    .el-button  {
        font-size: 12px!important;
    }
    .el-form-item__label{
        width: 100px!important;
    }
    .el-form-item__content{
        margin-left: 100px!important;
    }
    .el-upload--text{
        width: 100% !important;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .card-top .el-card__body{
        padding: 10px 20px;
        border-radius: 4px;
        box-shadow: 0 2px 12px 0 rgba(0,0,0,.1);
        color: #fff;
        background: #409eff url("../../assets/login/bj.png") no-repeat bottom/auto;
    }
</style>