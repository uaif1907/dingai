<template>
    <el-row :gutter="0">
        <!--        左面-->
        <el-col :span="5">
            <el-tree :data="data" :props="defaultProps" @node-click="handleNodeClick"></el-tree>
        </el-col>
        <!--        右面表格-->
        <el-col :span="18" :offset="1">
            <el-table :data="persons" border style="width: 100%;" height="300" size="small">
                <el-table-column type="selection" width="55"></el-table-column>
                <el-table-column prop="bar_code" label="资产条码" width="140"> </el-table-column>
                <el-table-column prop="name" label="资产名称" width="150"> </el-table-column>
                <el-table-column prop="type_id" label="资产类型" width="150"> </el-table-column>
                <el-table-column prop="company" label="使用公司" width="100"> </el-table-column>
                <el-table-column prop="department" label="使用部门" width="100"> </el-table-column>
                <el-table-column prop="user_id" label="使用人" width="100"> </el-table-column>
                <el-table-column prop="manager_id" label="管理员" width="100"> </el-table-column>
                <el-table-column prop="address" label="存放地点" width="100"> </el-table-column>
            </el-table>
        </el-col>
    </el-row>
</template>
<script>
    export default {
        data(){
            return {
                persons:[

                ],
                data:[{
                    label: '土地、房屋及构筑物',
                }, {label: '电器设备',}],
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
        }
    }
</script>
<style>

</style>



