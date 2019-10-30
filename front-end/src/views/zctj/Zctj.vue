<template>

    <router-view></router-view>

</template>

<script>
export default {
    name: 'Zctj',
    props: {
    // msg: String
    },
    data() {
        return {
          activeName: 'second'
        };
    },
    methods: {
        handleClick(tab, event) {
          console.log(tab, event);
        }
    }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
