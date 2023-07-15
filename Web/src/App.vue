<template>
  <div class="gap-4 mx-4 pt-16 lg:mx-32">
    <div class="grid grid-cols-12 max-h-screen grid-flow-row auto-cols-max gap-1 lg:gap-2">
      <textarea class="h-8 border col-span-8 md:col-span-10 max-h-24 resize-none area-lg"  placeholder="prompt"></textarea>
      <button type="button" class="bg-blue-500 hover:bg-blue-700 text-white font-bold px-2 col-span-4 md:col-span-2 rounded-full ">generate</button>
      <!--<div class="p-2 col-span-3 h-full bg-indigo-400"></div>-->
      <div class="col-span-3 h-full bg-indigo-400 max-w-sm rounded overflow-hidden shadow-lg"></div>
      <video class="w-full col-span-9 aspect-video bg-black" controls></video>
      <video class="w-full col-span-9 rounded aspect-video bg-black" controls></video>
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
