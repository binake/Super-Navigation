<template>
  <div>
    <h2 class="text-2xl font-bold mb-6">{{ category }}</h2>
    <div class="grid grid-cols-5 gap-4">
      <div 
        v-for="url in filteredUrls" 
        :key="url.id"
        @click="openUrl(url.url)"
        class="bg-white rounded-lg shadow-md p-4 cursor-pointer hover:shadow-xl transition-all duration-300 transform hover:scale-105 flex flex-col items-center"
      >
        <div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mb-3">
          <span class="text-blue-600 font-bold">{{ url.name[0] }}</span>
        </div>
        <div class="text-sm font-medium text-center mb-1 truncate w-full">
          {{ url.name }}
        </div>
        <div class="text-xs text-gray-500 text-center truncate w-full">
          {{ url.description }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

const props = defineProps({
  category: {
    type: String,
    required: true
  }
})

const urls = ref([])

const filteredUrls = computed(() => 
  urls.value.filter(url => url.category === props.category)
)

const openUrl = (url) => {
  window.open(url, '_blank')
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