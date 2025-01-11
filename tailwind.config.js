/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'text': '#050315',
        'background': '#ffffff',
        'primary': '#3298d8',
        'secondary': '#8c80e9',
        'accent': '#5642f0',
      }
    }
  },
  plugins: [],
}

