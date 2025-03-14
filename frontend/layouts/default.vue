<template>
  <div class="min-h-screen bg-gray-50 flex flex-col">
    <!-- Шапка сайта -->
    <header class="bg-white shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <!-- Логотип и навигация -->
          <div class="flex items-center">
            <NuxtLink to="/" class="flex-shrink-0 flex items-center">
              <span class="text-2xl font-bold text-primary">ТурАгентство</span>
            </NuxtLink>
            <div class="hidden md:block ml-10">
              <div class="flex items-center space-x-4">
                <NuxtLink to="/" class="px-3 py-2 hover:text-primary">Главная</NuxtLink>
                <NuxtLink to="/tours" class="px-3 py-2 hover:text-primary">Туры</NuxtLink>
                <NuxtLink to="/about" class="px-3 py-2 hover:text-primary">О нас</NuxtLink>
                <NuxtLink to="/contacts" class="px-3 py-2 hover:text-primary">Контакты</NuxtLink>
              </div>
            </div>
          </div>
          
          <!-- Кнопки авторизации/личный кабинет -->
          <div class="flex items-center space-x-4">
            <!-- Неавторизованный пользователь -->
            <template v-if="!isAuthenticated">
              <NuxtLink to="/login" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-indigo-700 bg-indigo-100 hover:bg-indigo-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                Войти
              </NuxtLink>
              <NuxtLink to="/register" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                Регистрация
              </NuxtLink>
            </template>
            
            <!-- Авторизованный пользователь -->
            <div v-else class="relative ml-3">
              <div>
                <button @click="toggleUserMenu" type="button" class="flex max-w-xs items-center rounded-full bg-indigo-100 p-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2" id="user-menu-button">
                  <span class="sr-only">Открыть меню пользователя</span>
                  <span v-if="!user" class="h-8 w-8 rounded-full flex items-center justify-center text-indigo-600 font-medium">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
                    </svg>
                  </span>
                  <span v-else class="h-8 w-8 rounded-full bg-indigo-600 flex items-center justify-center text-white font-medium">
                    {{ getUserInitials }}
                  </span>
                </button>
              </div>

              <!-- Выпадающее меню пользователя -->
              <div v-if="userMenuOpen" class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="user-menu-button" tabindex="-1">
                <span class="block px-4 py-2 text-sm text-gray-700 border-b border-gray-100" v-if="user">
                  {{ user.first_name }} {{ user.last_name }}
                </span>
                <NuxtLink to="/profile" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">
                  Личный кабинет
                </NuxtLink>
                <NuxtLink to="/profile/bookings" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">
                  Мои бронирования
                </NuxtLink>
                <NuxtLink v-if="isAdmin" to="/admin" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">
                  Панель администратора
                </NuxtLink>
                <button @click="logout" class="block w-full text-left px-4 py-2 text-sm text-red-700 hover:bg-gray-100" role="menuitem">
                  Выйти
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
    
    <!-- Основной контент -->
    <main class="flex-grow">
      <slot />
    </main>
    
    <!-- Подвал сайта -->
    <footer class="bg-gray-800 text-white py-8">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <h3 class="text-xl font-semibold mb-4">ТурАгентство</h3>
            <p class="text-gray-300">Лучшие туры по всему миру. Отдых, экскурсии, приключения.</p>
          </div>
          <div>
            <h3 class="text-xl font-semibold mb-4">Контакты</h3>
            <p class="text-gray-300 mb-2">Адрес: г. Москва, ул. Примерная, 123</p>
            <p class="text-gray-300 mb-2">Телефон: +7 (999) 123-45-67</p>
            <p class="text-gray-300">Email: info@example.com</p>
          </div>
          <div>
            <h3 class="text-xl font-semibold mb-4">Подписка</h3>
            <p class="text-gray-300 mb-2">Подпишитесь на наши новости и акции</p>
            <div class="flex">
              <input type="email" placeholder="Ваш email" class="px-3 py-2 rounded-l-md text-gray-800 w-full" />
              <button class="bg-indigo-600 hover:bg-indigo-700 px-4 py-2 rounded-r-md">ОК</button>
            </div>
          </div>
        </div>
        <div class="mt-8 pt-8 border-t border-gray-700 text-center text-gray-400">
          <p>© {{ new Date().getFullYear() }} ТурАгентство. Все права защищены.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useAuthStore } from '~/store/auth';
import { storeToRefs } from 'pinia';

const authStore = useAuthStore();
const { user, isAuthenticated } = storeToRefs(authStore);

// Выпадающее меню пользователя
const userMenuOpen = ref(false);

// Администратор или нет
const isAdmin = computed(() => authStore.isAdmin);

// Получаем инициалы пользователя
const getUserInitials = computed(() => {
  if (!user.value) return '';
  const first = user.value.first_name ? user.value.first_name.charAt(0).toUpperCase() : '';
  const last = user.value.last_name ? user.value.last_name.charAt(0).toUpperCase() : '';
  return first + last;
});

// Открытие/закрытие меню пользователя
const toggleUserMenu = () => {
  userMenuOpen.value = !userMenuOpen.value;
};

// Выход из системы
const logout = () => {
  authStore.logout();
  userMenuOpen.value = false;
  // Перенаправляем на главную страницу
  navigateTo('/');
};

// Обработчик клика за пределами меню для его закрытия
const handleClickOutside = (event) => {
  const menuButton = document.getElementById('user-menu-button');
  if (userMenuOpen.value && menuButton && !menuButton.contains(event.target)) {
    userMenuOpen.value = false;
  }
};

// Добавляем и удаляем обработчик при монтировании/размонтировании компонента
onMounted(() => {
  document.addEventListener('click', handleClickOutside);
});

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
});
</script> 