<template>
    <div class="bfgl-box">
        <div class="bfgl-top">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item :to="{ path: '/index' }">主页</el-breadcrumb-item>
                <el-breadcrumb-item><a href="">资产登记</a></el-breadcrumb-item>
            </el-breadcrumb>
        </div>

        <div class="bfgl-bottom">
            <el-tabs v-model="activeName" @tab-click="handleClick">

                <el-row>
                    <!--按钮-->
                    <el-col :span="12">
                        <el-button type="primary" size="small" icon="el-icon-plus" @click="addCollarDialogVisible = true">新增</el-button>
                        <el-button type="warning"  size="small" icon="el-icon-plus" @click="restore">还原</el-button>
                        <el-button size="small" icon="el-icon-printer">打印</el-button>
                        <el-button size="small" icon="el-icon-daochu">导出</el-button>
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
                <!-- 表格-->
                <el-table :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)" border style="width: 100%;margin:10px 0;"  @selection-change="handleSelectionChange">
                    <el-table-column fixed type="selection" width="55"></el-table-column>
                    <el-table-column prop="scrap_number" label="报废单号"></el-table-column>
                    <el-table-column prop="scrap_time" label="报修时间">
                        <template slot-scope="scope">
                            {{scope.row.scrap_time | moment}}
                        </template>
                    </el-table-column>
                    <el-table-column prop="scrap_handle_name" label="处理人"></el-table-column>
                    <el-table-column prop="scrap_remarks" label="说明" style="white-space:nowrap;" :show-overflow-tooltip="true"></el-table-column>
                    <el-table-column fixed="right" label="操作" width="100">
                        <template slot-scope="scope">
                            <el-button @click="handleClickShowCollar(scope.row)" type="text">查看</el-button>
                        </template>
                    </el-table-column>
                </el-table>
                <!-- 分页-->
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
                <!-- 新增报废 -->
                <el-dialog title="新增报废单" :visible.sync="addCollarDialogVisible" width="70%">
                    <el-form ref="form" :model="addCollarForm" label-width="80px">
                        <el-row>
                            <el-col :span="8">
                                <el-form-item label="报废单号" size="small">
                                    <el-input v-model="addCollarForm.scrap_number" placeholder="报废单号"></el-input>
                                </el-form-item>
                            </el-col>
                            <el-col :span="8">
                                <el-form-item label="报废时间" size="small">
                                    <el-date-picker
                                            v-model="addCollarForm.scrap_time"
                                            type="date"
                                            value-format="timestamp"
                                            style="width:100%;"
                                            placeholder="选择报废时间">
                                    </el-date-picker>
                                </el-form-item>
                            </el-col>
                            <el-col :span="8">
                                <el-form-item label="处理人" size="small">
                                    <el-input v-model="addCollarForm.scrap_handle_name" placeholder="处理人"></el-input>
                                </el-form-item>
                            </el-col>
                            <el-col :span="24">
                                <el-form-item label="说明" size="small">
                                    <el-input type="textarea" v-model="addCollarForm.scrap_remarks" placeholder="领用备注"></el-input>
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
                <el-button type="primary" @click="fun1(addCollarForm)">确 定</el-button>
            </span>
                </el-dialog>
                <!-- 查看报废 -->
                <el-dialog title="领用单" :visible.sync="showCollarDialogVisible" width="70%">
                    <el-form ref="form" :model="showCollarForm" disabled label-width="80px" class="show-collar-form">
                        <el-row>
                            <el-col :span="8">
                                <el-form-item label="报废单号" size="small">
                                    <el-input v-model="showCollarForm.scrap_number" placeholder="报废单号"></el-input>
                                </el-form-item>
                            </el-col>
                            <el-col :span="8">
                                <el-form-item label="报废时间" size="small">
                                    <el-date-picker
                                            v-model="showCollarForm.scrap_time"
                                            type="date"
                                            value-format="timestamp"
                                            style="width:100%;"
                                            placeholder="选择报废时间">
                                    </el-date-picker>
                                </el-form-item>
                            </el-col>
                            <el-col :span="8">
                                <el-form-item label="处理人" size="small">
                                    <el-input v-model="showCollarForm.scrap_handle_name" placeholder="处理人"></el-input>
                                </el-form-item>
                            </el-col>
                            <el-col :span="24">
                                <el-form-item label="说明" size="small">
                                    <el-input type="textarea" v-model="showCollarForm.scrap_remarks" placeholder="领用备注"></el-input>
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

            </el-tabs>
        </div>
    </div>
</template>

<script>
    import Selectuser from '@/components/Withdraw/selectuser.vue'
    import Selectedassets from '@/components/Withdraw/selectedassets.vue'
    export default {
        name: 'Zcdj',
        props: {
            // msg: String
        },
        data() {
            return {
                activeName: 'second',
                total:100,//默认数据总数
                currentPage:1,//默认开始页面
                pageSize:10,//每页的数据条数
                searchDate:[],
                addCollarDialogVisible:false,//添加弹窗
                selectPersonDialogVisible:false,
                addCollarForm:{time:Date.now()},//添加
                showCollarForm:{},
                showCollarDialogVisible:false,
                selectAssetsDialogVisible:false,
                selectedCollarAssetsData:[],
                selectCollarAssetsData:[],
                scrapIds:[],//报废列表
                currentPage2: 1,
                sizeForm: {
                    data:''
                },
                tableData: [
                    {
                        scrap_id:1,
                        scrap_number:"BF20180823004",
                        scrap_time:"2018-09-01 11:11:11",
                        scrap_handle_name:"李四",
                        scrap_handle_id:1,
                        scrap_remarks:"腐蚀严重无法修复或继续使用要发生危险！腐蚀严重无法修复或继续使用要发生危险！腐蚀严重无法修复或继续使用要发生危险！"
                    },
                ],
            };
        },
        methods: {
            handleClick(tab, event) {
                console.log(tab, event);
            },
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
            //还原
            restore:function(){
                if(this.scrapIds.length==0){
                    this.$message('请选中要还原的数据条目！');
                    return;
                }
                this.$confirm('此操作将还原该数据, 是否继续?', '资产还原确认提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    //要还原的资产
                    if(true){
                        this.$message({
                            type: 'success',
                            message: '还原成功!'
                        });
                        //获取最新 报废单列表
                        this.tableData = []
                    }else{
                        this.$message({
                            type: 'warning',
                            message: '还原失败!'
                        });
                    }

                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消还原'
                    });
                });
            },
            //选择报废单
            handleSelectionChange:function(val){
                //获取选中的删除条目ID
                this.scrapIds = val.map((val)=>{
                    return val.scrap_number
                })
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
    .bfgl-box{
        width: 100%;
        height: 100%;
    }
    .bfgl-top{
        display: block;
        height: 50px;
    }
    .el-breadcrumb{
        line-height: 50px;
    }
    .bfgl-bottom{
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
