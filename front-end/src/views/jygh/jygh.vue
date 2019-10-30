<template>
  <div class="jygh-box">
    <div class="jygh-top">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item :to="{ path: '/index' }">主页</el-breadcrumb-item>
        <el-breadcrumb-item><a href="">借用归还</a></el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="jygh-bottom">
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="借用" name="second">
          <!--          上面-->
          <el-row>
            <!--左边-->
            <el-col :span="12">
              <el-button type="primary" icon="el-icon-plus" size="small"  @click="addCollarDialogVisible = true">新增</el-button>
              <el-button type="primary" icon="el-icon-document" size="small" @click="restore">归还</el-button>
              <el-button icon="el-icon-printer" size="small">打印</el-button>
              <el-button icon="el-icon-upload2" size="small">导出</el-button>
            </el-col>
            <!--右边-->
            <el-col :span="12">
              <el-button size="small" icon="el-icon-search" style="margin-left:10px;float:right;"></el-button>
              <el-date-picker
                      v-model="date"
                      type="daterange"
                      range-separator="至"
                      start-placeholder="开始日期"
                      end-placeholder="结束日期"
                      style="float:right;"
                      size="small"
              >
              </el-date-picker>
            </el-col>
          </el-row>
          <!--          下面表格-->
          <el-table :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)" border style="width: 100%;margin: 10px 0;" @selection-change="handleSelectionChange">
            <el-table-column align="center" fixed type="selection" width="55"></el-table-column>
            <el-table-column fixed prop="status" align="center" label="状态" width="80">
              <template slot-scope="scope">
                <Status :status="scope.row.status"></Status>
              </template>
            </el-table-column>
            <el-table-column prop="borrow_number" label="借用单号" width="160"></el-table-column>
            <el-table-column prop="borrow_time" label="借用时间" width="120"></el-table-column>
            <el-table-column prop="personnel_name" label="借用人" width="120"></el-table-column>
            <el-table-column prop="borrow_name" label="借出处理人" width="120"></el-table-column>
            <el-table-column prop="zip" label="归还处理人" width="120"></el-table-column>
            <el-table-column prop="expect_time" label="预计归还时间" width="120"></el-table-column>
            <el-table-column prop="revert_time" label="归还时间" width="120"></el-table-column>
            <el-table-column fixed="right" align="center" label="操作" width="120">
              <template slot-scope="scope">
                <el-button @click="handleClickShowCollar(scope.row)" type="text" size="small">查看</el-button>
              </template>
            </el-table-column>
          </el-table>
          <!--          分页-->
          <div class="block">
            <el-pagination
                    @size-change="handleSizeChange"
                    @current-change="handleCurrentChange"
                    :current-page.sync="currentPage"
                    :page-sizes="[10, 20, 30, 40]"
                    :page-size="pageSize"
                    layout="sizes, prev, pager, next"
                    :total="total"
                    background>
            </el-pagination>
          </div>

          <!--        新增借用-->
          <el-dialog title="借用单" :visible.sync="addCollarDialogVisible" width="70%">
            <el-form ref="form" :model="addCollarForm" label-width="80px">
              <el-row>
                <el-col :span="8">
                  <el-form-item label="借用人">
                    <el-input v-model="addCollarForm.personnel_name">
                      <el-button slot="append" icon="el-icon-user-solid" @click="selectPersonDialogVisible=true"></el-button>
                    </el-input>
                  </el-form-item>
                </el-col>
                <el-col :span="8">
                  <el-form-item label="借出时间">
                    <el-date-picker
                            v-model="addCollarForm.collar_time"
                            type="date"
                            value-format="timestamp"
                            style="width:100%;"
                            placeholder="选择借出时间">
                    </el-date-picker>
                  </el-form-item>
                </el-col>
                <el-col :span="8">
                  <el-form-item label="预计归还">
                    <el-date-picker
                            v-model="addCollarForm.expect_retreat"
                            type="date"
                            value-format="timestamp"
                            style="width:100%;"
                            placeholder="预计归还时间">
                    </el-date-picker>
                  </el-form-item>
                </el-col>
                <el-col :span="8">
                  <el-form-item label="借出处理人">
                    <el-input v-model="addCollarForm.collar_address" placeholder="借出处理人"></el-input>
                  </el-form-item>
                </el-col>
                <el-col :span="8">
                  <el-form-item label="预计归还">
                    <el-date-picker
                            v-model="addCollarForm.expect_retreat"
                            type="date"
                            value-format="timestamp"
                            style="width:100%;"
                            placeholder="预计归还时间">
                    </el-date-picker>
                  </el-form-item>
                </el-col>
                <el-col :span="8">
                  <el-form-item label="归还处理人">
                    <el-input v-model="addCollarForm.handle_name" placeholder="归还处理人" disabled></el-input>
                  </el-form-item>
                </el-col>
                <el-col :span="16">
                  <el-form-item label="说明">
                    <el-input type="textarea" v-model="addCollarForm.collar_remarks" placeholder="领用备注"></el-input>
                  </el-form-item>
                </el-col>
              </el-row>
              <el-row style="text-align: left">
                <el-button @click="selectAssetsDialogVisible=true">选择资产</el-button>
                <el-button type="danger">删除</el-button>
              </el-row>
              <el-table :data="selectCollarAssetsData" border style="width: 100%;margin:10px 0;">
                <el-table-column fixed type="selection" width="55"></el-table-column>
                <el-table-column prop="bar_code" label="资产条码" width="140"> </el-table-column>
                <el-table-column prop="name" label="资产名称" width="150"> </el-table-column>
                <el-table-column prop="type_id" label="资产类型" width="150"> </el-table-column>
                <el-table-column prop="company" label="使用公司" width="100"> </el-table-column>
                <el-table-column prop="department" label="使用部门" width="100"> </el-table-column>
                <el-table-column prop="user_id" label="使用人" width="100"> </el-table-column>
                <el-table-column prop="manager_id" label="管理员" width="100"> </el-table-column>
                <el-table-column prop="address" label="存放地点" width="100"> </el-table-column>
              </el-table>
            </el-form>
            <!-- 选择领用人 -->
            <el-dialog title="选择用户" :visible.sync="selectPersonDialogVisible" width="70%" append-to-body>
              <Selectuser :handleAddGetPerson="handleAddGetPerson"></Selectuser>
              <span slot="footer" class="dialog-footer">
                    <el-button @click="selectPersonDialogVisible = false">取 消</el-button>
                </span>
            </el-dialog>
            <!-- 选择资产弹窗 -->
            <el-dialog title="选择资产" :visible.sync="selectAssetsDialogVisible" width="70%" append-to-body>
              <Selectedassets></Selectedassets>
              <span slot="footer" class="dialog-footer">
                    <el-button @click="selectAssetsDialogVisible = false">取 消</el-button>
                    <el-button type="primary" @click="handleSelectionDone">确 定</el-button>
                </span>
            </el-dialog>
            <span slot="footer" class="dialog-footer">
                <el-button @click="addCollarDialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="fun1(addCollarForm)">确 定</el-button>
            </span>
          </el-dialog>
          <!--        查看借用-->
          <el-dialog
                  title="借用单"
                  :visible.sync="showCollarDialogVisible"
                  width="70%">
            <el-form ref="form" :model="showCollarForm" disabled label-width="80px" class="show-collar-form">
              <!--              <el-form ref="form" :model="addCollarForm" label-width="80px">-->
              <el-row>
                <el-col :span="8">
                  <el-form-item label="借用人">
                    <el-input v-model="showCollarForm.personnel_name"></el-input>
                  </el-form-item>
                </el-col>
                <el-col :span="8">
                  <el-form-item label="借出时间">
                    <el-date-picker
                            v-model="showCollarForm.borrow_times"
                            type="date"
                            value-format="timestamp"
                            style="width:100%;"
                            placeholder="选择借出时间">
                    </el-date-picker>
                  </el-form-item>
                </el-col>
                <el-col :span="8">
                  <el-form-item label="预计归还">
                    <el-date-picker
                            v-model="showCollarForm.revert_times"
                            type="date"
                            value-format="timestamp"
                            style="width:100%;"
                            placeholder="预计归还时间">
                    </el-date-picker>
                  </el-form-item>
                </el-col>
                <el-col :span="8">
                  <el-form-item label="借出处理人">
                    <el-input v-model="showCollarForm.borrow_name" placeholder="借出处理人"></el-input>
                  </el-form-item>
                </el-col>
                <el-col :span="8">
                  <el-form-item label="预计归还">
                    <el-date-picker
                            v-model="showCollarForm.revert_times"
                            type="date"
                            value-format="timestamp"
                            style="width:100%;"
                            placeholder="预计归还时间">
                    </el-date-picker>
                  </el-form-item>
                </el-col>
                <el-col :span="8">
                  <el-form-item label="归还处理人">
                    <el-input v-model="showCollarForm.handle_name" placeholder="归还处理人" disabled></el-input>
                  </el-form-item>
                </el-col>
                <el-col :span="16">
                  <el-form-item label="说明">
                    <el-input type="textarea" v-model="showCollarForm.collar_remarks" placeholder="领用备注"></el-input>
                  </el-form-item>
                </el-col>
              </el-row>
              <el-table :data="selectCollarAssetsData" border style="width: 100%;margin:10px 0;">
                <el-table-column fixed type="selection" width="55"></el-table-column>
                <el-table-column prop="bar_code" label="资产条码" width="140"> </el-table-column>
                <el-table-column prop="name" label="资产名称" width="150"> </el-table-column>
                <el-table-column prop="type_id" label="资产类型" width="150"> </el-table-column>
                <el-table-column prop="company" label="使用公司" width="100"> </el-table-column>
                <el-table-column prop="department" label="使用部门" width="100"> </el-table-column>
                <el-table-column prop="user_id" label="使用人" width="100"> </el-table-column>
                <el-table-column prop="manager_id" label="管理员" width="100"> </el-table-column>
                <el-table-column prop="address" label="存放地点" width="100"> </el-table-column>
              </el-table>
              <!--            </el-form>-->
            </el-form>

            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="showCollarDialogVisible = false">确 定</el-button>
            </span>
          </el-dialog>

        </el-tab-pane>
      </el-tabs>
    </div>

  </div>
