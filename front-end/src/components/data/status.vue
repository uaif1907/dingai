<template>
    <div class="assets-status" :style="{backgroundColor:assetsStatus[status].color}">
        {{assetsStatus[status].label}}
    </div>
</template>
<script>
export default {
    data(){
        return {
            assetsStatus:{
                0:{label:"闲置",color:"#67C23A"},
                1:{label:"在用",color:"#409EFF"},
                2:{label:"借用",color:"#1898D1"},
                3:{label:"维修中",color:"#E6A23C"},
                4:{label:"报废",color:"#F56C6C"},
                5:{label:"已归还",color:"#67C23A"},
                6:{label:"已调出",color:"#7465EA"},
                8:{label:"已完成",color:"#67C23A"},
                9:{label:"已取消",color:"#E6A23C"},
                10:{label:"已报修",color:"#409EFF"},
                11:{label:"已接单",color:"#1898D1"},
                12:{label:"维修中",color:"#E6A23C"},
                13:{label:"维修成功",color:"#67C23A"},
                14:{label:"维修失败",color:"#F56C6C"},
            }
        }
    },
    props:{
        status:{
            required:true,
            type:Number,
            default:0
        }
    }
}
</script>
<style>
.assets-status{
    line-height: 24px;
    font-size: 12px;
    color: #fff;
    padding:0 10px;
    display: inline-block;
    border-radius: 12px;
}
</style>


