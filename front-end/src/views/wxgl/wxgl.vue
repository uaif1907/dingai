<template>
    <div class="wxgl-box">
        <div class="wxgl-top">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item :to="{ path: '/index' }">主页</el-breadcrumb-item>
                <el-breadcrumb-item><a href="">维修管理</a></el-breadcrumb-item>
            </el-breadcrumb>
        </div>

        <div class="wxgl-bottom">
            <el-row>
                <!--按钮-->
                <el-col :span="12">
                    <el-button type="primary" size="small" icon="el-icon-plus" @click="addCollarDialogVisible = true">新增</el-button>
                    <el-button size="small" icon="el-icon-printer">打印</el-button>
                    <el-button size="small" icon="el-icon-upload2">导出</el-button>
                </el-col>
                <!--日历-->
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
            <!--表格-->
            <el-table :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)" border style="width: 100%;margin:10px 0;">
                <el-table-column align="center" fixed type="selection" width="55"></el-table-column>
                <el-table-column align="center" prop="status" label="资产状态" width="100">
                    <template slot-scope="scope">
                        <Status :status="scope.row.status"></Status>
                    </template>
                </el-table-column>
                <el-table-column prop="collar_number" label="维修单号"> </el-table-column>
                <el-table-column prop="collar_time" label="报修时间"></el-table-column>
                <el-table-column prop="company_name" label="报修人"> </el-table-column>
                <el-table-column prop="service" label="维修人"> </el-table-column>
                <el-table-column prop="expend" label="维修花费" width="180"></el-table-column>
                <el-table-column fixed="right" label="操作" width="100">
                    <template slot-scope="scope">
                        <el-button type="text" size="small" @click="showRegister(scope.row)">查看</el-button>
                        <el-button type="text" size="small" @click="editRegister(scope.row)">编辑</el-button>
                    </template>
                </el-table-column>
            </el-table>
            <!--分页-->
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
            <!--新增维修-->
            <el-dialog title="新增维修单" :visible.sync="addCollarDialogVisible" width="70%">
                <el-col :span="24">
                    <el-steps :active="active" finish-status="success">
                        <el-step title="报修"></el-step>
                        <el-step title="已接单"></el-step>
                        <el-step title="维修中"></el-step>
                        <el-step title="完成"></el-step>
                    </el-steps>
                </el-col>
                <el-form ref="form" :model="addCollarForm" label-width="80px">
                    <el-row>
                        <el-col :span="8">
                            <el-form-item label="维修单号" size="small"style="margin-left: -30px">
                                <el-input v-model="addCollarForm.handle_name" placeholder="单号" disabled></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="报修时间" size="small">
                                <el-date-picker
                                        v-model="addCollarForm.time"
                                        type="date"
                                        value-format="timestamp"
                                        style="width:100%;"
                                        placeholder="选择报修日期">
                                </el-date-picker>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="报修人" size="small">
                                <el-input v-model="addCollarForm.personnel_name">
                                    <el-button slot="append" icon="el-icon-user-solid" @click="selectPersonDialogVisible=true"></el-button>
                                </el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="24">
                            <el-form-item label="维修说明" size="small" style="margin-left: -30px">
                                <el-input type="textarea" v-model="addCollarForm.collar_remarks" placeholder="报修说明"></el-input>
                            </el-form-item>
                        </el-col>
                    </el-row>
                    <el-row>
                        <el-button @click="selectAssetsDialogVisible=true" size="small">选择资产</el-button>
                        <el-button type="danger" size="small">删除</el-button>
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
                    <el-button @click="addCollarDialogVisible = false" size="small">取 消</el-button>
                    <el-button type="primary" @click="fun1(addCollarForm)" size="small">确 定</el-button>
                </span>
            </el-dialog>
            <!--查看维修-->
            <el-dialog title="查看维修单" width="70%" class="show-dialog" :visible.sync="showDialogTableVisible">
                <el-col :span="24">
                    <el-steps :active="active" finish-status="success">
                        <el-step title="报修"></el-step>
                        <el-step title="已接单"></el-step>
                        <el-step title="维修中"></el-step>
                        <el-step title="完成"></el-step>
                    </el-steps>
                </el-col>
                <el-form ref="addform" :model="showRegisterData" label-width="80px">
                    <el-row>
                        <el-col :span="8">
                            <el-form-item label="维修单号" size="small" style="margin-left: -30px">
                                <el-input v-model="showRegisterData.collar_number" placeholder="单号" disabled></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="报修时间" size="small">
                                <el-date-picker
                                        v-model="showRegisterData.collar_times"
                                        type="date"
                                        value-format="timestamp"
                                        style="width:100%;"
                                        placeholder="选择报修日期"
                                disabled>
                                </el-date-picker>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="报修人" size="small">
                                <el-input v-model="showRegisterData.company_name" disabled></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="维修状态" size="small" style="margin-left: -30px">
                                <el-input v-model="showRegisterData.status_name" placeholder="已取消" disabled></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="维修人" size="small">
                                <el-input v-model="showRegisterData.service" disabled></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="维修时间" size="small">
                                <el-date-picker
                                        v-model="showRegisterData.collar_times"
                                        type="date"
                                        value-format="timestamp"
                                        style="width:100%;"
                                        placeholder="选择报修日期"
                                disabled>
                                </el-date-picker>
                            </el-form-item>
                        </el-col>
                        <el-col :span="24">
                            <el-form-item label="报修说明" size="small" style="margin-left: -30px">
                                <el-input type="textarea" v-model="showRegisterData.Repair_remarks" placeholder="报修说明" disabled></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="24">
                            <el-form-item label="维修说明" size="small" style="margin-left: -30px">
                                <el-input type="textarea" v-model="showRegisterData.servic_remarks" placeholder="报修说明" disabled></el-input>
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
                <div slot="footer" class="dialog-footer">
                    <el-button type="primary" @click="showDialogTableVisible = false">确 定</el-button>
                </div>
            </el-dialog>

            <!--编辑维修-->
            <el-dialog title="编辑维修单" width="70%" :visible.sync="editDialogTableVisible">
                <el-col :span="24">
                    <el-steps :active="active" finish-status="success">
                        <el-step title="报修"></el-step>
                        <el-step title="已接单"></el-step>
                        <el-step title="维修中"></el-step>
                        <el-step title="完成"></el-step>
                    </el-steps>
                </el-col>
                <el-form ref="addform" :model="editRegisterData" label-width="80px">
                    <el-row>
                        <el-col :span="8">
                            <el-form-item label="维修单号" size="small" style="margin-left: -30px">
                                <el-input v-model="editRegisterData.collar_number" placeholder="单号"></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="报修时间" size="small">
                                <el-date-picker
                                        v-model="editRegisterData.collar_times"
                                        type="date"
                                        value-format="timestamp"
                                        style="width:100%;"
                                        placeholder="选择报修日期"
                                >
                                </el-date-picker>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="报修人" size="small">
                                <el-input v-model="editRegisterData.company_name" ></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="维修状态" size="small" style="margin-left: -30px">
                                <el-input v-model="editRegisterData.status_name" placeholder="已取消" ></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="维修人" size="small">
                                <el-input v-model="editRegisterData.service" ></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="维修时间" size="small">
                                <el-date-picker
                                        v-model="editRegisterData.collar_times"
                                        type="date"
                                        value-format="timestamp"
                                        style="width:100%;"
                                        placeholder="选择报修日期"
                                >
                                </el-date-picker>
                            </el-form-item>
                        </el-col>
                        <el-col :span="24">
                            <el-form-item label="报修说明" size="small" style="margin-left: -30px">
                                <el-input type="textarea" v-model="editRegisterData.Repair_remarks" placeholder="报修说明"></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="24">
                            <el-form-item label="维修说明" size="small" style="margin-left: -30px">
                                <el-input type="textarea" v-model="editRegisterData.servic_remarks" placeholder="报修说明"></el-input>
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
                <div slot="footer" class="dialog-footer">
                    <el-button @click="editDialogTableVisible = false">取消</el-button>
                    <el-button type="primary" @click="editRegisterDone">确 定</el-button>
                </div>
            </el-dialog>

        </div>

    </div>
