import Vue from 'vue'
import Router from 'vue-router'
// import Home from './views/Home.vue'
import Login from './views/login/login.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',//mode history代表，路由不再显示hash
  base: process.env.BASE_URL,//代表着是基本的路由请求的路径。
  routes: [
    // {
    //   path: '/',
    //   name: 'home',
    //   component: Home
    // },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    // }
    {
      path:'/',
      // name:'login',
      // component:Login,
      redirect:'/login'
    },
    {
      path:'/login',
      name:'login',
      component:Login
    },
    {
      path:'/index',
      name:'index',
      component: () => import('./views/index/Index.vue'),
      children:[
        {
          path:"dashboard",
          name:"Dashboard",
          component:()=>import('./views/ybp/Ybp.vue'),
        },
        {
          path:"register",
          name:"Register",
          component:()=>import('./views/zcdj/zcdj.vue'),
        },
        {
          path:"collar",
          name:"Collar",
          component:()=>import('./views/lytk/lytk.vue'),
        },
        {
          path:"borrow",
          name:"Borrow",
          component:()=>import('./views/jygh/jygh.vue'),
        },
        {
          path:"modify",
          name:"Modify",
          component:()=>import('./views/xxxg/Information.vue'),

        },
        {
          path:"repair",
          name:"Repair",
          component:()=>import('./views/wxgl/wxgl.vue'),
        },
        {
          path:"scrap",
          name:"Scrap",
          component:()=>import('./views/bfgl/Bfgl.vue'),
        },
        {
          path: "census",
          name: "Census",
          // redirect:'scrap',
          component: () => import('./views/zctj/Zctj.vue'),
          children: [
            {
              path: "bill",
              name: "Bill",
              component: () => import('./views/zcqd/Zcqd.vue'),
            },
          ]
        },
      ]
    }
  ]
})
