<template>
    <div :class="[
        'fixed top-0 left-0',
        'w-screen h-screen',
        'p-5',
        'flex justify-center items-center',
        showed2 ? 'opacity-100' : 'opacity-0 pointer-events-none',
        'transition-all duration-300',
        'overwrite-hidden',
        'overflow-auto'
    ]">
        <div class="absolute top-0 left-0 w-full h-full bg-black/50" @click="closing()" />

        <div :class="[
            'w-full max-w-sm bg-white rounded-md overflow-hidden z-10',
            showed2 ? 'scale-100' : 'scale-0',
            'transition-all duration-300',
            'overflow-auto'
        ]">
            <div class="border-b-2 p-3 flex justify-between items-center">
                <div class="font-bold text-gray-700">
                    {{ title }}
                </div>
                <div class="h-7 w-7 p-1 hover:bg-gray-200 active:scale-90 rounded-md cursor-pointer transition-all"
                    @click="closing()">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-full w-full" fill="none" viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </div>
            </div>

            <div class="flex flex-col p-4 gap-4">
                <div class="flex h-1/2">
                    <div class="bg-gray-300 py-2 px-4 rounded-tl-xl rounded-br-xl">
                        <slot name="Text">place</slot>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "StepContent",
    props: {
        showModal2: {},
        title: {
            default: "error"
        }
    },
    data() {
        return {
            showed2: false,
        }
    },
    mounted() {
        this.showed2 = this.showModal2
    },
    watch: {
        showModal2(newVal) {
            this.showed2 = newVal
        }
    },
    methods: {
        closing() {
            this.showed2 = false
            this.$emit("closing")
        }
    }
}
</script>