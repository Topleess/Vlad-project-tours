<template>
  <div class="min-h-screen bg-gray-100">
    <div class="py-10">
      <header>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold leading-tight text-gray-900">Управление турами</h1>
            <div class="flex space-x-3">
              <button
                @click="openTourModal(null)"
                class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
              >
                <svg class="-ml-1 mr-2 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
                </svg>
                Добавить тур
              </button>
              <NuxtLink to="/admin" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-indigo-700 bg-indigo-100 hover:bg-indigo-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                Назад к панели управления
              </NuxtLink>
            </div>
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
                          placeholder="Поиск по названию тура или стране"
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
                  <div class="mt-4 flex md:mt-0 md:ml-4 space-x-3">
                    <select
                      v-model="categoryFilter"
                      @change="handleSearch"
                      class="block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    >
                      <option value="">Все категории</option>
                      <option value="beach">Пляжный отдых</option>
                      <option value="adventure">Приключения</option>
                      <option value="city">Городские туры</option>
                      <option value="culture">Культурные туры</option>
                    </select>
                    
                    <select
                      v-model="sortBy"
                      @change="handleSearch"
                      class="block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    >
                      <option value="title_asc">По названию (А-Я)</option>
                      <option value="title_desc">По названию (Я-А)</option>
                      <option value="price_asc">По цене (низкая-высокая)</option>
                      <option value="price_desc">По цене (высокая-низкая)</option>
                      <option value="date_asc">По дате (старые-новые)</option>
                      <option value="date_desc">По дате (новые-старые)</option>
                    </select>
                  </div>
                </div>
              </div>

              <!-- Список туров -->
              <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
                <div v-if="loading" class="col-span-full text-center py-12">
                  <svg class="mx-auto h-12 w-12 text-indigo-600 animate-spin" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  <p class="mt-4 text-lg text-gray-600">Загрузка туров...</p>
                </div>
                
                <div v-else-if="tours.length === 0" class="col-span-full text-center py-12">
                  <svg class="mx-auto h-12 w-12 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <p class="mt-4 text-lg text-gray-600">Туры не найдены</p>
                  <p class="mt-2 text-gray-500">Попробуйте изменить параметры поиска или добавьте новый тур</p>
                </div>
                
                <div v-for="tour in tours" :key="tour.id" class="bg-white overflow-hidden shadow rounded-lg">
                  <div class="relative h-48 w-full overflow-hidden group">
                    <img v-if="tour.image_url" :src="tour.image_url" class="h-full w-full object-cover transition-all duration-300 group-hover:scale-105" :alt="tour.title" />
                    <div v-else class="h-full w-full bg-gray-200 flex items-center justify-center">
                      <svg class="h-12 w-12 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                      </svg>
                    </div>
                    <div class="absolute top-2 right-2 bg-white bg-opacity-90 rounded-full p-1">
                      <span class="px-2 py-1 text-xs font-medium text-gray-800">
                        {{ tour.price.toLocaleString('ru-RU') }} ₽
                      </span>
                    </div>
                  </div>
                  <div class="p-5">
                    <h3 class="text-lg leading-6 font-medium text-gray-900">
                      {{ tour.title }}
                    </h3>
                    <p class="mt-1 text-sm text-gray-500">
                      {{ tour.country }}, {{ tour.city }}
                    </p>
                    <p class="mt-2 text-sm text-gray-500 line-clamp-2">
                      {{ tour.description }}
                    </p>
                    <div class="mt-3 flex items-center text-sm text-gray-500">
                      <svg class="flex-shrink-0 mr-1.5 h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd" />
                      </svg>
                      <span>{{ tour.duration }} дней</span>
                    </div>
                    <div class="mt-4 flex justify-end space-x-3">
                      <button 
                        @click="openTourModal(tour)" 
                        class="inline-flex items-center px-3 py-1.5 border border-transparent text-xs font-medium rounded-md text-indigo-700 bg-indigo-100 hover:bg-indigo-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                      >
                        Редактировать
                      </button>
                      <button 
                        @click="confirmDelete(tour)" 
                        class="inline-flex items-center px-3 py-1.5 border border-transparent text-xs font-medium rounded-md text-red-700 bg-red-100 hover:bg-red-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
                      >
                        Удалить
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- Пагинация -->
              <div class="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6 mt-6 rounded-lg shadow">
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
                      Показаны <span class="font-medium">{{ (currentPage - 1) * perPage + 1 }}</span> - <span class="font-medium">{{ Math.min(currentPage * perPage, totalTours) }}</span> из <span class="font-medium">{{ totalTours }}</span> туров
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
      </main>
    </div>
    
    <!-- Модальное окно для редактирования/добавления тура -->
    <div v-if="tourModal.show" class="fixed z-10 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
      <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true" @click="tourModal.show = false"></div>

        <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>

        <div class="inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-2xl sm:w-full sm:p-6">
          <div>
            <div class="mt-3 text-center sm:mt-5">
              <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
                {{ tourModal.isNew ? 'Добавление нового тура' : 'Редактирование тура' }}
              </h3>
              <div class="mt-4">
                <form @submit.prevent="saveTour" class="space-y-6">
                  <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
                    <div class="sm:col-span-6">
                      <label for="title" class="block text-sm font-medium text-gray-700 text-left">Название тура</label>
                      <input
                        type="text"
                        name="title"
                        id="title"
                        v-model="tourModal.tour.title"
                        required
                        class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                      />
                    </div>
                    
                    <div class="sm:col-span-3">
                      <label for="country" class="block text-sm font-medium text-gray-700 text-left">Страна</label>
                      <input
                        type="text"
                        name="country"
                        id="country"
                        v-model="tourModal.tour.country"
                        required
                        class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                      />
                    </div>
                    
                    <div class="sm:col-span-3">
                      <label for="city" class="block text-sm font-medium text-gray-700 text-left">Город</label>
                      <input
                        type="text"
                        name="city"
                        id="city"
                        v-model="tourModal.tour.city"
                        required
                        class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                      />
                    </div>
                    
                    <div class="sm:col-span-3">
                      <label for="duration" class="block text-sm font-medium text-gray-700 text-left">Продолжительность (дней)</label>
                      <input
                        type="number"
                        name="duration"
                        id="duration"
                        v-model="tourModal.tour.duration"
                        min="1"
                        required
                        class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                      />
                    </div>
                    
                    <div class="sm:col-span-3">
                      <label for="price" class="block text-sm font-medium text-gray-700 text-left">Цена (₽)</label>
                      <input
                        type="number"
                        name="price"
                        id="price"
                        v-model="tourModal.tour.price"
                        min="0"
                        required
                        class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                      />
                    </div>
                    
                    <div class="sm:col-span-3">
                      <label for="category" class="block text-sm font-medium text-gray-700 text-left">Категория</label>
                      <select
                        id="category"
                        name="category"
                        v-model="tourModal.tour.category"
                        required
                        class="mt-1 block w-full bg-white border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                      >
                        <option value="beach">Пляжный отдых</option>
                        <option value="adventure">Приключения</option>
                        <option value="city">Городские туры</option>
                        <option value="culture">Культурные туры</option>
                      </select>
                    </div>
                    
                    <div class="sm:col-span-3">
                      <label for="image_url" class="block text-sm font-medium text-gray-700 text-left">URL изображения</label>
                      <input
                        type="url"
                        name="image_url"
                        id="image_url"
                        v-model="tourModal.tour.image_url"
                        class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        placeholder="https://example.com/image.jpg"
                      />
                    </div>
                    
                    <div class="sm:col-span-6">
                      <label for="description" class="block text-sm font-medium text-gray-700 text-left">Описание</label>
                      <textarea
                        id="description"
                        name="description"
                        rows="4"
                        v-model="tourModal.tour.description"
                        required
                        class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                      ></textarea>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
          <div class="mt-5 sm:mt-6 sm:grid sm:grid-cols-2 sm:gap-3 sm:grid-flow-row-dense">
            <button
              type="button"
              @click="saveTour"
              class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-indigo-600 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:col-start-2 sm:text-sm"
            >
              {{ tourModal.isNew ? 'Добавить' : 'Сохранить' }}
            </button>
            <button
              type="button"
              @click="tourModal.show = false"
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
const { user, loading: authLoading } = storeToRefs(authStore);
const isAdmin = computed(() => authStore.isAdmin);

