/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#0056b3',
          light: '#4285f4',
          dark: '#003d82',
        },
        secondary: {
          DEFAULT: '#34a853',
          light: '#5cbb73',
          dark: '#237537',
        },
        accent: {
          DEFAULT: '#fbbc05',
          light: '#fcd050',
          dark: '#d9a003',
        },
        danger: {
          DEFAULT: '#ea4335',
          light: '#f0685d',
          dark: '#bd2c20',
        },
      },
      fontFamily: {
        sans: ['Inter', 'Roboto', 'sans-serif'],
        display: ['Montserrat', 'sans-serif'],
      },
    },
  },
  plugins: [],
} 