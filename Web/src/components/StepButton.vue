<template>
    <div :class="[
        'btn-style',
        'flex gap-2',
        'px-10 py-2',
        'rounded-md font-bold',
        'text-white',
        colorSelector,
        'hover:scale-105 active:scale-95',
        'transition-all',
        'cursor-pointer',
        'text-center'
    ]">

        <div>
            <div class="text-black">{{ title }}<br></div>
            <div class="text-black">{{ text }}<br></div>
            <div class="text-red-700">{{ note }}</div>

        </div>

    </div>
</template>
  
<script>
export default {
    name: "StepBotton",
    props: {
        title: {},
        text: {

        },
        note: {},
        color: {
            default: "gray"
        },
    },
    computed: {
        colorSelector() {
            return {
                gray: 'bg-gray-400 hover:bg-gray-300 active:bg-gray-500',
                green: 'bg-green-400 hover:bg-green-300 active:bg-green-500',
                blue: 'bg-blue-500 hover:bg-blue-700 active:bg-blue-500',
                red: 'bg-red-400 hover:bg-red-300 active:bg-red-500',
                yellow: 'bg-yellow-400 hover:bg-yellow-300 active:bg-yellow-500',
                white: 'bg-white hover:bg-gray-300 active:bg-gray-500'
            }[this.color]
        }
    }
}
</script>

<style>
.btn-style {
    width: 230px;
    height: 500px;
}
</style>