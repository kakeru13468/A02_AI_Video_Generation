<template>
  <div class="mx-4 pt-16 lg:mx-32">
    <div class="grid grid-cols-12 max-h-screen grid-flow-row auto-cols-max gap-4">
      <textarea class="h-8 border col-span-10 max-h-24 resize-none"></textarea>
      <button type="button" class="border rounded-sm col-span-2">generate</button>
      <div class="p-2 col-span-3 h-full bg-indigo-400"></div>
      <video src="../../media/combined.mp4" class="w-full col-span-9 aspect-video bg-black" controls></video>
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
