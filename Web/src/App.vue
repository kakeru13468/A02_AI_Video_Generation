<template>
  <div class="container gap-4 mx-auto pt-16">
    <div class="grid grid-cols-12 max-h-screen grid-flow-row auto-cols-max gap-1 lg:gap-2">
      <textarea v-model="prompt" class="h-8 border col-span-8 md:col-span-10 max-h-24 resize-none area-lg"  placeholder="prompt"></textarea>
      <button @click="generateVideo(prompt)" type="button" class="bg-blue-500 hover:bg-blue-700 text-white font-bold px-2 col-span-4 md:col-span-2 rounded-full ">generate</button>
      <!--<div class="p-2 col-span-3 h-full bg-indigo-400"></div>-->
      <div class="md:col-span-3 col-span-full w-full p-4 h-full bg-indigo-400 rounded overflow-hidden shadow-lg"></div>
      <video :src="videoSrc" class="w-full col-span-full md:col-span-9 rounded aspect-video bg-black" controls></video>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      videoName: '',
      prompt: ''
    }
  },
  computed: {
    videoSrc() {
      return 'http://localhost:3000/videos/' + this.videoName;
    }
  },
  components: {
  },
  methods: {
    generateVideo(prompt) {
      axios.post('/api/generate', {}, { params: { prompt: prompt, dry_run: 'yeah' } })
        .then(response => {
          this.videoName =  response.data;
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
