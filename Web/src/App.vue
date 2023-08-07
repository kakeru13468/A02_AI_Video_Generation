<template>
  <nav class="flex w-full flex-wrap items-center justify-between py-2 bg-neutral-50 lg:py-4">
    <div class="flex w-full flex-wrap items-center justify-between px-3">
      <nav class="w-full rounded-md" aria-label="breadcrumb">
        <ol class="list-reset ml-2 flex">
          <li>
            <a href="https://github.com/kakeru13468/A02_AI_Video_Generation" target="_blank" class="text-neutral-700 bg-neutral-50">Doc</a>
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
        placeholder="prompt" v-model="promptData" onkeydown="if(event.keyCode==13)return false;"
        @keyup.enter.prevent="getPrompt()"></textarea>
      <button type="button"
        class="transition-all hover:scale-105 active:scale-95 bg-blue-500 hover:bg-blue-700 text-white font-bold px-2 sm:col-span-12 md:col-span-2 lg:col-span-2 rounded-full "
        @click="getPrompt()">generate</button>

      <div
        class="sm:col-span-12 md:col-start-1 md:col-end-6 lg:col-start-1 lg:col-end-4 w-full p-4 bg-indigo-400 rounded overflow-hidden shadow-lg">
        Parameter
      </div>

      <div
        class="sm:col-span-12 md:col-start-1 md:col-end-6 lg:col-start-1 lg:col-end-4 mt-4 w-full p-4 bg-teal-500 rounded overflow-hidden shadow-lg relative">
        Script
        <div class="flex justify-between items-start">
          <button type="button"
            class="absolute top-4 right-1 bg-blue-500 hover:bg-blue-700 text-white font-bold px-2 rounded-full">copy</button>
        </div>
      </div>

      <div class="sm:col-span-12 md:col-start-6 md:col-end-13 md:row-start-2 md:row-end-4 lg:col-start-4 lg:col-end-13">
        <video class="w-full col-span-full rounded aspect-video bg-black" controls></video>
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

  <div :class="[
    'w-screen h-screen',
    'p-5',
    'flex flex-col items-center gap-2'
  ]">
    <ScriptContent title="Script" :showModal="showed" @closing="showed = false">
      <template v-slot:LeftItemText>
        {{promptData}}
      </template>
      <template v-slot:RightItemText>
        return GPT Script
      </template>
    </ScriptContent>

  </div>

  <footer class="p-4 bg-neutral-50 text-center lg:text-left">
    <div class="p-4 text-center text-neutral-700 bg-neutral-50">
      © 2023 Copyright : A02 Project
    </div>
  </footer>
</template>

<script>
import ScriptBotton from './components/ScriptBotton.vue'
import ScriptContent from './components/ScriptContent.vue'
export default {
  name: 'App',
  data() {
    return {
      promptData: '',
      showed: false,
    }
  },
  components: {
    ScriptBotton,
    ScriptContent,
  },
  methods: {
    getPrompt() {
      this.promptData
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