<template>
    <div class="change-box">

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
            <el-table-column fixed type="selection" width="55"></el-table-column>
            <el-table-column prop="collar_number" label="变更单号" width="160"></el-table-column>
            <el-table-column prop="collar_time" label="变更时间" width="120"></el-table-column>
            <el-table-column prop="personnel_name" label="资产名称" width="140"></el-table-column>
            <el-table-column prop="Supplier" label="供应商" width="140"></el-table-column>
            <el-table-column prop="company_name" label="联系人" width="140"></el-table-column>
            <el-table-column prop="phone" label="联系方式" width="140"></el-table-column>
            <el-table-column prop="maturity" label="维保到期时间" width="120"></el-table-column>
            <el-table-column prop="department_name" label="资产类型" width="160"></el-table-column>
            <el-table-column prop="company_name" label="使用人" width="100"></el-table-column>
            <el-table-column prop="company" label="使用公司" width="100"></el-table-column>
            <el-table-column prop="company_department" label="使用部门" width="100"></el-table-column>
            <el-table-column prop="user" label="管理员" width="120"></el-table-column>
            <el-table-column fixed="right" label="操作" width="100">
                <template slot-scope="scope">
                    <el-button @click="handleClickShowCollar(scope.row)" type="text" >查看</el-button>
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

        <!-- 新增基本信息 -->
        <el-dialog title="变更单" :visible.sync="addCollarDialogVisible" width="70%">

            <el-form ref="form" :model="addCollarForm" label-width="80px">
                <el-row>
                    <el-col :span="12">
                        <el-form-item label="变更单号" size="small">
                            <el-input v-model="addCollarForm.modify_number" disabled></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="12">
                        <el-form-item label="处理时间" size="small">
                            <el-date-picker
                                    v-model="addCollarForm.time"
                                    type="date"
                                    format="yyyy 年 MM 月 dd 日"
                                    value-format="timestamp"
                                    style="width:100%;"
                                    placeholder="选择领用日期">
                            </el-date-picker>
                        </el-form-item>
                    </el-col>
                </el-row>

            </el-form>
            <el-form ref="editform" :model="addCollarForm" label-width="80px">
                <el-row>
                    <el-col :span="8">
                        <el-form-item label="资产名称" size="small">
                            <el-input v-model="addCollarForm.name" placeholder="资产名称" size="small">
                                <el-button slot="append" type="primary" icon="el-icon-office-building" @click="selectAssetsDialogVisible=true" size="small"></el-button>
                            </el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="8">
                        <el-form-item label="供应商" size="small">
                            <el-input v-model="addCollarForm.specification" placeholder="供应商"></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="8">
                        <el-form-item label="联系人" size="small">
                            <el-input v-model="addCollarForm.specification" placeholder="联系人"></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="8" class="sn-box">
                        <el-form-item label="联系方式" size="small">
                            <el-input v-model="addCollarForm.sn" placeholder="联系方式"></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="8">
                        <el-form-item label="到期时间" size="small">
                            <el-date-picker
                                    v-model="addCollarForm.time"
                                    type="date"
                                    format="yyyy 年 MM 月 dd 日"
                                    value-format="timestamp"
                                    style="width:100%;"
                                    placeholder="选择领用日期">
                            </el-date-picker>
                        </el-form-item>
                    </el-col>
                    <el-col :span="24">
                        <el-form-item label="备注">
                            <el-input type="textarea" v-model="addCollarForm.remarks" placeholder="备注"></el-input>
                        </el-form-item>
                    </el-col>

                </el-row>
            </el-form>
            <!-- 选择资产弹窗 -->
            <el-dialog
                    title="选择资产"
                    :visible.sync="selectAssetsDialogVisible"
                    width="70%"
                    append-to-body>
                <Selectedassets></Selectedassets>
                <span slot="footer" class="dialog-footer">
                <el-button  @click="selectAssetsDialogVisible = false">取 消</el-button>
                <el-button  type="primary" @click="handleSelectionDone">确 定</el-button>
            </span>
            </el-dialog>

            <span slot="footer" class="dialog-footer">
                <el-button @click="addCollarDialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="fun1(addCollarForm)">确 定</el-button>
            </span>
        </el-dialog>

        <!-- 查看基本信息 -->
        <el-dialog
                title="变更单"
                :visible.sync="showCollarDialogVisible"
                width="70%">
            <el-form ref="form" :model="showCollarForm" label-width="80px">
                <el-row>
                    <el-col :span="12">
                        <el-form-item label="变更单号" size="small">
                            <el-input v-model="showCollarForm.collar_number" disabled></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="12">
                        <el-form-item label="处理时间" size="small">
                            <el-date-picker
                                    v-model="showCollarForm.collar_times"
                                    type="date"
                                    format="yyyy 年 MM 月 dd 日"
                                    value-format="timestamp"
                                    style="width:100%;"
                                    placeholder="选择领用日期">
                            </el-date-picker>
                        </el-form-item>
                    </el-col>
                </el-row>

            </el-form>
            <el-form ref="editform" :model="showCollarForm" label-width="80px">
                <el-row>
                    <el-col :span="8">
                        <el-form-item label="资产名称" size="small">
                            <el-input v-model="showCollarForm.personnel_name" placeholder="资产名称" size="small">
                                <el-button slot="append" type="primary" icon="el-icon-office-building" @click="selectAssetsDialogVisible=true" size="small"></el-button>
                            </el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="8">
                        <el-form-item label="供应商" size="small">
                            <el-input v-model="showCollarForm.Supplier" placeholder="供应商"></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="8">
                        <el-form-item label="联系人" size="small">
                            <el-input v-model="showCollarForm.company_name" placeholder="联系人"></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="8" class="sn-box">
                        <el-form-item label="联系方式" size="small">
                            <el-input v-model="showCollarForm.phone" placeholder="联系方式"></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="8">
                        <el-form-item label="到期时间" size="small">
                            <el-date-picker
                                    v-model="showCollarForm.times"
                                    type="date"
                                    format="yyyy 年 MM 月 dd 日"
                                    value-format="timestamp"
                                    style="width:100%;"
                                    placeholder="选择日期">
                            </el-date-picker>
                        </el-form-item>
                    </el-col>
                    <el-col :span="24">
                        <el-form-item label="备注">
                            <el-input type="textarea" v-model="showCollarForm.remarks" placeholder="备注"></el-input>
                        </el-form-item>
                    </el-col>

                </el-row>
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
        name: 'withdraws',
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
                        personnel_name:'打印机',
                        department_name:'电气设备',
                        company_name:'张三',
                        phone:'12345678909',
                        maturity:'2019-10-02',
                        Supplier:'康宁',
                        user:'allcky',
                        company:'优逸客',
                        company_department:'UAIF1907',//规格型号，SN号，计量单位，存放地点，使用期限，来源，备注
                        // model:'无规格',
                        // sn:'7777777',
                        // unit:'台',
                        // location:'出门右拐顶到头',
                        // age:'2年',
                        // source:'偷的',
                        remarks:'好好非常好',
                        collar_times:'1529254718034',
                        times:Date.now(),
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
        float: left;
        text-align: left!important;
    }
    .el-row{
        text-align: left!important;
    }
    .sn-box{
        margin-left: 33%;
    }

</style>
