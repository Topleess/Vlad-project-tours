<template>
  <div class="min-h-screen bg-gray-100">
    <div class="py-10">
      <header>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 class="text-3xl font-bold leading-tight text-gray-900">Личный кабинет</h1>
        </div>
      </header>
      <main>
        <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
          <div class="px-4 py-8 sm:px-0">
            <!-- Loading indicator -->
            <div v-if="loading" class="flex justify-center items-center h-64">
              <svg class="animate-spin h-12 w-12 text-indigo-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            </div>
            
            <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-6">
              <!-- Профиль -->
              <div class="md:col-span-1">
                <div class="bg-white shadow overflow-hidden sm:rounded-lg">
                  <div class="px-4 py-5 sm:px-6 flex justify-between items-center">
                    <div>
                      <h3 class="text-lg leading-6 font-medium text-gray-900">Информация о пользователе</h3>
                      <p class="mt-1 max-w-2xl text-sm text-gray-500">Ваши персональные данные</p>
                    </div>
                    <button
                      @click="isEditing = !isEditing"
                      class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md text-indigo-700 bg-indigo-100 hover:bg-indigo-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                    >
                      {{ isEditing ? 'Отмена' : 'Редактировать' }}
                    </button>
                  </div>
                  <!-- Режим просмотра -->
                  <div v-if="!isEditing" class="border-t border-gray-200 px-4 py-5 sm:p-0">
                    <dl class="sm:divide-y sm:divide-gray-200">
                      <div class="py-4 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt class="text-sm font-medium text-gray-500">Имя</dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{{ user?.first_name }}</dd>
                      </div>
                      <div class="py-4 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt class="text-sm font-medium text-gray-500">Фамилия</dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{{ user?.last_name }}</dd>
                      </div>
                      <div class="py-4 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt class="text-sm font-medium text-gray-500">Email</dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{{ user?.email }}</dd>
                      </div>
                      <div class="py-4 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt class="text-sm font-medium text-gray-500">Телефон</dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{{ user?.phone || 'Не указан' }}</dd>
                      </div>
                      <div class="py-4 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt class="text-sm font-medium text-gray-500">Роль</dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                          <span v-if="isAdmin" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                            Администратор
                          </span>
                          <span v-else class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-blue-100 text-blue-800">
                            Клиент
                          </span>
                        </dd>
                      </div>
                    </dl>
                  </div>
                  
                  <!-- Режим редактирования -->
                  <div v-else class="border-t border-gray-200 px-4 py-5 sm:p-6">
                    <form @submit.prevent="updateProfile">
                      <div class="space-y-6">
                        <div>
                          <label for="first_name" class="block text-sm font-medium text-gray-700">Имя</label>
                          <input
                            type="text"
                            name="first_name"
                            id="first_name"
                            v-model="userForm.first_name"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                          />
                        </div>
                        <div>
                          <label for="last_name" class="block text-sm font-medium text-gray-700">Фамилия</label>
                          <input
                            type="text"
                            name="last_name"
                            id="last_name"
                            v-model="userForm.last_name"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                          />
                        </div>
                        <div>
                          <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
                          <input
                            type="email"
                            name="email"
                            id="email"
                            disabled
                            v-model="userForm.email"
                            class="mt-1 block w-full border border-gray-300 bg-gray-100 rounded-md shadow-sm py-2 px-3 focus:outline-none sm:text-sm"
                          />
                          <p class="mt-1 text-xs text-gray-500">Email нельзя изменить</p>
                        </div>
                        <div>
                          <label for="phone" class="block text-sm font-medium text-gray-700">Телефон</label>
                          <input
                            type="tel"
                            name="phone"
                            id="phone"
                            v-model="userForm.phone"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                          />
                        </div>
                        
                        <div class="flex justify-end space-x-3">
                          <button
                            type="button"
                            @click="isEditing = false"
                            class="inline-flex justify-center py-2 px-4 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                          >
                            Отмена
                          </button>
                          <button
                            type="submit"
                            :disabled="loading"
                            class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                          >
                            Сохранить
                          </button>
                        </div>
                      </div>
                    </form>
                  </div>
                </div>
                
                <!-- Смена пароля -->
                <div class="bg-white shadow overflow-hidden sm:rounded-lg mt-6">
                  <div class="px-4 py-5 sm:px-6">
                    <h3 class="text-lg leading-6 font-medium text-gray-900">Безопасность</h3>
                    <p class="mt-1 max-w-2xl text-sm text-gray-500">Управление паролем</p>
                  </div>
                  <div class="border-t border-gray-200 px-4 py-5 sm:p-6">
                    <form @submit.prevent="changePassword">
                      <div class="space-y-6">
                        <div>
                          <label for="current_password" class="block text-sm font-medium text-gray-700">Текущий пароль</label>
                          <input
                            type="password"
                            name="current_password"
                            id="current_password"
                            v-model="passwordForm.current_password"
                            required
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                          />
                        </div>
                        <div>
                          <label for="new_password" class="block text-sm font-medium text-gray-700">Новый пароль</label>
                          <input
                            type="password"
                            name="new_password"
                            id="new_password"
                            v-model="passwordForm.new_password"
                            required
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                          />
                        </div>
                        <div>
                          <label for="confirm_password" class="block text-sm font-medium text-gray-700">Подтверждение нового пароля</label>
                          <input
                            type="password"
                            name="confirm_password"
                            id="confirm_password"
                            v-model="passwordForm.confirm_password"
                            required
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                          />
                        </div>
                        
                        <div class="flex justify-end">
                          <button
                            type="submit"
                            :disabled="loading || passwordForm.new_password !== passwordForm.confirm_password"
                            class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                          >
                            Сменить пароль
                          </button>
                        </div>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
              
              <!-- Бронирования -->
              <div class="md:col-span-2">
                <div class="bg-white shadow overflow-hidden sm:rounded-lg">
                  <div class="px-4 py-5 sm:px-6">
                    <h3 class="text-lg leading-6 font-medium text-gray-900">Мои бронирования</h3>
                    <p class="mt-1 max-w-2xl text-sm text-gray-500">История ваших заказов</p>
                  </div>
                  <div class="border-t border-gray-200">
                    <div v-if="bookings.length === 0" class="p-6 text-center text-gray-500">
                      У вас пока нет бронирований. <NuxtLink to="/tours" class="text-indigo-600 hover:text-indigo-500">Выберите тур</NuxtLink>
                    </div>
                    
                    <ul v-else role="list" class="divide-y divide-gray-200">
                      <li v-for="booking in bookings" :key="booking.id" class="p-4 hover:bg-gray-50">
                        <div class="flex items-center space-x-4">
                          <div class="flex-shrink-0">
                            <div class="h-10 w-10 rounded-full bg-indigo-100 flex items-center justify-center">
                              <svg class="h-6 w-6 text-indigo-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                              </svg>
                            </div>
                          </div>
                          <div class="flex-1 min-w-0">
                            <p class="text-sm font-medium text-gray-900 truncate">
                              {{ booking.tour?.title || 'Тур' }} 
                            </p>
                            <p class="text-sm text-gray-500 truncate">
                              {{ formatDate(booking.start_date) }} - {{ formatDate(booking.end_date) }}
                            </p>
                          </div>
                          <div>
                            <span :class="getStatusClass(booking.status)">
                              {{ getStatusText(booking.status) }}
                            </span>
                          </div>
                          <div>
                            <NuxtLink :to="`/booking/${booking.id}`" 
                              class="inline-flex items-center px-2.5 py-1.5 border border-transparent text-xs font-medium rounded text-indigo-700 bg-indigo-100 hover:bg-indigo-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                            >
                              Детали
                            </NuxtLink>
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
import { ref, reactive, onMounted, computed } from 'vue';
import { useAuthStore } from '~/store/auth';
import { storeToRefs } from 'pinia';

