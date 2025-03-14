<template>
  <div class="min-h-screen bg-gray-100">
    <div class="py-10">
      <header>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 class="text-3xl font-bold leading-tight text-gray-900">Панель администратора</h1>
        </div>
      </header>
      <main>
        <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
          <div class="px-4 py-8 sm:px-0">
            <div v-if="!isAdmin" class="bg-red-50 border-l-4 border-red-400 p-4 mb-8">
              <div class="flex">
                <div class="flex-shrink-0">
                  <svg class="h-5 w-5 text-red-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                    <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                </div>
                <div class="ml-3">
                  <p class="text-sm text-red-700">
                    У вас нет доступа к этой странице. Только администраторы могут видеть данный раздел.
                  </p>
                </div>
              </div>
            </div>
            
            <div v-else class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
              <!-- Пользователи -->
              <div class="bg-white overflow-hidden shadow rounded-lg">
                <div class="p-5">
                  <div class="flex items-center">
                    <div class="flex-shrink-0 bg-indigo-500 rounded-md p-3">
                      <svg class="h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
                      </svg>
                    </div>
                    <div class="ml-5 w-0 flex-1">
                      <dt class="text-sm font-medium text-gray-500 truncate">
                        Пользователи
                      </dt>
                      <dd class="flex items-baseline">
                        <div class="text-2xl font-semibold text-gray-900">
                          {{ stats.users || 0 }}
                        </div>
                      </dd>
                    </div>
                  </div>
                </div>
                <div class="bg-gray-50 px-5 py-3">
                  <div class="text-sm">
                    <NuxtLink to="/admin/users" class="font-medium text-indigo-600 hover:text-indigo-500">
                      Управление пользователями <span aria-hidden="true">&rarr;</span>
                    </NuxtLink>
                  </div>
                </div>
              </div>
              
              <!-- Туры -->
              <div class="bg-white overflow-hidden shadow rounded-lg">
                <div class="p-5">
                  <div class="flex items-center">
                    <div class="flex-shrink-0 bg-green-500 rounded-md p-3">
                      <svg class="h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                    </div>
                    <div class="ml-5 w-0 flex-1">
                      <dt class="text-sm font-medium text-gray-500 truncate">
                        Туры
                      </dt>
                      <dd class="flex items-baseline">
                        <div class="text-2xl font-semibold text-gray-900">
                          {{ stats.tours || 0 }}
                        </div>
                      </dd>
                    </div>
                  </div>
                </div>
                <div class="bg-gray-50 px-5 py-3">
                  <div class="text-sm">
                    <NuxtLink to="/admin/tours" class="font-medium text-indigo-600 hover:text-indigo-500">
                      Управление турами <span aria-hidden="true">&rarr;</span>
                    </NuxtLink>
                  </div>
                </div>
              </div>
              
              <!-- Бронирования -->
              <div class="bg-white overflow-hidden shadow rounded-lg">
                <div class="p-5">
                  <div class="flex items-center">
                    <div class="flex-shrink-0 bg-yellow-500 rounded-md p-3">
                      <svg class="h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                      </svg>
                    </div>
                    <div class="ml-5 w-0 flex-1">
                      <dt class="text-sm font-medium text-gray-500 truncate">
                        Бронирования
                      </dt>
                      <dd class="flex items-baseline">
                        <div class="text-2xl font-semibold text-gray-900">
                          {{ stats.bookings || 0 }}
                        </div>
                        <div v-if="stats.pendingBookings > 0" class="ml-2">
                          <span class="inline-flex items-baseline px-2.5 py-0.5 rounded-full text-sm font-medium bg-yellow-100 text-yellow-800">
                            {{ stats.pendingBookings }} ожидают
                          </span>
                        </div>
                      </dd>
                    </div>
                  </div>
                </div>
                <div class="bg-gray-50 px-5 py-3">
                  <div class="text-sm">
                    <NuxtLink to="/admin/bookings" class="font-medium text-indigo-600 hover:text-indigo-500">
                      Управление бронированиями <span aria-hidden="true">&rarr;</span>
                    </NuxtLink>
                  </div>
                </div>
              </div>
              
              <!-- Отзывы -->
              <div class="bg-white overflow-hidden shadow rounded-lg">
                <div class="p-5">
                  <div class="flex items-center">
                    <div class="flex-shrink-0 bg-purple-500 rounded-md p-3">
                      <svg class="h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                      </svg>
                    </div>
                    <div class="ml-5 w-0 flex-1">
                      <dt class="text-sm font-medium text-gray-500 truncate">
                        Отзывы
                      </dt>
                      <dd class="flex items-baseline">
                        <div class="text-2xl font-semibold text-gray-900">
                          {{ stats.reviews || 0 }}
                        </div>
                      </dd>
                    </div>
                  </div>
                </div>
                <div class="bg-gray-50 px-5 py-3">
                  <div class="text-sm">
                    <NuxtLink to="/admin/reviews" class="font-medium text-indigo-600 hover:text-indigo-500">
                      Управление отзывами <span aria-hidden="true">&rarr;</span>
                    </NuxtLink>
                  </div>
                </div>
              </div>
              
              <!-- Последняя активность -->
              <div class="bg-white overflow-hidden shadow rounded-lg sm:col-span-2">
                <div class="px-5 py-4 border-b border-gray-200">
                  <h3 class="text-lg leading-6 font-medium text-gray-900">Последние действия</h3>
                </div>
                <div class="px-5 py-5">
                  <div class="flow-root">
                    <ul role="list" class="-mb-8">
                      <li v-for="(activity, index) in recentActivity" :key="index">
                        <div class="relative pb-8">
                          <span v-if="index !== recentActivity.length - 1" class="absolute top-5 left-5 -ml-px h-full w-0.5 bg-gray-200" aria-hidden="true"></span>
                          <div class="relative flex items-start space-x-3">
                            <div class="relative">
                              <div :class="getActivityTypeClass(activity.type)">
                                <svg v-if="activity.type === 'user'" class="h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                </svg>
                                <svg v-else-if="activity.type === 'tour'" class="h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                                <svg v-else-if="activity.type === 'booking'" class="h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                </svg>
                                <svg v-else class="h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                                </svg>
                              </div>
                            </div>
                            <div class="min-w-0 flex-1">
                              <div>
                                <div class="text-sm">
                                  <span class="font-medium text-gray-900">{{ activity.title }}</span>
                                </div>
                                <p class="mt-0.5 text-sm text-gray-500">
                                  {{ activity.description }}
                                </p>
                              </div>
                              <div class="mt-2 text-sm text-gray-500">
                                <p>{{ formatDate(activity.date) }}</p>
                              </div>
                            </div>
                          </div>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useAuthStore } from '~/store/auth';
