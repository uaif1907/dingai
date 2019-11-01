import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import moment from 'moment/moment'
import VCharts from 'v-charts'

Vue.use(ElementUI);
Vue.use(VCharts);
Vue.config.productionTip = false;
Vue.filter('moment', function (value, formatString) {
    formatString = formatString || 'YYYY-MM-DD';
    return moment(value).format(formatString); // value可以是普通日期 20170723
    //return moment.unix(value).format(formatString); // 这是时间戳转时间
});
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

Vue.prototype.$axios = axios
// 添加请求拦截器
axios.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
    config.headers["Authorization"]="JWT "+localStorage.token
    return config;
  }, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
  });





//全局路由守卫
router.beforeEach((to, from, next)=>{
    if(to.matched.length>0){
        // 路由地址正确
        //判断是否需要登录才能进入   路由对象中 requeredsAuth true
        // for(let i of to.matched){
        //     console.log(i.meta.requiresAuth)
        // }

        if(to.matched.some(obj=>{
            if(obj.meta.requiresAuth){
                return true
            }
        })){
            if(localStorage.token){
                next()
            }else{
                next({path:'/login'})
            }
        }else{
            next()
        }

    }else{
        // 路由地址不正确
        next({path:'/login'})
    }
})

new Vue({
  router,
    axios,
  render: h => h(App)
}).$mount('#app')
