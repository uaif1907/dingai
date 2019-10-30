<template>
  <div class="ybp-box">
    <div class="ybp-top">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item :to="{ path: '/index' }">主页</el-breadcrumb-item>
        <el-breadcrumb-item><a href="">仪表盘</a></el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="">
<!--      上面卡篇-->
      <el-row :span="24">
        <el-col :span="4" style="padding-left: 10px; padding-right: 10px;">
          <el-card class="box-card card-top">
            <p class="title">待签字</p>
            <p class="number">221</p>
          </el-card>
        </el-col>
        <el-col :span="4" style="padding-left: 10px; padding-right: 10px;">
          <el-card class="box-card card-top">
            <p class="title">待签字</p>
            <p class="number">43</p>
          </el-card>
        </el-col>
        <el-col :span="4" style="padding-left: 10px; padding-right: 10px;">
          <el-card class="box-card card-top">
            <p class="title">待签字</p>
            <p class="number">213</p>
          </el-card>
        </el-col>
        <el-col :span="4" style="padding-left: 10px; padding-right: 10px;">
          <el-card class="box-card card-top">
            <p class="title">待签字</p>
            <p class="number">54</p>
          </el-card>
        </el-col>
        <el-col :span="4" style="padding-left: 10px; padding-right: 10px;">
          <el-card class="box-card card-top">
            <p class="title">待签字</p>
            <p class="number">66</p>
          </el-card>
        </el-col>
        <el-col :span="4" style="padding-left: 10px; padding-right: 10px;">
          <el-card class="box-card card-top">
            <p class="title">待签字</p>
            <p class="number">777</p>
          </el-card>
        </el-col>
      </el-row>
<!--下面饼图-->
      <el-row :span="24" style="margin: 20px 0">
        <el-col :span="12" style="padding-left: 10px; padding-right: 10px;">
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <i class="el-icon-pie-chart"></i>
              <span>资产概况</span>
            </div>
            <el-row :span="24">
              <el-col :span="12">
                <p style="height: 30px">在用</p>
                <el-progress type="circle" :percentage="46" :width="160" :stroke-width="14"></el-progress>
              </el-col>
              <el-col :span="12">
                <p style="height: 30px">闲置</p>
                <el-progress type="circle" :percentage="54" :width="160" :stroke-width="14" color="#67C23A"></el-progress>
              </el-col>
            </el-row>
          </el-card>
        </el-col>
        <el-col :span="12" style="padding-left: 10px; padding-right: 10px;">
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <i class="el-icon-pie-chart"></i>
              <span>资产状态占比</span>
            </div>
            <el-row>
              <el-col :span="24">
                <ve-pie :data="chartData" height="193px" :settings="chartSettings" :legend=legend :colors="color"></ve-pie>
              </el-col>
            </el-row>
          </el-card>
        </el-col>
      </el-row>
<!--折线图-->
      <el-row :span="24">
        <el-col :span="24">
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <i class="el-icon-pie-chart"></i>
              <span>资产分类统计</span>
            </div>
              <ve-histogram :data="means" :colors=color :tooltip="{trigger:'item'}"></ve-histogram>
          </el-card>
        </el-col>
      </el-row>
    </div>

  </div>
</template>

<script>
  export default {
    name: 'Zcdj',
    props: {
      // msg: String
    },
    data() {
      this.chartSettings = {
        radius:70,
        offsetY:100,
      };
      return {
        activeName: 'second',
        color:['#67C23A','#F56C6C','#409EFF'],
        chartData: {
          columns: ['状态', '访问用户'],
          rows: [
            { '状态': '闲置', '访问用户': 1393 },
            { '状态': '在用', '访问用户': 3530 },
            { '状态': '报废', '访问用户': 2923 },
          ]
        },
        legend:{
          type:'scroll',orient: 'vertical',right:30,top:10,bottom:10
        },
        means: {
          columns: ['分类', '数量'],
          rows: [
            { '分类': '土地、房屋及建筑物', '数量': 1393},
            { '分类': '专业设备', '数量': 3530},
            { '分类': '电器设备', '数量': 2923},
            { '分类': '电子产品及通信设备', '数量': 430},
            { '分类': '文艺体育设备', '数量': 923},
            { '分类': '图书文物及陈列品', '数量': 1920},
            { '分类': '家具用具及其他类', '数量': 620}
          ]
        }
      };
    },
    methods: {

    }

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .ybp-box{
    width: 100%;
    height: 100%;
  }
  .ybp-top{
    display: block;
    height: 50px;
  }
  .el-breadcrumb{
    line-height: 50px;
  }
  .ybp-bottom{
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
  .title{
    font-size: 12px;
    line-height: 30px;
    text-align: left;
  }
  .number{
    font-size: 24px;
    height: 40px;
    line-height: 50px;
    text-align: left;
  }
  .clearfix{
    text-align: left;
  }
  .clearfix i{
    font-size: 24px;
     vertical-align: middle;
  }
  .clearfix span{
     vertical-align: middle;
  }

</style>
