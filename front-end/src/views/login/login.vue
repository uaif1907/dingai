<template>
  <div class="login-box">
    <div class="loginCon">

      <div class="login-left"></div>

      <div class="login-right">
        <p>用户登录</p>
        <el-form :model="ruleForm" :rules="rules" status-icon ref="ruleForm">

          <el-form-item prop="username">
            <el-input placeholder="请输入用户名" clearable v-model="ruleForm.username" style="width: 284px"></el-input>
          </el-form-item>

          <el-form-item prop="password">
            <el-input placeholder="请输入密码" clearable v-model="ruleForm.password" type="password" style="width: 284px"></el-input>
          </el-form-item>

          <el-button type="primary" style="width:284px" @click="onSubmit('ruleForm')">登录</el-button>

        </el-form>
      </div>
    </div>
<!--    版权-->
    <div class="copyright">
      <p>Copyright ©2018 dingai, All Rights Reserved.</p>
    </div>
<!--    退出-->
    <div class="close">
      <i class="el-icon-close"></i>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'login',
  components: {
    // HelloWorld
  },
  data(){
    return {
      ruleForm:{
        username:'',
        password:''
      },
      rules:{
        username:[
          { required: true, message: '请输入用户名',trigger:'blur'},
          { min: 3, max: 5, message: '长度在3到5字符', trigger: 'blur' }
        ],
        password:[
          { required: true, message: '请输入密码',trigger:'blur'},
          { min: 6, message: '密码长度在6位以上', trigger: 'blur' }
        ]
      }
    }
  },
  methods:{
    onSubmit(formName){
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$message({
            message: '登录成功',
            type: 'success',
        });
          this.$router.push({name:"index"});
        } else {
          this.$message.error('登录失败');
            return false;
          }
        });
    }
  }
}
</script>
<style>
  .login-box{
    width: 100%;
    height: 100%;
    background: url("../../assets/login/login.jpg");
    background-size: cover;
  }
  .loginCon{
    width: 550px;
    height: 230px;
    /*background-color: red;*/
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    margin: auto;
  }
  /*左边*/
  .login-left{
    float: left;
    width: 240px;
    height: 230px;
    background: url("../../assets/login/logo.png") no-repeat;
    background-size: contain;
    border-right: 1px solid hsla(0,0%,100%,.2);
    box-sizing: border-box;
  }
  /*右面*/
  .login-right{
    width: 310px;
    height: 230px;
    float: right;
    padding: 0 13px;
    box-sizing: border-box;
  }
  .login-right p{
    width: 284px;
    height: 40px;
    color: #fff;
    font-size: 16px;
    line-height: 40px;
    text-align: left;
    margin: 0 auto;
  }
  .copyright{
    width: 100%;
    height: 50px;
    font-size: 12px;
    text-align: center;
    color: hsla(0,0%,100%,0.5);
    line-height: 50px;
    position: absolute;
    bottom: 0;
  }
  /*退出*/
  .close{
    width: 50px;
    height: 50px;
    position: absolute;
    right: 20px;
    top: 5px;
    background-color: rgba(51,128,255,0.9);
    transition: all 0.3s linear;
    cursor: pointer;
  }
  .close i{
    font-size: 26px;
    color: #ffffff;
    line-height: 50px;
  }
  .close:hover{
    transform: scale(1.1);
  }
</style>