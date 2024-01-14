import { createRouter, createWebHistory } from "vue-router";

import Home from './components/Home.vue'
import Create from './components/Create.vue'
import ArticleDetails from './components/ArticleDetails.vue'
import ArticleEdit from './components/ArticleEdit.vue'

const routes = [
    {
        path:'/',
        name:'home',
        component:Home
    },
    {
        path:'/create',
        name:'create',
        component:Create
    },
    {
        path:'/details/:id',
        name:'details',
        component:ArticleDetails,
        props:true
    },
    {
        path:'/edit/:id',
        name:'edit',
        component:ArticleEdit,
        props:true
    }
]

const router = createRouter({
    history:createWebHistory(),
    routes,
})


export default router;