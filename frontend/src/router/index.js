import { createRouter, createWebHashHistory } from 'vue-router'
import NavigationCategory from '../components/NavigationCategory.vue'
import HomePage from '../views/HomePage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/category/:category',
    name: 'Category',
    component: NavigationCategory,
    props: true
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router 