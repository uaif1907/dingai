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
                    <el-button size="small" icon="el-icon-printer" >打印</el-button>
                    <el-button size="small" icon="el-icon-upload2" @click="date">导出</el-button>
                </el-col>
                <!--日历-->
                <el-col :span="12">
                    <el-button size="small" icon="el-icon-search" style="margin-left:10px;float:right;" @click="Search"></el-button>
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
                <el-table-column align="center" prop="status" label="资产状态" width="100" >
                    <template slot-scope="scope">
                        <Status :status="scope.row.status"  ></Status>
                    </template>
                </el-table-column>
                <el-table-column prop="prop" label="资产" > </el-table-column>
                <el-table-column prop="time1" label="报修时间"></el-table-column>
                <el-table-column prop="name" label="报修人"> </el-table-column>
                <el-table-column prop="explain" label="报修说明" v-model="data1"> </el-table-column>
                <el-table-column prop="time2" label="维修时间"></el-table-column>
                <el-table-column prop="people" label="维修人"> </el-table-column>
                <el-table-column prop="explain2" label="维修说明" > </el-table-column>
                <el-table-column prop="price" label="维修花费" width="180"></el-table-column>
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
                        :total="this.tableData.length"
                        background>
                </el-pagination>
                <!--:total="total"-->
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
                            <el-form-item label="维修单号" size="small" style="margin-left: -30px">
                                <el-input v-model="addCollarForm.handle_name" placeholder="单号" disabled></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="报修时间" size="small">
                                <el-date-picker
                                        v-model="addCollarForm.time"
                                        type="date"
                                        style="width:100%;"
                                        placeholder="选择报修日期">
                                </el-date-picker>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="报修人" size="small">
                                <el-input v-model="addCollarForm.personnel_name" disabled>
                                    <el-button slot="append" icon="el-icon-user-solid" @click="selectPersonDialogVisible=true"></el-button>
                                </el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label=" 选择资产" size="small" style="margin-left: -30px">
                                <template>
                                  <el-select v-model="value" placeholder="请选择">
                                    <el-option
                                      v-for="item in options"
                                      :key="item.value"
                                      :label="item.label"
                                      :value="item.value">
                                    </el-option>
                                  </el-select>
                                </template>
                            </el-form-item>
                        </el-col>
                        <el-col :span="24">
                            <el-form-item label="维修说明" size="small" style="margin-left: -30px">
                                <el-input type="textarea" v-model="addCollarForm.collar_remarks" placeholder="报修说明"></el-input>
                            </el-form-item>
                        </el-col>
                    </el-row>
                    <!--<el-row>-->
                        <!--<el-button @click="selectAssetsDialogVisible=true" size="small">选择资产</el-button>-->

                        <!--<el-button type="danger" size="small">删除</el-button>-->
                    <!--</el-row>-->
                    <!--<el-table :data="selectCollarAssetsData" border style="width: 100%;margin:10px 0;">-->
                        <!--<el-table-column fixed type="selection" width="55"></el-table-column>-->
                        <!--<el-table-column prop="bar_code" label="资产条码" width="140"> </el-table-column>-->
                        <!--<el-table-column prop="name" label="资产名称" width="150"> </el-table-column>-->
                        <!--<el-table-column prop="type_id" label="资产类型" width="150"> </el-table-column>-->
                        <!--<el-table-column prop="company" label="使用公司" width="100"> </el-table-column>-->
                        <!--<el-table-column prop="department" label="使用部门" width="100"> </el-table-column>-->
                        <!--<el-table-column prop="user_id" label="使用人" width="100"> </el-table-column>-->
                        <!--<el-table-column prop="manager_id" label="管理员" width="100"> </el-table-column>-->
                        <!--<el-table-column prop="address" label="存放地点" width="100"> </el-table-column>-->
                    <!--</el-table>-->
                </el-form>
                <!-- 选择领用人 -->
                <el-dialog title="选择用户" :visible.sync="selectPersonDialogVisible" width="70%" append-to-body>
                    <Selectuser :handleAddGetPerson="handleAddGetPerson"></Selectuser>
                    <span slot="footer" class="dialog-footer">
                    <el-button @click="selectPersonDialogVisible = false">取 消</el-button>
                </span>
                </el-dialog>
                <!-- 选择资产弹窗 -->
                <!--<el-dialog title="选择资产" :visible.sync="selectAssetsDialogVisible" width="70%" append-to-body>-->
                    <!--<Selectedassets></Selectedassets>-->
                    <!--<span slot="footer" class="dialog-footer">-->
                    <!--<el-button @click="selectAssetsDialogVisible = false">取 消</el-button>-->
                    <!--<el-button type="primary" @click="handleSelectionDone">确 定</el-button>-->
                <!--</span>-->
                <!--</el-dialog>-->
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
                                <el-input v-model="showRegisterData.num" placeholder="单号" disabled></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="报修时间" size="small">
                                <el-date-picker
                                        v-model="showRegisterData.time1"
                                        type="date"
                                        style="width:100%;"
                                        placeholder="选择报修日期"
                                disabled>
                                </el-date-picker>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="报修人" size="small">
                                <el-input v-model="showRegisterData.name" disabled></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="维修状态" size="small" style="margin-left: -30px">
                                <el-input v-model="showRegisterData.status" placeholder="已取消" disabled></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="维修人" size="small">
                                <el-input v-model="showRegisterData.people" disabled></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="维修时间" size="small">
                                <el-date-picker
                                        v-model="showRegisterData.time2"
                                        type="date"
                                        style="width:100%;"
                                        placeholder="选择报修日期"
                                disabled>
                                </el-date-picker>
                            </el-form-item>
                        </el-col>
                        <el-col :span="24">
                            <el-form-item label="报修说明" size="small" style="margin-left: -30px">
                                <el-input type="textarea" v-model="showRegisterData.explain2" placeholder="报修说明" disabled></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="24">
                            <el-form-item label="维修说明" size="small" style="margin-left: -30px">
                                <el-input type="textarea" v-model="showRegisterData.explain" placeholder="维修说明" disabled></el-input>
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
                    <el-button type="danger" @click="del(showRegisterData)">删除</el-button>
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
                                <el-input v-model="editRegisterData.num" placeholder="单号" disabled></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="报修时间" size="small">
                                <el-date-picker
                                        v-model="editRegisterData.time1"
                                        type="date"
                                        style="width:100%;"
                                        placeholder="选择报修日期"
                                >
                                </el-date-picker>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="报修人" size="small">
                                <el-input v-model="editRegisterData.name" disabled></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="维修状态" size="small" style="margin-left: -30px">
                                <el-input v-model="editRegisterData.status" placeholder="已取消" disabled></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="维修人" size="small">
                                <el-input v-model="editRegisterData.people" ></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="维修时间" size="small">
                                <el-date-picker
                                        v-model="editRegisterData.time2"
                                        type="date"
                                        style="width:100%;"
                                        placeholder="选择维修日期"
                                >
                                </el-date-picker>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="价钱" size="small" style="margin-left: -30px">
                                <el-input type="text" v-model="editRegisterData.price" placeholder="价钱"></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="24">
                            <el-form-item label="报修说明" size="small" style="margin-left: -30px">
                                <el-input type="textarea" v-model="editRegisterData.explain" placeholder="报修说明"></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="24">
                            <el-form-item label="维修说明" size="small" style="margin-left: -30px">
                                <el-input type="textarea" v-model="editRegisterData.explain2" placeholder="报修说明"></el-input>
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
                    <el-button type="primary" @click="editRegisterDone(editRegisterData)">确 定</el-button>
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
        mounted(){
            this.find();

            },
        name: 'wxgl',
        props: {
            // msg: String
        },
        updated(){
            for(let i=0;i<this.tableData.length;i++)
            {
                this.tableData[i]['time1']=this.tableData[i]['time1'].split(' ')[0];
                this.tableData[i]['time2']=this.tableData[i]['time2'].split(' ')[0]

            }

        },
         methods: {
            //挂载前将后台数据加载到前台
            find(){
            this.$axios.get("/api/maintain").then(res=>{
            this.tableData=res.data.data;
            this.options = res.data.prop;
            });
            },
             Search(){
                this.tableMi=this.tableData;
                if(this.sizeForm.date!=undefined) {
                    let date = this.sizeForm.date;
                    let LIST = [];
                    let date1 = new Date(date[0]).toLocaleDateString();
                    let date2 = new Date(date[1]).toLocaleDateString();
                    LIST.push(date1);
                    LIST.push(date2);
                    for(let i=0;i<this.tableData.length;i++)
                    {
                        if(parseInt(this.tableData[i].time2.split('-')[0])>=parseInt(date2.split('/')[0]&parseInt(this.tableData[i].time1.split('-')[0])<=parseInt(date1.split('/')[0])))
                        {
                            if(parseInt(this.tableData[i].time2.split('-')[1])>=parseInt(date2.split('/')[1]&parseInt(this.tableData[i].time1.split('-')[1])<=parseInt(date1.split('/')[1]))) {
                                if(parseInt(this.tableData[i].time2.split('-')[2])>=parseInt(date2.split('/')[2]&parseInt(this.tableData[i].time1.split('-')[2])<=parseInt(date1.split('/')[2]))) {
                                    this.tableMi2 = this.tableData.splice(i);
                                    this.tableData='';
                                    this.tableData=this.tableMi2;
                                }
                            }
                        }
                    }
                }
                else{
                    this.tableData=this.tableMi;
                }

             },
            date(){
                // console.log(this.sizeForm.data)
            },
            deleteRow(index, rows) {
                rows.splice(index, 1);
            },
            handleSizeChange() {
                // console.log(`每页 ${val} 条`);
            },
            handleCurrentChange(val) {
                // console.log(`当前页: ${val}`);
                // console.log(this.data1);
                this.currentPage = val;
            },
            handleSelectionDone(){
                this.selectAssetsDialogVisible = false;
                this.selectedCollarAssetsData = this.selectCollarAssetsData;
            },
            handleAddGetPerson(row){
                this.selectPersonDialogVisible = false;
                this.addCollarForm.personnel_id = row.id;
                this.addCollarForm.personnel_name = row.name;
                this.ddd=row
            },
            handleClickShowCollar(data){
                this.showCollarDialogVisible = true;
                this.showCollarForm = data;
            },
             del(data){
                data['edit']=2;
                this.$axios.post(
                       "/api/maintain",data
                ).then(res=>{
                    data='';
                    this.showDialogTableVisible=false;
                   this.$message({
                      message: '删除成功',
                      type: 'success',
                  });
                this.$axios.get(
                       "/api/maintain"
                ).then(res=>{
                 this.$axios.get("/api/maintain").then(res=>{
                this.tableData=res.data.data;

                 });

                })

                }).catch(res=>{
                    this.showDialogTableVisible=false;
                   this.$message({
                      message: '删除失败',
                      type: 'failed',
                  });
                });
             },
            fun1(data){
                this.addCollarDialogVisible = false;
                data['edit']=0;
                data['property']=this.value;

                data['pop']=this.ddd;
                this.$axios.post(
                       "/api/maintain",data
                ).then(res=>{
                    data='';
                this.$axios.get(
                       "/api/maintain"
                ).then(res=>{
                 this.$axios.get("/api/maintain").then(res=>{
                this.tableData=res.data.data;

                 });

                });

                this.addCollarForm={};
                    this.addCollarForm['handle_name']='WX'+Date.parse(new Date())
                });
            },
            handleAvatarSuccess(){
                this.imageUrl = URL.createObjectURL(file.raw);
            },
            beforeAvatarUpload(){

            },
            showRegister(row){
                this.showDialogTableVisible = true;
                this.showRegisterData = row;
                // console.log('点击行数',row)
            },
            editRegisterDone(row){
                this.editDialogTableVisible = false;
                //ajax 提交编辑数据 editRegisterData
                this.editRegisterData['edit'] = 1;
                this.$axios.post(
                       "/api/maintain",this.editRegisterData
                ).then(res=>{
                this.$axios.get(
                       "/api/maintain"
                ).then(res=>{
                 this.$axios.get("/api/maintain").then(res=>{
                this.tableData=res.data.data;

            });
                })
                });

                this.editRegisterData=row;

                if(true)
                {
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
        data(){
            return{
                //资产选择
                options: [
                ],
                value: '',
                property:'',
                data1:'',
                editRegisterData:{},
                editDialogTableVisible:false,
                showRegisterData:{},
                showDialogTableVisible:false,
                active:0,
                total:100,//默认数据总数
                currentPage:1,//默认开始页面
                pageSize:10,//每页的数据条数
                searchDate:[],
                ddd:'',
                addCollarDialogVisible:false,
                selectPersonDialogVisible:false,
                addCollarForm:{
                    handle_name:'WX'+Date.parse(new Date()),
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
                ],
                tableMi:[],
                tableMi2:[],

            }
        },

        components:{
            Status,
            Selectuser,
            Selectedassets
        },



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
