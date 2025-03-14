<template>
  <div class="min-h-screen bg-gray-100">
    <div class="py-10">
      <header>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold leading-tight text-gray-900">Управление пользователями</h1>
            <NuxtLink to="/admin" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-indigo-700 bg-indigo-100 hover:bg-indigo-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
              Назад к панели управления
            </NuxtLink>
          </div>
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
            
            <div v-else>
              <!-- Поиск и фильтры -->
              <div class="bg-white shadow px-4 py-5 sm:rounded-lg sm:p-6 mb-6">
                <div class="md:flex md:items-center md:justify-between">
                  <div class="flex-1 min-w-0">
                    <div class="mt-1 flex rounded-md shadow-sm">
                      <div class="relative flex items-stretch flex-grow focus-within:z-10">
                        <input
                          type="text"
                          v-model="searchQuery"
                          @input="handleSearch"
                          class="focus:ring-indigo-500 focus:border-indigo-500 block w-full rounded-none rounded-l-md sm:text-sm border-gray-300"
                          placeholder="Поиск по имени, email или телефону"
                        />
                      </div>
                      <button
                        type="button"
                        @click="handleSearch"
                        class="-ml-px relative inline-flex items-center space-x-2 px-4 py-2 border border-gray-300 text-sm font-medium rounded-r-md text-gray-700 bg-gray-50 hover:bg-gray-100 focus:outline-none focus:ring-1 focus:ring-indigo-500 focus:border-indigo-500"
                      >
                        <svg class="h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                          <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd" />
                        </svg>
                        <span>Поиск</span>
                      </button>
                    </div>
                  </div>
                  <div class="mt-4 flex md:mt-0 md:ml-4">
                    <select
                      v-model="filterRole"
                      @change="handleSearch"
                      class="block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    >
                      <option value="">Все роли</option>
                      <option value="admin">Администраторы</option>
                      <option value="client">Клиенты</option>
                    </select>
                  </div>
                </div>
              </div>

              <!-- Таблица пользователей -->
              <div class="bg-white shadow overflow-hidden sm:rounded-lg">
                <div class="flex flex-col">
                  <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
                    <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
                      <div class="overflow-hidden border-b border-gray-200">
                        <table class="min-w-full divide-y divide-gray-200">
                          <thead class="bg-gray-50">
                            <tr>
                              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Пользователь
                              </th>
                              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Контакты
                              </th>
                              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Статус/Роль
                              </th>
                              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Регистрация
                              </th>
                              <th scope="col" class="relative px-6 py-3">
                                <span class="sr-only">Действия</span>
                              </th>
                            </tr>
                          </thead>
                          <tbody class="bg-white divide-y divide-gray-200">
                            <tr v-if="loading" class="text-center">
                              <td colspan="5" class="px-6 py-4 whitespace-nowrap">
                                <div class="flex justify-center">
                                  <svg class="animate-spin h-5 w-5 text-indigo-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                  </svg>
                                  <span class="ml-2">Загрузка...</span>
                                </div>
                              </td>
                            </tr>
                            
                            <tr v-if="users.length === 0 && !loading" class="text-center">
                              <td colspan="5" class="px-6 py-4 whitespace-nowrap text-gray-500">
                                Пользователи не найдены
                              </td>
                            </tr>
                            
                            <tr v-for="user in users" :key="user.id" class="hover:bg-gray-50">
                              <td class="px-6 py-4 whitespace-nowrap">
                                <div class="flex items-center">
                                  <div class="flex-shrink-0 h-10 w-10">
                                    <div class="h-10 w-10 rounded-full bg-indigo-100 flex items-center justify-center">
                                      <span class="text-sm font-medium text-indigo-600">
                                        {{ getUserInitials(user) }}
                                      </span>
                                    </div>
                                  </div>
                                  <div class="ml-4">
                                    <div class="text-sm font-medium text-gray-900">
                                      {{ user.first_name }} {{ user.last_name }}
                                    </div>
                                    <div class="text-sm text-gray-500">
                                      ID: {{ user.id }}
                                    </div>
                                  </div>
                                </div>
                              </td>
                              <td class="px-6 py-4 whitespace-nowrap">
                                <div class="text-sm text-gray-900">{{ user.email }}</div>
                                <div class="text-sm text-gray-500">{{ user.phone || 'Телефон не указан' }}</div>
                              </td>
                              <td class="px-6 py-4 whitespace-nowrap">
                                <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full" :class="user.is_active ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'">
                                  {{ user.is_active ? 'Активен' : 'Заблокирован' }}
                                </span>
                                <span class="ml-2 px-2 inline-flex text-xs leading-5 font-semibold rounded-full" :class="user.is_admin ? 'bg-purple-100 text-purple-800' : 'bg-blue-100 text-blue-800'">
                                  {{ user.is_admin ? 'Администратор' : 'Клиент' }}
                                </span>
                              </td>
                              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                {{ formatDate(user.created_at) }}
                              </td>
                              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                                <button 
                                  @click="openUserModal(user)" 
                                  class="text-indigo-600 hover:text-indigo-900 mr-2"
                                >
                                  Редактировать
                                </button>
                                <button 
                                  @click="toggleUserStatus(user)" 
                                  :class="user.is_active ? 'text-red-600 hover:text-red-900' : 'text-green-600 hover:text-green-900'"
                                >
                                  {{ user.is_active ? 'Заблокировать' : 'Разблокировать' }}
                                </button>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                </div>
                
                <!-- Пагинация -->
                <div class="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6">
                  <div class="flex-1 flex justify-between sm:hidden">
                    <button 
                      @click="changePage(currentPage - 1)" 
                      :disabled="currentPage === 1"
                      class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 disabled:opacity-50"
                    >
                      Назад
                    </button>
                    <button 
                      @click="changePage(currentPage + 1)" 
                      :disabled="currentPage === totalPages"
                      class="ml-3 relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 disabled:opacity-50"
                    >
                      Вперед
                    </button>
                  </div>
                  <div class="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
                    <div>
                      <p class="text-sm text-gray-700">
                        Показаны <span class="font-medium">{{ (currentPage - 1) * perPage + 1 }}</span> - <span class="font-medium">{{ Math.min(currentPage * perPage, totalUsers) }}</span> из <span class="font-medium">{{ totalUsers }}</span> пользователей
                      </p>
                    </div>
                    <div>
                      <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
                        <button 
                          @click="changePage(currentPage - 1)" 
                          :disabled="currentPage === 1"
                          class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50 disabled:opacity-50"
                        >
                          <span class="sr-only">Предыдущая</span>
                          <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                            <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
                          </svg>
                        </button>
                        <button 
                          v-for="page in paginationPages" 
                          :key="page" 
                          @click="changePage(page)"
                          :class="[
                            page === currentPage ? 'z-10 bg-indigo-50 border-indigo-500 text-indigo-600' : 'bg-white border-gray-300 text-gray-500 hover:bg-gray-50',
                            'relative inline-flex items-center px-4 py-2 border text-sm font-medium'
                          ]"
                        >
                          {{ page }}
                        </button>
                        <button 
                          @click="changePage(currentPage + 1)" 
                          :disabled="currentPage === totalPages"
                          class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50 disabled:opacity-50"
                        >
                          <span class="sr-only">Следующая</span>
                          <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                            <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                          </svg>
                        </button>
                      </nav>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
    
    <!-- Модальное окно редактирования пользователя -->
    <div v-if="userModal.show" class="fixed z-10 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
      <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true" @click="userModal.show = false"></div>

        <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>

        <div class="inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full sm:p-6">
          <div>
            <div class="mt-3 text-center sm:mt-5">
              <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
                Редактирование пользователя
              </h3>
              <div class="mt-2">
                <form @submit.prevent="updateUser">
                  <div class="space-y-6">
                    <div>
                      <label for="first_name" class="block text-sm font-medium text-gray-700 text-left">Имя</label>
                      <input
                        type="text"
                        name="first_name"
                        id="first_name"
                        v-model="userModal.user.first_name"
                        class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                      />
                    </div>
                    <div>
                      <label for="last_name" class="block text-sm font-medium text-gray-700 text-left">Фамилия</label>
                      <input
                        type="text"
                        name="last_name"
                        id="last_name"
                        v-model="userModal.user.last_name"
                        class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                      />
                    </div>
                    <div>
                      <label for="email" class="block text-sm font-medium text-gray-700 text-left">Email</label>
                      <input
                        type="email"
                        name="email"
                        id="email"
                        v-model="userModal.user.email"
                        disabled
                        class="mt-1 block w-full border border-gray-300 bg-gray-100 rounded-md shadow-sm py-2 px-3 focus:outline-none sm:text-sm"
                      />
                      <p class="mt-1 text-xs text-gray-500 text-left">Email нельзя изменить</p>
                    </div>
                    <div>
                      <label for="phone" class="block text-sm font-medium text-gray-700 text-left">Телефон</label>
                      <input
                        type="tel"
                        name="phone"
                        id="phone"
                        v-model="userModal.user.phone"
                        class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                      />
                    </div>
                    
                    <div class="flex items-center">
                      <input
                        id="is_active"
                        name="is_active"
                        type="checkbox"
                        v-model="userModal.user.is_active"
                        class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
                      />
                      <label for="is_active" class="ml-2 block text-sm text-gray-900">
                        Активный пользователь
                      </label>
                    </div>
                    
                    <div class="flex items-center">
                      <input
                        id="is_admin"
                        name="is_admin"
                        type="checkbox"
                        v-model="userModal.user.is_admin"
                        class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
                      />
                      <label for="is_admin" class="ml-2 block text-sm text-gray-900">
                        Права администратора
                      </label>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
          <div class="mt-5 sm:mt-6 sm:grid sm:grid-cols-2 sm:gap-3 sm:grid-flow-row-dense">
            <button
              type="button"
              @click="updateUser"
              class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-indigo-600 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:col-start-2 sm:text-sm"
            >
              Сохранить
            </button>
            <button
              type="button"
              @click="userModal.show = false"
              class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:col-start-1 sm:text-sm"
            >
              Отмена
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, reactive, onMounted } from 'vue';
import { useAuthStore } from '~/store/auth';
import { storeToRefs } from 'pinia';

