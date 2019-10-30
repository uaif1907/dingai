<template>
  <div class="libraty-box">
    <el-row>
      <!--                按钮-->
      <el-col :span="12">
        <el-button type="primary" size="small" icon="el-icon-plus" @click="addCollarDialogVisible = true">新增</el-button>
        <el-button size="small" icon="el-icon-printer">打印</el-button>
        <el-button size="small" icon="el-icon-daochu">导出</el-button>
      </el-col>
      <!--            日历-->
      <el-col :span="12">
        <el-button size="small" icon="el-icon-search" style="margin-left:10px;float:right;"></el-button>
        <el-date-picker
                v-model="sizeForm.date"
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

    <!--        表格-->
    <el-table :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)" border style="width: 100%;margin:10px 0;">
      <el-table-column fixed type="selection" width="55"></el-table-column>
      <el-table-column prop="collar_number" label="退库单号" width="160"></el-table-column>
      <el-table-column prop="collar_time" label="退库时间" width="120"></el-table-column>
      <el-table-column prop="department_name" label="仓库名称" width="342"></el-table-column>
      <el-table-column prop="company_name" label="退库使用公司" ></el-table-column>
      <el-table-column prop="personnel_name" label="处理人" width="120"></el-table-column>
      <el-table-column fixed="right" label="操作" width="100">
        <template slot-scope="scope">
          <el-button @click="handleClickShowCollar(scope.row)" type="text" >查看</el-button>
        </template>
      </el-table-column>
    </el-table>
    <!--        分页-->
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
    <!-- 新增退库 -->
    <el-dialog title="退库单" :visible.sync="addCollarDialogVisible" width="70%">
      <el-form ref="form" :model="addCollarForm" label-width="80px">
        <el-row>
          <el-col :span="12">
            <el-form-item label="退库处理人" size="small">
               <el-input v-model="addCollarForm.handle_name" placeholder="" disabled></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="退库时间">
              <el-date-picker
                      v-model="addCollarForm.collar_time"
                      type="date"
                      value-format="timestamp"
                      style="width:100%;"
                      placeholder="选择退库日期">
              </el-date-picker>
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item label="退库使用公司">
              <el-select v-model="addCollarForm.company_name" placeholder="请选择退库公司" style="width:100%;">
                <el-option label="康佳" value="康佳"></el-option>
                <el-option label="康宁" value="康宁"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="退库仓库">
              <el-select v-model="addCollarForm.department_name" placeholder="请选择退库仓库" style="width:100%;">
                <el-option label="北区仓库" value="北区仓库"></el-option>
                <el-option label="南区仓库" value="南区仓库"></el-option>
              </el-select>
            </el-form-item>
          </el-col>

          <el-col :span="24">
            <el-form-item label="退库说明">
              <el-input type="textarea" v-model="addCollarForm.collar_remarks" placeholder="退库备注"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
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
                <el-button type="primary" @click="addCollarDialogVisible = false">确 定</el-button>
            </span>
    </el-dialog>
    <!-- 查看退库 -->
    <el-dialog title="退库单" :visible.sync="showCollarDialogVisible" width="70%">
      <el-form ref="form" :model="showCollarForm" disabled label-width="80px" class="show-collar-form">
         <el-row>
          <el-col :span="12">
            <el-form-item label="退库处理人" size="small">
               <el-input v-model="showCollarForm.personnel_name" placeholder="" disabled></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="退库时间">
              <el-date-picker
                      v-model="showCollarForm.expect_time"
                      type="date"
                      value-format="timestamp"
                      style="width:100%;"
                      placeholder="选择退库日期">
              </el-date-picker>
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item label="退库使用公司">
              <el-select v-model="showCollarForm.company_name" placeholder="请选择退库公司" style="width:100%;">
                <el-option label="康佳" value="康佳"></el-option>
                <el-option label="康宁" value="康宁"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="退库仓库">
              <el-select v-model="showCollarForm.department_name" placeholder="请选择退库仓库" style="width:100%;">
                <el-option label="北区仓库" value="北区仓库"></el-option>
                <el-option label="南区仓库" value="南区仓库"></el-option>
              </el-select>
            </el-form-item>
          </el-col>

          <el-col :span="24">
            <el-form-item label="退库说明">
              <el-input type="textarea" v-model="showCollarForm.collar_remarks" placeholder="一级棒"></el-input>
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
      </el-form>

      <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="showCollarDialogVisible = false">确 定</el-button>
            </span>
    </el-dialog>

  </div>
</template>

<script>
  import Selectuser from '@/components/Withdraw/selectuser.vue'
  import Selectedassets from '@/components/Withdraw/selectedassets.vue'
  export default {
    name: 'library',
    props: {
      // isCollapse:Boolean
    },
    data(){
      return{
        total:100,//默认数据总数
                currentPage:1,//默认开始页面
                pageSize:10,//每页的数据条数
        searchDate:[],
        addCollarDialogVisible:false,
        selectPersonDialogVisible:false, //选择联系人对话框状态
        addCollarForm:{},
        showCollarForm:{},
        showCollarDialogVisible:false,
        selectAssetsDialogVisible:false,
        selectedCollarAssetsData:[], //已选择资产
        selectCollarAssetsData:[],   //正在选择资产
        currentPage2: 1,
        sizeForm: {
          data:''
        },
        tableData: [
          {
            id:1,
            collar_number:'TK20180618003',
            collar_time:'2018-06-18',
            personnel_name:'张三',
            department_name:'北区仓库',
            company_name:'康达',
            expect_time:'1529254718034',
            collar_remarks:'一级棒'
          },
          {
            id:2,
            collar_number:'TK20180618003',
            collar_time:'2018-06-18',
            personnel_name:'李四',
            department_name:'北区仓库',
            company_name:'康达',
            expect_time:'1529254718034',
            collar_remarks:'一级棒'
          },
          {
            id:3,
            collar_number:'TK20180618003',
            collar_time:'2018-06-18',
            personnel_name:'王五',
            department_name:'北区仓库',
            company_name:'康达',
            expect_time:'1529254718034',
            collar_remarks:'一级棒'
          },
          {
            id:4,
            collar_number:'TK20180618003',
            collar_time:'2018-06-18',
            personnel_name:'赵柳',
            department_name:'南区仓库',
            company_name:'康达',
            expect_time:'1529254718034',
            collar_remarks:'一级棒'
          },
        ],
      }
    },
    methods: {
      deleteRow(index, rows) {
        rows.splice(index, 1);
      },
      handleSizeChange(val) {
        console.log(`每页 ${val} 条`);
      },
      handleCurrentChange(val) {
        console.log(`当前页: ${val}`);
      },
      handleSelectionDone(){
        this.selectAssetsDialogVisible = false; //隐藏选择资产弹窗
        this.selectedCollarAssetsData = this.selectCollarAssetsData; //将选择的资产放入已选择资产中
      },
      handleAddGetPerson(row){
        this.selectPersonDialogVisible = false;
        this.addCollarForm.personnel_id = row.personnel_id;
        this.addCollarForm.personnel_name = row.personnel_name;
      },
      handleClickShowCollar(data){
        this.showCollarDialogVisible = true;
        this.showCollarForm = data;
      }
    },
    components:{
      Selectuser,
      Selectedassets
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .el-col{
    /*float: left;*/
    text-align: left!important;
  }
  .el-row{
    text-align: left!important;
  }

</style>