<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
    <div class="bg-white rounded-lg shadow-xl w-[500px] p-6">
      <h2 class="text-2xl font-bold mb-6 text-center">添加自定义网址</h2>
      
      <div class="mb-4">
        <label class="block mb-2">网站名称</label>
        <input 
          v-model="name" 
          placeholder="请输入网站名称" 
          class="w-full p-3 border rounded"
        />
      </div>
      
      <div class="mb-4">
        <label class="block mb-2">网站地址</label>
        <input 
          v-model="url" 
          placeholder="请输入完整的网址，如 https://example.com" 
          class="w-full p-3 border rounded"
        />
      </div>
      
      <div class="mb-4">
        <label class="block mb-2">选择分类</label>
        <select 
          v-model="category" 
          class="w-full p-3 border rounded"
        >
          <option 
            v-for="group in navigationGroups" 
            :key="group.name" 
            :value="group.name"
          >
            {{ group.name }}
          </option>
        </select>
      </div>

      <div class="mb-6">
        <label class="block mb-2">网站描述</label>
        <textarea 
          v-model="description" 
          placeholder="简单描述这个网站（可选）" 
          class="w-full p-3 border rounded h-24"
        ></textarea>
      </div>
      
      <div class="flex justify-center space-x-4">
        <button 
          @click="$emit('close')" 
          class="px-6 py-3 bg-gray-200 rounded hover:bg-gray-300"
        >
          取消
        </button>
        <button 
          @click="submitUrl" 
          class="px-6 py-3 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          确认添加
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const name = ref('')
const url = ref('')
const category = ref('日常使用')
const description = ref('')

const navigationGroups = [
  { name: '日常使用' },
  { name: 'AI' },
  { name: '有趣生活' },
  // ... 其他分类
]

const emit = defineEmits(['close', 'add-url'])

const submitUrl = () => {
  if (name.value && url.value) {
    emit('add-url', {
      name: name.value,
      url: url.value,
      category: category.value,
      description: description.value
    })
  }
}
</script> 