const authStore = useAuthStore();
const { user, loading, error } = storeToRefs(authStore);
const isAdmin = computed(() => authStore.isAdmin);

const router = useRouter();

// Редактирование профиля
const isEditing = ref(false);
const userForm = reactive({
  first_name: '',
  last_name: '',
  email: '',
  phone: ''
});

// Форма смены пароля
const passwordForm = reactive({
  current_password: '',
  new_password: '',
  confirm_password: ''
});

// Бронирования
const bookings = ref([]);
const bookingsLoading = ref(false);
const bookingsError = ref(null);

// Получение бронирований
const fetchBookings = async () => {
  bookingsLoading.value = true;
  try {
    const response = await fetch(`${useRuntimeConfig().public.apiBase}/bookings/user`, {
      headers: {
        'Authorization': `Bearer ${authStore.token}`
      }
    });
    
    if (!response.ok) {
      throw new Error('Ошибка при получении бронирований');
    }
    
    bookings.value = await response.json();
  } catch (error) {
    bookingsError.value = error.message;
    console.error('Ошибка при получении бронирований:', error);
  } finally {
    bookingsLoading.value = false;
  }
};

// Обновление профиля
const updateProfile = async () => {
  try {
    const response = await fetch(`${useRuntimeConfig().public.apiBase}/users/me`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${authStore.token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        first_name: userForm.first_name,
        last_name: userForm.last_name,
        phone: userForm.phone
      })
    });
    
    if (!response.ok) {
      throw new Error('Ошибка при обновлении профиля');
    }
    
    // Обновляем данные пользователя в хранилище
    await authStore.fetchUserInfo();
    isEditing.value = false;
  } catch (error) {
    console.error('Ошибка при обновлении профиля:', error);
  }
};

