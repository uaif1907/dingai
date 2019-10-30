<template>
  <div class="zvdj-box">
    <div class="zvdj-top">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item :to="{ path: '/index' }">主页</el-breadcrumb-item>
        <el-breadcrumb-item><a href="">信息修改</a></el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="zvdj-bottom">
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="基本信息变更" name="second">
          <changeInformation></changeInformation>
        </el-tab-pane>
        <el-tab-pane label="维保信息变更" name="third">
          <changeMaintenance></changeMaintenance>
        </el-tab-pane>
      </el-tabs>
    </div>

  </div>
</template>

<script>
  import changeInformation from '@/components/information/changeInformation.vue'
  import changeMaintenance from '@/components/information/changeMaintenance.vue'
  export default {
    name: 'Zcdj',
    props: {
      // msg: String
    },
    data() {
      return {
        activeName: 'second'
      };
    },
    methods: {
      handleClick(tab, event) {
        console.log(tab, event);
      }
    },
    components:{
      changeInformation,
      changeMaintenance
    }

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .zvdj-box{
    width: 100%;
    height: 100%;
  }
  .zvdj-top{
    display: block;
    height: 50px;
  }
  .el-breadcrumb{
    line-height: 50px;
  }
  .zvdj-bottom{
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
