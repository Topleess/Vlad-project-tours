// https://nuxt.com/docs/api/configuration/nuxt-config
export default {
  devtools: { enabled: true },

  // Модули Nuxt
  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt',
  ],

  // Настройки приложения
  app: {
    head: {
      title: 'Туристическое агентство',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { hid: 'description', name: 'description', content: 'Веб-приложение для туристического агентства. Поиск и бронирование туров.' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ]
    }
  },

  // Настройка серверного API
  runtimeConfig: {
    public: {
      apiBase: process.env.API_BASE_URL || 'https://jsonplaceholder.typicode.com'
    }
  },

  // Настройки Tailwind CSS
  tailwindcss: {
    cssPath: '~/assets/css/tailwind.css',
    configPath: 'tailwind.config.js'
  },

  // Отключаем строгую проверку совместимости для defu
  experimental: {
    componentIslands: true
  },

  // Отключение некоторых предупреждений
  typescript: {
    strict: false,
    shim: false
  },
  
  // Поддержка JSON-импортов
  build: {
    transpile: ['defu']
  },

  // Настройка Pinia
  pinia: {
    autoImports: ['defineStore', 'storeToRefs']
  },

  // Автоматические импорты
  imports: {
    dirs: ['store']
  }
}