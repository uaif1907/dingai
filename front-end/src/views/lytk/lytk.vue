<template>
  <div class="lytk-box">
    <div class="lytk-top">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item :to="{ path: '/index' }">主页</el-breadcrumb-item>
        <el-breadcrumb-item><a href="">领用退库</a></el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="lytk-bottom">
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="领用" name="second">
          <Withdraw></Withdraw>
        </el-tab-pane>

        <el-tab-pane label="退库" name="third">
          <Library></Library>
        </el-tab-pane>

      </el-tabs>

    </div>

  </div>
</template>

<script>
  import Withdraw from '@/components/Withdraw/withdraw.vue'
  import Library from '@/components/Withdraw/library.vue'
  export default {
    name: 'lytk',
    props: {
      // msg: String
    },
    components:{
      Withdraw,
      Library
    },
    data() {
      return {
        activeName: 'second'
      };
    },
    methods: {
      handleClick() {
        // console.log(tab, event);
      }
    }

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .lytk-box{
    width: 100%;
    height: 100%;
  }
  .lytk-top{
    display: block;
    height: 50px;
  }
  .el-breadcrumb{
    line-height: 50px;
  }
  .lytk-bottom{
    width: auto;
    height: auto;
    padding: 20px;
    box-shadow: 0 2px 12px 0 rgba(0,0,0,.1);
    background-color: #ffffff;
    border: 1px solid #ebeef5;
    color: #303133;
    transition: .3s;
    overflow: hidden;
  }

</style>
