/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
],
  theme: {
    screens:{
      'sm': '390px',
      'md': '640px',
      'lg': '768px',
      'xl': '1024px',
    },
  },
  plugins: [],
}