</template>

<script>
  import Selectuser from '@/components/Withdraw/selectuser.vue'
  import Selectedassets from '@/components/Withdraw/selectedassets.vue'
  import Status from'@/components/data/status.vue'
  export default {
    name: 'Zcdj',
    props: {
      // msg: String
    },
    data() {
      return {
        total:100,//默认数据总数
        currentPage:1,//默认开始页面
        pageSize:10,//每页的数据条数
        revert:[],
        showCollarForm:{},
        showCollarDialogVisible:false,
        selectedCollarAssetsData:{},
        selectAssetsDialogVisible:false,
        selectPersonDialogVisible:false,
        selectCollarAssetsData:[],
        addCollarForm:{},
        addCollarDialogVisible:false,
        activeName: 'second',
        date:'',
        currentPage2: 1,
        tableData: [{
          id:1,
          borrow_number:'JY20180618003',
          borrow_time:'2018-06-13',
          borrow_times:'1529254718034',
          expect_time:'2019-07-03',
          expect_revert:'1529254718034',
          personnel_name:'张三',
          borrow_name:'allcky',
          department_name:'研发部',
          company_name:'康达',
          revert_time:'2021-12-12',
          revert_times:'1639254711111',
          status:2,
        }],
      };
    },
    methods: {
      handleClick(row) {
        console.log(row);
      },
      handleAddGetPerson(row){//借用人
        this.selectPersonDialogVisible = false;
        this.addCollarForm.personnel_id = row.personnel_id;
        this.addCollarForm.personnel_name = row.personnel_name;
      },
      handleSelectionDone(){//资产
        this.selectAssetsDialogVisible = false;
        this.selectedCollarAssetsData = this.selectCollarAssetsData;
      },
      fun1(data){//添加数据
        this.addCollarDialogVisible = false;
        this.tableData.push(data)
      },
      handleClickShowCollar(data){
        this.showCollarDialogVisible = true;
        this.showCollarForm = data;
      },
      handleSizeChange(val) {
        console.log(`每页 ${val} 条`);
      },
      handleCurrentChange(val) {
        console.log(`当前页: ${val}`);
      },
      //删除
      restore:function(){
        if(this.revert.length==0){
          this.$message('请选中要归还的数据条目！');
          return;
        }
        this.$confirm('此操作将归还该数据, 是否继续?', '资产归还确认提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          //要还原的资产
          if(true){
            this.$message({
              type: 'success',
              message: '归还成功!'
            });
            //获取最新 报废单列表
            this.tableData = []
          }else{
            this.$message({
              type: 'warning',
              message: '归还失败!'
            });
          }

        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消还原'
          });
        });
      },
      //选择要删除的单
      handleSelectionChange:function(val){
        //获取选中的删除条目ID
        this.revert = val.map((val)=>{
          return val.scrap_number
        })
      },
    },
    components:{
      Status,
      Selectedassets,
      Selectuser
    }

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .jygh-box{
    width: 100%;
    height: 100%;
  }
  .jygh-top{
    display: block;
    height: 50px;
  }
  .el-breadcrumb{
    line-height: 50px;
  }
  .jygh-bottom{
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
  .el-col {
    text-align: left!important;
  }
</style>
