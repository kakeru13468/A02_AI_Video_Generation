<template>
  <nav class="flex w-full flex-wrap items-center justify-between py-2 bg-neutral-50 lg:py-4">
    <div class="flex w-full flex-wrap items-center justify-between px-3">
      <nav class="w-full rounded-md" aria-label="breadcrumb">
        <ol class="list-reset ml-2 flex">
          <li>
            <a href="https://github.com/kakeru13468/A02_AI_Video_Generation" target="_blank"
              class="text-neutral-700 bg-neutral-50">Doc</a>
          </li>
          <li>
            <span class="mx-2 text-neutral-500 dark:text-neutral-200">/</span>
          </li>
          <li>
            <a href="#" class="text-neutral-700 bg-neutral-50">about</a>
          </li>
        </ol>
      </nav>
    </div>
  </nav>
  <div class="container gap-4 mx-auto pt-12">
    <div class="grid grid-cols-12 gap-1 ">
      <textarea class="flex-wrap sm:col-span-12 md:col-span-10 lg:col-span-10 h-8 border max-h-24 resize-none area-lg"
        v-model="prompt"></textarea>
      <!-- ,generateVideo(promptData) -->
      <button type="button"
        class="transition-all hover:scale-105 active:scale-95 bg-blue-500 hover:bg-blue-700 text-white font-bold px-2 sm:col-span-12 md:col-span-2 lg:col-span-2 rounded-full "
        @click="generateVideo(prompt), getPrompt()">generate</button>
      <!-- generateVideo(promptData) -->

      <div
        class="lg:col-start-1 lg:col-end-4 lg:row-start-2 lg:row-end-7 w-full h-full p-4 bg-indigo-400 rounded overflow-hidden shadow-lg">
        Parameter
      </div>

      <!-- <div
        class="sm:col-span-12 md:col-start-1 md:col-end-6 lg:col-start-1 lg:col-end-4 mt-4 w-full p-4 bg-teal-500 rounded overflow-hidden shadow-lg relative">
        Script
        <div class="flex justify-between items-start">
          <button type="button"
            class="absolute top-4 right-1 bg-blue-500 hover:bg-blue-700 text-white font-bold px-2 rounded-full">copy</button>
        </div>
      </div> -->

      <div class="sm:col-span-12 md:col-start-6 md:col-end-13 md:row-start-2 md:row-end-4 lg:col-start-4 lg:col-end-13">
        <video :src="videoSrc" class="w-full col-span-full md:col-span-9 rounded aspect-video bg-black" controls></video>
        <div class="mt-4 mx-4 flex ">
          <span id="videoName" class="mr-3 py-1 px-2">My Video</span>
          <button
            class="transition-all hover:scale-105 active:scale-95 bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center">
            <svg class="fill-current w-4 h-4 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
              <path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z" />
            </svg>
            <span>Download</span>
          </button>
          <div class="px-4">
            <ScriptBotton text="Script place" color="blue" @click="showed = true" />
          </div>
        </div>
      </div>
    </div>
  </div>

  <ScriptContent title="Script" :showModal="showed" @closing="showed = false">
    <template v-slot:LeftItemText>
      {{ prompt }}
    </template>
    <template v-slot:RightItemText>
      Script: {{ scriptData }}<br>
      Prompt: {{ promptData }}
    </template>
  </ScriptContent>


  <footer class="p-4 bg-neutral-50 text-center lg:text-left">
    <div class="p-4 text-center text-neutral-700 bg-neutral-50">
      © 2023 Copyright : A02 Project
    </div>
  </footer>
  <!-- <div class="container gap-4 mx-auto pt-16">
    <div class="grid grid-cols-12 max-h-screen grid-flow-row auto-cols-max gap-1 lg:gap-2">
      <textarea v-model="prompt" class="h-8 border col-span-8 md:col-span-10 max-h-24 resize-none area-lg"  placeholder="prompt"></textarea>
      <button @click="generateVideo(prompt)" type="button" class="bg-blue-500 hover:bg-blue-700 text-white font-bold px-2 col-span-4 md:col-span-2 rounded-full ">generate</button>
      <div class="md:col-span-3 col-span-full w-full p-4 h-full bg-indigo-400 rounded overflow-hidden shadow-lg"></div>
      <video :src="videoSrc" class="w-full col-span-full md:col-span-9 rounded aspect-video bg-black" controls></video>
    </div>
  </div> -->
</template>

<script>
import ScriptBotton from './components/ScriptBotton.vue'
import ScriptContent from './components/ScriptContent.vue'
import scriptJson from '../static/script.json'
import promptJson from '../static/prompt.json'
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      videoName: '',
      showed: false,
      prompt: '',
      scriptData: '',
      promptData: '',
    }
  },
  computed: {
    videoSrc() {
      return 'http://' + window.location.hostname + ':3000/videos/' + this.videoName;
    }
  },
  components: {
    ScriptBotton,
    ScriptContent,
  },
  methods: {
    getPrompt() {
      this.prompt

    },
    generateVideo(prompt) {
      axios.post('/api/generate', {}, { params: { prompt: prompt, dry_run: 'yeah' } })
        .then(response => {
          this.videoName = response.data;
          this.scriptData = scriptJson;
          this.promptData = promptJson;
        })
        .catch(error => {
          console.log(error)
        })
    },
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