const router = useRouter();

// Состояние
const tours = ref([]);
const loading = ref(false);
const error = ref(null);

// Пагинация
const currentPage = ref(1);
const perPage = ref(9);
const totalTours = ref(0);
const totalPages = computed(() => Math.ceil(totalTours.value / perPage.value));

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
const categoryFilter = ref('');
const sortBy = ref('date_desc');

// Модальное окно для тура
const tourModal = reactive({
  show: false,
  isNew: true,
  tour: {
    id: null,
    title: '',
    country: '',
    city: '',
    description: '',
    price: 0,
    duration: 7,
    category: 'beach',
    image_url: ''
  }
});

// Получение списка туров
const fetchTours = async () => {
  loading.value = true;
  error.value = null;
  
  try {
    let url = `${useRuntimeConfig().public.apiBase}/tours?page=${currentPage.value}&limit=${perPage.value}`;
    
    if (searchQuery.value) {
      url += `&search=${encodeURIComponent(searchQuery.value)}`;
    }
    
    if (categoryFilter.value) {
      url += `&category=${categoryFilter.value}`;
    }
    
    if (sortBy.value) {
      url += `&sort=${sortBy.value}`;
    }
    
    const response = await fetch(url, {
      headers: {
        'Authorization': `Bearer ${authStore.token}`
      }
    });
    
    if (!response.ok) {
      throw new Error('Ошибка при получении списка туров');
    }
    
    const data = await response.json();
    tours.value = data.items;
    totalTours.value = data.total;
  } catch (err) {
    error.value = err.message;
    console.error('Ошибка при получении туров:', err);
  } finally {
    loading.value = false;
  }
};

