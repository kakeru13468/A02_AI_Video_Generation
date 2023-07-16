<template>
  <div class="container gap-4 mx-auto pt-16">
    <div class="grid grid-cols-12 max-h-screen grid-flow-row auto-cols-max gap-1 lg:gap-2">
      <textarea class="h-8 border col-span-8 md:col-span-10 max-h-24 resize-none area-lg"  placeholder="prompt"></textarea>
      <button type="button" class="bg-blue-500 hover:bg-blue-700 text-white font-bold px-2 col-span-4 md:col-span-2 rounded-full ">generate</button>
      <!--<div class="p-2 col-span-3 h-full bg-indigo-400"></div>-->
      <div class="md:col-span-3 col-span-full w-full p-4 h-full bg-indigo-400 rounded overflow-hidden shadow-lg"></div>
      <div class="md:col-span-9">
        <video class="w-full col-span-full rounded aspect-video bg-black" controls></video>
        <div class="mt-4">
          <input class="appearance-none bg-transparent border-none text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" placeholder="Video name" aria-label="Full name" disabled="disabled">
          <button class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center">
            <svg class="fill-current w-4 h-4 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z"/></svg>
            <span>Download</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  }
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
