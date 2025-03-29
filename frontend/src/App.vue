<template>
  <div class="flex h-screen">
    <!-- 左侧侧边栏 -->
    <div class="w-64 bg-gray-900 text-white p-4">
      <div class="flex items-center mb-6">
        <img src="/path/to/logo.png" alt="牛导航" class="w-12 h-12 mr-3">
        <h1 class="text-2xl font-bold">牛导航</h1>
      </div>
      
      <nav>
        <router-link 
          v-for="(group, index) in navigationGroups" 
          :key="index"
          :to="{ name: 'Category', params: { category: group.name }}"
          class="block mb-2 cursor-pointer p-2 rounded hover:bg-gray-700"
          active-class="bg-blue-600"
        >
          {{ group.name }}
        </router-link>
      </nav>
    </div>

    <!-- 右侧内容区 -->
    <div class="flex-1 bg-gray-100 overflow-y-auto">
      <!-- 顶部导航栏 -->
      <div class="bg-white shadow-md p-4 flex justify-between items-center">
        <div class="flex items-center">
          <input 
            type="text" 
            placeholder="搜索网址" 
            class="w-96 p-2 border rounded mr-4"
          />
          <button class="bg-blue-500 text-white px-4 py-2 rounded">搜索</button>
        </div>
        
        <div class="flex items-center">
          <router-link 
            to="/"
            class="mr-4 text-blue-500 hover:underline"
          >
            首页
          </router-link>
          <button 
            @click="showAddModal = true"
            class="bg-blue-500 text-white px-4 py-2 rounded mr-4"
          >
            + 添加网址
          </button>
          <div>用户头像/登录</div>
        </div>
      </div>

      <!-- 内容区 -->
      <div class="p-6">
        <router-view v-slot="{ Component }">
          <keep-alive>
            <component :is="Component" />
          </keep-alive>
        </router-view>
      </div>
    </div>

    <AddUrlModal 
      v-if="showAddModal" 
      @close="showAddModal = false"
      @add-url="addUrl"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import AddUrlModal from './components/AddUrlModal.vue'
import axios from 'axios'

const urls = ref([])
const showAddModal = ref(false)

const navigationGroups = [
  { name: '日常使用' },
  { name: 'AI' },
  { name: '有趣生活' },
  { name: '搜索引擎' },
  { name: '影音娱乐' },
  { name: '新闻期刊' },
  { name: '生活必备' },
  { name: '电子书集' },
  { name: '论文学术' },
  { name: '素材资源' },
  { name: '学习提升' },
  { name: '软件应用' },
  { name: '新媒体π' },
  { name: '教师教学' }
]

const addUrl = async (urlData) => {
  try {
    await axios.post('http://localhost:5000/add_url', urlData)
    await fetchUrls()
    showAddModal.value = false
  } catch (error) {
    console.error('添加失败', error)
  }
}

const fetchUrls = async () => {
  try {
    const response = await axios.get('http://localhost:5000/get_urls')
    urls.value = response.data
  } catch (error) {
    console.error('获取URLs失败', error)
  }
}

onMounted(fetchUrls)
</script> 