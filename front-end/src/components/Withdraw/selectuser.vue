<template>
    <el-row :gutter="0">
        <!--        左面-->
        <el-col :span="5">
            <el-tree :data="data" :props="defaultProps" @node-click="handleNodeClick"></el-tree>
        </el-col>
        <!--        右面表格-->
        <el-col :span="18" :offset="1">
            <el-table :data="persons" border style="width: 100%;" height="300" size="small">
                <el-table-column width="50">
                    <template slot-scope="scope" >
                        <el-button @click="handleSelectPerson(scope.row)" type="text" >选择</el-button>
                    </template>
                </el-table-column>
                <el-table-column prop="personnel_number" label="员工工号" width="100"> </el-table-column>
                <el-table-column prop="personnel_name" label="员工姓名" width="100"> </el-table-column>
                <el-table-column prop="company_name" label="所属公司" width="150"></el-table-column>
                <el-table-column prop="department_name" label="所属部门" width="100"> </el-table-column>
                <el-table-column prop="email" label="邮箱" width="160"> </el-table-column>
                <el-table-column prop="phone" label="手机" width="140"> </el-table-column>
            </el-table>
        </el-col>
    </el-row>
</template>
<script>
    export default {
        data(){
            return {
                persons:[
                    {
                        personnel_id:1,
                        personnel_number:1001,
                        personnel_name:"张三",
                        company_id:1,
                        company_name:"康佳",
                        dep_id:1,
                        department_name:"研发部",
                        email:"zhangsan@qq.com",
                        phone:13800002222
                    },
                    {
                        personnel_id:2,
                        personnel_number:1002,
                        personnel_name:"李四",
                        company_id:1,
                        company_name:"康佳",
                        dep_id:2,
                        department_name:"人事部",
                        email:"lisi@qq.com",
                        phone:13800002233
                    }
                ],
                data:[{
                    label: '康佳',
                    children: [{
                        label: '研发部',
                    },
                        {label:'人事部'},
                        {label:'财务部'}]
                }, {label: '康宁',}],
                defaultProps: {
                    children: 'children',
                    label: 'label'
                }
            }
        },
        props:{
            handleAddGetPerson:{
                type:Function,
                default:function(){}
            }
        },
        methods:{
            handleNodeClick(data) {
                console.log(data);
            },
            handleSelectPerson:function(row){
                this.handleAddGetPerson(row);
            },
        }
    }
</script>
<style>

</style>



