<template>
  <div>
    <h1 class="text-3xl font-bold mb-6">欢迎使用牛导航</h1>
    <div class="grid grid-cols-3 gap-4">
      <router-link 
        v-for="group in navigationGroups" 
        :key="group.name"
        :to="{ name: 'Category', params: { category: group.name }}"
        class="bg-white rounded-lg shadow-md p-6 hover:shadow-xl transition-all duration-300 transform hover:scale-105 text-center"
      >
        <div class="text-xl font-semibold">{{ group.name }}</div>
        <div class="text-sm text-gray-500 mt-2">查看 {{ group.name }} 分类</div>
      </router-link>
    </div>
  </div>
</template>

<script setup>
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
</script> 