import { storeToRefs } from 'pinia';

const authStore = useAuthStore();
const { user, loading } = storeToRefs(authStore);
const isAdmin = computed(() => authStore.isAdmin);

const router = useRouter();

// Статистика
const stats = ref({
  users: 0,
  tours: 0,
  bookings: 0,
  pendingBookings: 0,
  reviews: 0
});

// Последние действия
const recentActivity = ref([
  // Примеры действий
  {
    type: 'user',
    title: 'Новая регистрация',
    description: 'Иван Петров зарегистрировался в системе',
    date: new Date(Date.now() - 1000 * 60 * 60) // час назад
  },
  {
    type: 'booking',
    title: 'Новое бронирование',
    description: 'Анна Смирнова забронировала тур "Отдых в Греции"',
    date: new Date(Date.now() - 1000 * 60 * 60 * 3) // 3 часа назад
  },
  {
    type: 'tour',
    title: 'Новый тур добавлен',
    description: 'Добавлен новый тур "Путешествие по Алтаю"',
    date: new Date(Date.now() - 1000 * 60 * 60 * 24) // день назад
  },
  {
    type: 'review',
    title: 'Новый отзыв',
    description: 'Михаил Иванов оставил отзыв о туре "Выходные в Стамбуле"',
    date: new Date(Date.now() - 1000 * 60 * 60 * 36) // 1.5 дня назад
  }
]);

// Получение статистики
const fetchStats = async () => {
  try {
    const response = await fetch(`${useRuntimeConfig().public.apiBase}/admin/stats`, {
      headers: {
        'Authorization': `Bearer ${authStore.token}`
      }
    });
    
    if (!response.ok) {
      throw new Error('Ошибка при получении статистики');
    }
    
    stats.value = await response.json();
  } catch (error) {
    console.error('Ошибка при получении статистики:', error);
  }
};

// Получение последних действий
const fetchRecentActivity = async () => {
  try {
    const response = await fetch(`${useRuntimeConfig().public.apiBase}/admin/activity`, {
      headers: {
        'Authorization': `Bearer ${authStore.token}`
      }
    });
    
    if (!response.ok) {
      // Если API еще не реализован, оставляем примеры
      return;
    }
    
    recentActivity.value = await response.json();
  } catch (error) {
    console.error('Ошибка при получении последних действий:', error);
  }
};

// Вспомогательные функции
const formatDate = (date) => {
  if (!date) return '';
  if (typeof date === 'string') {
    date = new Date(date);
  }
  return date.toLocaleString('ru-RU');
};

const getActivityTypeClass = (type) => {
  const classes = {
    'user': 'h-10 w-10 rounded-full flex items-center justify-center bg-indigo-500',
    'tour': 'h-10 w-10 rounded-full flex items-center justify-center bg-green-500',
    'booking': 'h-10 w-10 rounded-full flex items-center justify-center bg-yellow-500',
    'review': 'h-10 w-10 rounded-full flex items-center justify-center bg-purple-500'
  };
  
  return classes[type] || classes['user'];
};

onMounted(async () => {
  if (!authStore.isAuthenticated) {
    return router.push('/login');
  }
  
  if (isAdmin.value) {
    await fetchStats();
    await fetchRecentActivity();
  }
});
</script> 