const authStore = useAuthStore();
const { user: currentUser, loading: authLoading } = storeToRefs(authStore);
const isAdmin = computed(() => authStore.isAdmin);

const router = useRouter();

// Состояние
const users = ref([]);
const loading = ref(false);
const error = ref(null);

// Пагинация
const currentPage = ref(1);
const perPage = ref(10);
const totalUsers = ref(0);
const totalPages = computed(() => Math.ceil(totalUsers.value / perPage.value));

// Вычисляем страницы для пагинации (показываем максимум 5 страниц)
const paginationPages = computed(() => {
  const pages = [];
  let startPage = Math.max(1, currentPage.value - 2);
  let endPage = Math.min(totalPages.value, startPage + 4);
  
  if (endPage - startPage < 4) {
    startPage = Math.max(1, endPage - 4);
  }
  
  for (let i = startPage; i <= endPage; i++) {
    pages.push(i);
  }
  
  return pages;
});

// Поиск и фильтрация
const searchQuery = ref('');
const filterRole = ref('');

// Модальное окно редактирования пользователя
const userModal = reactive({
  show: false,
  user: {
    id: null,
    first_name: '',
    last_name: '',
    email: '',
    phone: '',
    is_active: true,
    is_admin: false
  }
});

// Получение списка пользователей
const fetchUsers = async () => {
  loading.value = true;
  error.value = null;
  
  try {
    let url = `${useRuntimeConfig().public.apiBase}/admin/users?page=${currentPage.value}&limit=${perPage.value}`;
    
    if (searchQuery.value) {
      url += `&search=${encodeURIComponent(searchQuery.value)}`;
    }
    
    if (filterRole.value) {
      url += `&role=${filterRole.value}`;
    }
    
    const response = await fetch(url, {
      headers: {
        'Authorization': `Bearer ${authStore.token}`
      }
    });
    
    if (!response.ok) {
      throw new Error('Ошибка при получении списка пользователей');
    }
    
    const data = await response.json();
    users.value = data.items;
    totalUsers.value = data.total;
  } catch (err) {
    error.value = err.message;
    console.error('Ошибка при получении пользователей:', err);
  } finally {
    loading.value = false;
  }
};

