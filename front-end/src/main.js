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

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
