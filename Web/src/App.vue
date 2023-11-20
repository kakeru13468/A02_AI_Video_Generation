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

      <!-- <div
        class="lg:col-start-1 lg:col-end-4 lg:row-start-2 lg:row-end-7 w-full h-full p-4 bg-indigo-400 rounded overflow-hidden shadow-lg">
        Parameter
      </div> -->
      <div
        class="lg:col-start-1 lg:col-end-4 lg:row-start-2 lg:row-end-7 w-full h-full p-4 bg-indigo-400 rounded overflow-hidden shadow-lg">

        <!--video type-->
        <div class="pt-4">
          Vdeo type
        </div>
        <!--select-->
        <div class="relative  w-full min-w-[200px]">
          <select ref="videoTypeSelect"
            class="peer h-full w-full rounded-[7px] border border-blue-gray-200 border-t-transparent bg-transparent px-3 py-2.5 font-sans text-sm font-normal text-blue-gray-700 outline outline-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 empty:!bg-red-500 disabled:border-0 disabled:bg-blue-gray-50">
            <option class="text-gray-400" value="" disabled selected>select...</option>
            <option value="happy">Happy</option>
            <option value="horror">Horror</option>
            <option value="romance">Romance</option>
          </select>
          <label
            class="before:content[' '] after:content[' '] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none text-[11px] font-normal leading-tight text-blue-gray-400 transition-all before:pointer-events-none before:mt-[6.5px] before:mr-1 before:box-border before:block before:h-1.5 before:w-2.5 before:rounded-tl-md before:border-t before:border-l before:border-blue-gray-200 before:transition-all after:pointer-events-none after:mt-[6.5px] after:ml-1 after:box-border after:block after:h-1.5 after:w-2.5 after:flex-grow after:rounded-tr-md after:border-t after:border-r after:border-blue-gray-200 after:transition-all peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[3.75] peer-placeholder-shown:text-blue-gray-500 peer-placeholder-shown:before:border-transparent peer-placeholder-shown:after:border-transparent peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-pink-500 peer-focus:before:border-t-2 peer-disabled:text-transparent peer-disabled:before:border-transparent peer-disabled:after:border-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500">
            Select video type
          </label>
        </div>
        <div class="pt-4">
          Voice style
        </div>
        <div class="relative  w-full min-w-[200px]">
          <select ref="voiceTypeSelect"
            class="peer h-full w-full rounded-[7px] border border-blue-gray-200 border-t-transparent bg-transparent px-3 py-2.5 font-sans text-sm font-normal text-blue-gray-700 outline outline-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 empty:!bg-red-500 disabled:border-0 disabled:bg-blue-gray-50">
            <option class="text-gray-400" value="" disabled selected>select...</option>
            <option value="0">0</option>
            <option value="0.5">0.5</option>
            <option value="1">1</option>
            <option value="1.5">1.5</option>
            <option value="2">2</option>
            <option value="2.5">2.5</option>
            <option value="3">3</option>
          </select>
          <label
            class="before:content[' '] after:content[' '] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none text-[11px] font-normal leading-tight text-blue-gray-400 transition-all before:pointer-events-none before:mt-[6.5px] before:mr-1 before:box-border before:block before:h-1.5 before:w-2.5 before:rounded-tl-md before:border-t before:border-l before:border-blue-gray-200 before:transition-all after:pointer-events-none after:mt-[6.5px] after:ml-1 after:box-border after:block after:h-1.5 after:w-2.5 after:flex-grow after:rounded-tr-md after:border-t after:border-r after:border-blue-gray-200 after:transition-all peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[3.75] peer-placeholder-shown:text-blue-gray-500 peer-placeholder-shown:before:border-transparent peer-placeholder-shown:after:border-transparent peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-pink-500 peer-focus:before:border-t-2 peer-disabled:text-transparent peer-disabled:before:border-transparent peer-disabled:after:border-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500">
            Select voice type
          </label>
        </div>
      </div>
      <div class="sm:col-span-12 md:col-start-6 md:col-end-13 md:row-start-2 md:row-end-4 lg:col-start-4 lg:col-end-13">
        <video v-if="videoName !== ''" :src=videoSrc
          class="w-full col-span-full md:col-span-9 rounded aspect-video bg-black" controls></video>
        <div v-else-if="isGenerating"
          class=" w-full col-span-full md:col-span-9 rounded aspect-video bg-black progress-container">
          <div class="progress">
            <div class="color">
              Generate
            </div>
          </div>
        </div>
        <div v-else class=" w-full col-span-full md:col-span-9 rounded aspect-video bg-indigo-400">
          <div class="pt-4">
            Generate step <br>
            1. Input your text <br>
            2. Choise video type and voice type <br>
            3. Click generate button <br>
            4. Generate!!!
          </div>
        </div>
        <div class=" mt-4 mx-4 flex ">
          <span id=" videoName" class="mr-3 py-1 px-2">My Video</span>
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
      <div v-for="text in texts" :key="text">
        Script: {{ text.script }}<br>
        <!-- Prompt: {{ text.prompt }} -->
      </div>
    </template>
  </ScriptContent>


  <footer class="p-4 bg-neutral-50 text-center lg:text-left">
    <div class="p-4 text-center text-neutral-700 bg-neutral-50">
      © 2023 Copyright : A02 Project
    </div>
  </footer>
</template>

<script>
import ScriptBotton from './components/ScriptBotton.vue'
import ScriptContent from './components/ScriptContent.vue'
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
      texts: '',
      isGenerating: false,
    }
  },
  computed: {
    videoSrc() {
      if (this.videoName == '') {
        return console.log('no video');
      } else {
        return 'http://' + window.location.hostname + ':3000/videos/' + this.videoName;
      }

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
      this.isGenerating = true;
      const videoType = this.$refs.videoTypeSelect.value;
      const voiceType = this.$refs.voiceTypeSelect.value;
      const combinedPrompt = prompt + ', prompt and script type: ' + videoType;
      axios.post('/api/generate', {}, { params: { prompt: combinedPrompt, dry_run: 'yeah', voiceType } })
        .then(response => {
          this.videoName = response.data.videoPath;
          this.texts = response.data.texts;
          this.isGenerating = false;
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

.progress-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 90%;
}

.progress {
  position: relative;
  height: 40px;
  width: 30%;
  border: 11px solid #f4a261;
  border-radius: 65px;
}

.progress .color {
  position: absolute;
  background-color: #ffffff;
  top: 30;
  width: 30px;
  height: 20px;
  border-radius: 45px;
  animation: progres 4s infinite linear;
}

@keyframes progres {
  0% {
    width: 0%;
  }

  25% {
    width: 50%;
  }

  50% {
    width: 75%;
  }

  75% {
    width: 85%;
  }

  100% {
    width: 100%;
  }
}
</style>