// Обработка поиска
const handleSearch = () => {
  currentPage.value = 1;
  fetchUsers();
};

// Смена страницы пагинации
const changePage = (page) => {
  if (page < 1 || page > totalPages.value) return;
  currentPage.value = page;
  fetchUsers();
};

// Получение инициалов пользователя для аватара
const getUserInitials = (user) => {
  const first = user.first_name ? user.first_name.charAt(0).toUpperCase() : '';
  const last = user.last_name ? user.last_name.charAt(0).toUpperCase() : '';
  return first + last;
};

// Форматирование даты
const formatDate = (dateString) => {
  if (!dateString) return '';
  const date = new Date(dateString);
  return date.toLocaleDateString('ru-RU');
};

// Открытие модального окна редактирования пользователя
const openUserModal = (user) => {
  userModal.user = { ...user };
  userModal.show = true;
};

// Обновление пользователя
const updateUser = async () => {
  loading.value = true;
  
  try {
    const response = await fetch(`${useRuntimeConfig().public.apiBase}/admin/users/${userModal.user.id}`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${authStore.token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        first_name: userModal.user.first_name,
        last_name: userModal.user.last_name,
        phone: userModal.user.phone,
        is_active: userModal.user.is_active,
        is_admin: userModal.user.is_admin
      })
    });
    
    if (!response.ok) {
      throw new Error('Ошибка при обновлении пользователя');
    }
    
    // Обновляем список пользователей
    await fetchUsers();
    
    // Закрываем модальное окно
    userModal.show = false;
  } catch (error) {
    console.error('Ошибка при обновлении пользователя:', error);
    alert('Ошибка при обновлении пользователя: ' + error.message);
  } finally {
    loading.value = false;
  }
};

// Переключение статуса пользователя (активен/заблокирован)
const toggleUserStatus = async (user) => {
  if (confirm(`Вы уверены, что хотите ${user.is_active ? 'заблокировать' : 'разблокировать'} пользователя ${user.first_name} ${user.last_name}?`)) {
    loading.value = true;
    
    try {
      const response = await fetch(`${useRuntimeConfig().public.apiBase}/admin/users/${user.id}/toggle-status`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${authStore.token}`
        }
      });
      
      if (!response.ok) {
        throw new Error('Ошибка при изменении статуса пользователя');
      }
      
      // Обновляем список пользователей
      await fetchUsers();
    } catch (error) {
      console.error('Ошибка при изменении статуса пользователя:', error);
      alert('Ошибка при изменении статуса пользователя: ' + error.message);
    } finally {
      loading.value = false;
    }
  }
};

// Инициализация
onMounted(async () => {
  if (!authStore.isAuthenticated) {
    return router.push('/login');
  }
  
  if (isAdmin.value) {
    await fetchUsers();
  }
});
</script> 