// Смена пароля
const changePassword = async () => {
  if (passwordForm.new_password !== passwordForm.confirm_password) {
    alert('Пароли не совпадают');
    return;
  }
  
  try {
    const response = await fetch(`${useRuntimeConfig().public.apiBase}/users/me/password`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${authStore.token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        current_password: passwordForm.current_password,
        new_password: passwordForm.new_password
      })
    });
    
    if (!response.ok) {
      const data = await response.json();
      throw new Error(data.detail || 'Ошибка при смене пароля');
    }
    
    // Очищаем форму
    passwordForm.current_password = '';
    passwordForm.new_password = '';
    passwordForm.confirm_password = '';
    
    alert('Пароль успешно изменен');
  } catch (error) {
    alert(error.message);
    console.error('Ошибка при смене пароля:', error);
  }
};

// Утилиты для бронирований
const formatDate = (dateString) => {
  if (!dateString) return '';
  const date = new Date(dateString);
  return date.toLocaleDateString('ru-RU');
};

const getStatusClass = (status) => {
  const statusClasses = {
    'pending': 'px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800',
    'confirmed': 'px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800',
    'cancelled': 'px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800',
    'completed': 'px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-blue-100 text-blue-800'
  };
  
  return statusClasses[status] || statusClasses['pending'];
};

const getStatusText = (status) => {
  const statusTexts = {
    'pending': 'Ожидает подтверждения',
    'confirmed': 'Подтверждено',
    'cancelled': 'Отменено',
    'completed': 'Завершено'
  };
  
  return statusTexts[status] || 'Неизвестно';
};

// Инициализация
onMounted(async () => {
  if (!authStore.isAuthenticated) {
    return router.push('/login');
  }
  
  // Заполняем форму текущими данными
  if (user.value) {
    userForm.first_name = user.value.first_name;
    userForm.last_name = user.value.last_name;
    userForm.email = user.value.email;
    userForm.phone = user.value.phone || '';
  }
  
  // Загружаем бронирования
  await fetchBookings();
});
</script> 