// Обработка поиска
const handleSearch = () => {
  currentPage.value = 1;
  fetchTours();
};

// Смена страницы пагинации
const changePage = (page) => {
  if (page < 1 || page > totalPages.value) return;
  currentPage.value = page;
  fetchTours();
};

// Открыть модальное окно для добавления/редактирования тура
const openTourModal = (tour) => {
  if (tour) {
    tourModal.isNew = false;
    tourModal.tour = { ...tour };
  } else {
    tourModal.isNew = true;
    tourModal.tour = {
      id: null,
      title: '',
      country: '',
      city: '',
      description: '',
      price: 0,
      duration: 7,
      category: 'beach',
      image_url: ''
    };
  }
  tourModal.show = true;
};

// Сохранение тура
const saveTour = async () => {
  loading.value = true;
  try {
    const method = tourModal.isNew ? 'POST' : 'PUT';
    const endpoint = tourModal.isNew 
      ? `${useRuntimeConfig().public.apiBase}/tours` 
      : `${useRuntimeConfig().public.apiBase}/tours/${tourModal.tour.id}`;
    
    const response = await fetch(endpoint, {
      method,
      headers: {
        'Authorization': `Bearer ${authStore.token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(tourModal.tour)
    });
    
    if (!response.ok) {
      throw new Error(`Ошибка при ${tourModal.isNew ? 'добавлении' : 'обновлении'} тура`);
    }
    
    // Обновляем список туров
    await fetchTours();
    
    // Закрываем модальное окно
    tourModal.show = false;
  } catch (error) {
    console.error('Ошибка при сохранении тура:', error);
    alert(`Ошибка при ${tourModal.isNew ? 'добавлении' : 'обновлении'} тура: ${error.message}`);
  } finally {
    loading.value = false;
  }
};

// Подтверждение удаления тура
const confirmDelete = (tour) => {
  if (confirm(`Вы уверены, что хотите удалить тур "${tour.title}"?`)) {
    deleteTour(tour.id);
  }
};

// Удаление тура
const deleteTour = async (id) => {
  loading.value = true;
  try {
    const response = await fetch(`${useRuntimeConfig().public.apiBase}/tours/${id}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${authStore.token}`
      }
    });
    
    if (!response.ok) {
      throw new Error('Ошибка при удалении тура');
    }
    
    // Обновляем список туров
    await fetchTours();
  } catch (error) {
    console.error('Ошибка при удалении тура:', error);
    alert('Ошибка при удалении тура: ' + error.message);
  } finally {
    loading.value = false;
  }
};

// Инициализация
onMounted(async () => {
  if (!authStore.isAuthenticated) {
    return router.push('/login');
  }
  
  if (isAdmin.value) {
    await fetchTours();
  }
});
</script> 