</template>

<script>
    import Status from'@/components/data/status.vue'
    import Selectuser from '@/components/Withdraw/selectuser.vue'
    import Selectedassets from '@/components/Withdraw/selectedassets.vue'
    export default {
        name: 'wxgl',
        props: {
            // msg: String
        },
        data(){
            return{
                editRegisterData:{},
                editDialogTableVisible:false,
                showRegisterData:{},
                showDialogTableVisible:false,
                active:0,
                total:100,//默认数据总数
                currentPage:1,//默认开始页面
                pageSize:10,//每页的数据条数
                searchDate:[],
                addCollarDialogVisible:false,
                selectPersonDialogVisible:false,
                addCollarForm:{
                    time:Date.now()
                },
                showCollarForm:{},
                showCollarDialogVisible:false,
                selectAssetsDialogVisible:false,
                selectedCollarAssetsData:[],
                selectCollarAssetsData:[],
                currentPage2: 1,
                sizeForm: {
                    data:''
                },
                tableData: [
                    {
                        id:1,
                        collar_number:'WB20180608001',
                        collar_time:'2018-06-18',
                        expend:'$98.00',
                        service:'里斯',
                        company_name:'张三',
                        status_name:'已取消',
                        Repair_remarks:'废了',
                        servic_remarks:'换个新的XIM Alpha',
                        collar_times:'1529254718034',
                        times:Date.now(),
                        status:9
                    },
                    {
                        id:2,
                        collar_number:'WB20180608001',
                        collar_time:'2018-06-18',
                        expend:'$98.00',
                        service:'里斯',
                        company_name:'张三',
                        status_name:'已取消',
                        Repair_remarks:'废了',
                        servic_remarks:'换个新的XIM Alpha',
                        collar_times:'1529254718034',
                        times:Date.now(),
                        status:10
                    },
                    {
                        id:3,
                        collar_number:'WB20180608001',
                        collar_time:'2018-06-18',
                        expend:'$98.00',
                        service:'里斯',
                        company_name:'张三',
                        status_name:'已取消',
                        Repair_remarks:'废了',
                        servic_remarks:'换个新的XIM Alpha',
                        collar_times:'1529254718034',
                        times:Date.now(),
                        status:11
                    },
                    {
                        id:4,
                        collar_number:'WB20180608001',
                        collar_time:'2018-06-18',
                        expend:'$98.00',
                        service:'里斯',
                        company_name:'张三',
                        status_name:'已取消',
                        Repair_remarks:'废了',
                        servic_remarks:'换个新的XIM Alpha',
                        collar_times:'1529254718034',
                        times:Date.now(),
                        status:12
                    },
                    {
                        id:5,
                        collar_number:'WB20180608001',
                        collar_time:'2018-06-18',
                        expend:'$98.00',
                        service:'里斯',
                        company_name:'张三',
                        status_name:'已取消',
                        Repair_remarks:'废了',
                        servic_remarks:'换个新的XIM Alpha',
                        collar_times:'1529254718034',
                        times:Date.now(),
                        status:13
                    },
                    {
                        id:6,
                        collar_number:'WB20180608001',
                        collar_time:'2018-06-18',
                        expend:'$98.00',
                        service:'里斯',
                        company_name:'张三',
                        status_name:'已取消',
                        Repair_remarks:'废了',
                        servic_remarks:'换个新的XIM Alpha',
                        collar_times:'1529254718034',
                        times:Date.now(),
                        status:14
                    },

                ],
            }
        },
        methods: {
            deleteRow(index, rows) {
                rows.splice(index, 1);
            },
            handleSizeChange() {
                // console.log(`每页 ${val} 条`);
            },
            handleCurrentChange(val) {
                // console.log(`当前页: ${val}`);
                this.currentPage = val;
            },
            handleSelectionDone(){
                this.selectAssetsDialogVisible = false;
                this.selectedCollarAssetsData = this.selectCollarAssetsData;
            },
            handleAddGetPerson(row){
                this.selectPersonDialogVisible = false;
                this.addCollarForm.personnel_id = row.personnel_id;
                this.addCollarForm.personnel_name = row.personnel_name;
            },
            handleClickShowCollar(data){
                this.showCollarDialogVisible = true;
                this.showCollarForm = data;
            },
            fun1(data){
                this.addCollarDialogVisible = false;
                this.tableData.push(data)
            },
            handleAvatarSuccess(){
                this.imageUrl = URL.createObjectURL(file.raw);
            },
            beforeAvatarUpload(){

            },
            showRegister(row){
                this.showDialogTableVisible = true;
                this.showRegisterData = row;
            },
            editRegisterDone(){
                this.editDialogTableVisible = false;
                //ajax 提交编辑数据 editRegisterData
                                    this.tableData[0]=this.editRegisterData;

                if(true){
                    this.$message({
                        type: 'success',
                        message: '编辑成功!'
                    });
                }else{
                    this.$message({
                        type: 'warning',
                        message: '编辑失败!'
                    });
                }

            },
            editRegister(row){
                this.editDialogTableVisible = true;
                this.editRegisterData = JSON.parse(JSON.stringify(row));
                if (this.tableData != this.tableData) {
                    this.editRegisterData=this.tableData
                }
            },
        },
        components:{
            Status,
            Selectuser,
            Selectedassets
        }

    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .wxgl-box{
        width: 100%;
        height: 100%;
    }
    .wxgl-top{
        display: block;
        height: 50px;
    }
    .el-breadcrumb{
        line-height: 50px;
    }
    .wxgl-bottom{
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
    .el-col{
        float: left;
        text-align: left!important;
    }
    .el-row{
        text-align: left!important;
    }
</style>
