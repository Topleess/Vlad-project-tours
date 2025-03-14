<template>
  <div>
    <div class="bg-blue-800 py-10">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 class="text-3xl font-extrabold text-white text-center">Каталог туров</h1>
        <p class="mt-3 text-xl text-blue-200 text-center max-w-3xl mx-auto">
          Выберите идеальный тур для вашего отпуска из нашей коллекции
        </p>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Фильтры -->
      <div class="bg-white p-6 rounded-lg shadow mb-8">
        <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
          <!-- Направление -->
          <div>
            <label for="destination" class="block text-sm font-medium text-gray-700">Направление</label>
            <select id="destination" v-model="filters.destination" class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-primary focus:border-primary sm:text-sm rounded-md">
              <option value="">Все направления</option>
              <option value="turkey">Турция</option>
              <option value="italy">Италия</option>
              <option value="france">Франция</option>
              <option value="spain">Испания</option>
              <option value="greece">Греция</option>
            </select>
          </div>

          <!-- Тип тура -->
          <div>
            <label for="type" class="block text-sm font-medium text-gray-700">Тип тура</label>
            <select id="type" v-model="filters.type" class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-primary focus:border-primary sm:text-sm rounded-md">
              <option value="">Все типы</option>
              <option value="beach">Пляжный отдых</option>
              <option value="excursion">Экскурсионный</option>
              <option value="ski">Горнолыжный</option>
              <option value="adventure">Приключение</option>
              <option value="wellness">Оздоровительный</option>
            </select>
          </div>

          <!-- Диапазон цен -->
          <div>
            <label for="price" class="block text-sm font-medium text-gray-700">Цена (₽)</label>
            <div class="flex space-x-2 mt-1">
              <input 
                type="number" 
                id="price_min" 
                v-model="filters.priceMin" 
                placeholder="от" 
                class="block w-full px-3 py-2 sm:text-sm border-gray-300 rounded-md focus:ring-primary focus:border-primary"
              />
              <input 
                type="number" 
                id="price_max" 
                v-model="filters.priceMax" 
                placeholder="до" 
                class="block w-full px-3 py-2 sm:text-sm border-gray-300 rounded-md focus:ring-primary focus:border-primary"
              />
            </div>
          </div>

          <!-- Длительность -->
          <div>
            <label for="duration" class="block text-sm font-medium text-gray-700">Длительность (дней)</label>
            <select id="duration" v-model="filters.duration" class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-primary focus:border-primary sm:text-sm rounded-md">
              <option value="">Любая</option>
              <option value="1-3">1-3 дня</option>
              <option value="4-7">4-7 дней</option>
              <option value="8-14">8-14 дней</option>
              <option value="15+">15+ дней</option>
            </select>
          </div>
        </div>

        <!-- Вторая строка фильтров -->
        <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 mt-4">
          <!-- Дата вылета -->
          <div>
            <label for="departure_date" class="block text-sm font-medium text-gray-700">Дата вылета</label>
            <input 
              type="date" 
              id="departure_date" 
              v-model="filters.departureDate" 
              class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-primary focus:border-primary sm:text-sm rounded-md"
            />
          </div>

          <!-- Количество взрослых -->
          <div>
            <label for="adults" class="block text-sm font-medium text-gray-700">Взрослые</label>
            <input 
              type="number" 
              id="adults" 
              v-model="filters.adults" 
              min="1" 
              max="10" 
              class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-primary focus:border-primary sm:text-sm rounded-md"
            />
          </div>

          <!-- Количество детей -->
          <div>
            <label for="children" class="block text-sm font-medium text-gray-700">Дети</label>
            <input 
              type="number" 
              id="children" 
              v-model="filters.children" 
              min="0" 
              max="10" 
              class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-primary focus:border-primary sm:text-sm rounded-md"
            />
          </div>

          <!-- Кнопка поиска -->
          <div class="flex items-end">
            <button @click="applyFilters" class="w-full bg-primary hover:bg-primary-dark focus:ring-4 focus:outline-none focus:ring-primary-light rounded-lg px-5 py-2.5 text-center text-white font-medium">
              Найти туры
            </button>
          </div>
        </div>
      </div>

      <!-- Сортировка и результаты -->
      <div class="flex justify-between items-center mb-6">
        <div class="text-lg text-gray-700">
          Найдено: <span class="font-bold">{{ filteredTours.length }}</span> туров
        </div>
        <div class="flex items-center">
          <label for="sort" class="mr-2 text-sm font-medium text-gray-700">Сортировать:</label>
          <select id="sort" v-model="sortOption" class="block pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-primary focus:border-primary sm:text-sm rounded-md">
            <option value="price_asc">По цене (сначала дешевые)</option>
            <option value="price_desc">По цене (сначала дорогие)</option>
            <option value="rating_desc">По рейтингу</option>
            <option value="duration_asc">По длительности (сначала короткие)</option>
            <option value="duration_desc">По длительности (сначала длинные)</option>
          </select>
        </div>
      </div>

      <!-- Список туров -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- Карточка тура -->
        <div v-for="tour in sortedTours" :key="tour.id" class="bg-white rounded-lg shadow overflow-hidden">
          <div class="relative">
            <img :src="tour.image" :alt="tour.title" class="w-full h-48 object-cover">
            <div class="absolute top-2 right-2 bg-accent text-black text-sm font-semibold px-2 py-1 rounded">
              {{ tour.discount ? '-' + tour.discount + '%' : 'Новинка' }}
            </div>
          </div>
          <div class="p-4">
            <div class="flex justify-between items-start">
              <h3 class="text-lg font-bold text-gray-900">{{ tour.title }}</h3>
              <div class="flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-yellow-400" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                </svg>
                <span class="ml-1 text-sm font-semibold text-gray-600">{{ tour.rating }} ({{ tour.reviewsCount }})</span>
              </div>
            </div>
            <p class="mt-1 text-sm text-gray-600">{{ tour.destination }}</p>
            <div class="mt-2 flex items-center text-sm text-gray-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
              {{ tour.duration }} дней
            </div>
            <div class="mt-1 flex items-center text-sm text-gray-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
              </svg>
              {{ tour.hotelInfo }}
            </div>
            <div class="mt-1 flex items-center text-sm text-gray-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
              {{ tour.food }}
            </div>
            <div class="mt-4 flex justify-between items-center">
              <div>
                <div v-if="tour.oldPrice" class="text-sm text-gray-500 line-through">{{ formatCurrency(tour.oldPrice) }}</div>
                <div class="text-lg font-bold text-gray-900">{{ formatCurrency(tour.price) }}</div>
                <div class="text-xs text-gray-500">за человека</div>
              </div>
              <NuxtLink :to="`/tours/${tour.id}`" class="bg-primary hover:bg-primary-dark text-white py-2 px-4 rounded-md">
                Подробнее
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>

      <!-- Пагинация -->
      <div class="flex justify-center mt-8">
        <ul class="flex space-x-2">
          <li>
            <button @click="prevPage" :disabled="currentPage === 1" class="px-3 py-1 rounded-md" :class="currentPage === 1 ? 'text-gray-400 cursor-not-allowed' : 'text-primary hover:bg-blue-100'">
              &lt;
            </button>
          </li>
          <li v-for="page in totalPages" :key="page">
            <button @click="goToPage(page)" class="px-3 py-1 rounded-md" :class="currentPage === page ? 'bg-primary text-white' : 'text-primary hover:bg-blue-100'">
              {{ page }}
            </button>
          </li>
          <li>
            <button @click="nextPage" :disabled="currentPage === totalPages" class="px-3 py-1 rounded-md" :class="currentPage === totalPages ? 'text-gray-400 cursor-not-allowed' : 'text-primary hover:bg-blue-100'">
              &gt;
            </button>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

// Фильтры
const filters = ref({
  destination: '',
  type: '',
  priceMin: null,
  priceMax: null,
  duration: '',
  departureDate: null,
  adults: 2,
  children: 0
});

// Опция сортировки
const sortOption = ref('price_asc');

// Пагинация
const currentPage = ref(1);
const itemsPerPage = 9;

// Макет данных о турах (в реальном приложении данные будут загружаться с сервера)
const tours = ref([
  {
    id: 1,
    title: 'Солнечная Турция',
    destination: 'Турция, Анталья',
    type: 'beach',
    price: 45000,
    oldPrice: 50000,
    discount: 10,
    duration: 7,
    rating: 4.8,
    reviewsCount: 124,
    image: 'https://images.unsplash.com/photo-1584132967334-10e028bd69f7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80',
    hotelInfo: 'Отель 5★',
    food: 'Всё включено'
  },
  {
    id: 2,
    title: 'Культурная Италия',
    destination: 'Италия, Рим',
    type: 'excursion',
    price: 70000,
    oldPrice: null,
    discount: null,
    duration: 5,
    rating: 4.6,
    reviewsCount: 89,
    image: 'https://images.unsplash.com/photo-1552832230-c0197dd311b5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1096&q=80',
    hotelInfo: 'Отель 4★',
    food: 'Завтраки'
  },
  {
    id: 3,
    title: 'Горнолыжная Франция',
    destination: 'Франция, Куршевель',
    type: 'ski',
    price: 95000,
    oldPrice: 120000,
    discount: 20,
    duration: 10,
    rating: 4.9,
    reviewsCount: 72,
    image: 'https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1413&q=80',
    hotelInfo: 'Шале 5★',
    food: 'Полупансион'
  },
  {
    id: 4,
    title: 'Яркая Испания',
    destination: 'Испания, Барселона',
    type: 'excursion',
    price: 65000,
    oldPrice: null,
    discount: null,
    duration: 6,
    rating: 4.7,
    reviewsCount: 103,
    image: 'https://images.unsplash.com/photo-1558642084-fd07fae5282e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1036&q=80',
    hotelInfo: 'Отель 4★',
    food: 'Завтраки и ужины'
  },
  {
    id: 5,
    title: 'Острова Греции',
    destination: 'Греция, Санторини',
    type: 'beach',
    price: 85000,
    oldPrice: 90000,
    discount: 5,
    duration: 8,
    rating: 4.9,
    reviewsCount: 156,
    image: 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
    hotelInfo: 'Вилла 5★',
    food: 'Всё включено'
  },
  {
    id: 6,
    title: 'Термальная Венгрия',
    destination: 'Венгрия, Будапешт',
    type: 'wellness',
    price: 55000,
    oldPrice: null,
    discount: null,
    duration: 4,
    rating: 4.5,
    reviewsCount: 68,
    image: 'https://images.unsplash.com/photo-1551867633-194f125bddfa?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80',
    hotelInfo: 'СПА-отель 4★',
    food: 'Полупансион'
  },
  {
    id: 7,
    title: 'Экзотический Таиланд',
    destination: 'Таиланд, Пхукет',
    type: 'beach',
    price: 80000,
    oldPrice: 100000,
    discount: 20,
    duration: 12,
    rating: 4.7,
    reviewsCount: 132,
    image: 'https://images.unsplash.com/photo-1504214208698-ea1916a2195a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80',
    hotelInfo: 'Бунгало 5★',
    food: 'Завтраки'
  },
  {
    id: 8,
    title: 'Альпийская Австрия',
    destination: 'Австрия, Вена',
    type: 'excursion',
    price: 75000,
    oldPrice: null,
    discount: null,
    duration: 7,
    rating: 4.8,
    reviewsCount: 91,
    image: 'https://images.unsplash.com/photo-1523906921802-b5d2d899e93b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=715&q=80',
    hotelInfo: 'Отель 4★',
    food: 'Завтраки'
  },
  {
    id: 9,
    title: 'Приключения в Черногории',
    destination: 'Черногория, Будва',
    type: 'adventure',
    price: 60000,
    oldPrice: 65000,
    discount: 8,
    duration: 9,
    rating: 4.6,
    reviewsCount: 78,
    image: 'https://images.unsplash.com/photo-1525472095808-9c0a75b9d1c2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1469&q=80',
    hotelInfo: 'Отель 3★',
    food: 'Завтраки и ужины'
  },
  {
    id: 10,
    title: 'Египетские пирамиды',
    destination: 'Египет, Хургада',
    type: 'beach',
    price: 50000,
    oldPrice: 58000,
    discount: 15,
    duration: 10,
    rating: 4.4,
    reviewsCount: 145,
    image: 'https://images.unsplash.com/photo-1583248483201-2c9f2c7daa8c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
    hotelInfo: 'Отель 5★',
    food: 'Всё включено'
  },
  {
    id: 11,
    title: 'Загадочная Япония',
    destination: 'Япония, Токио',
    type: 'excursion',
    price: 120000,
    oldPrice: null,
    discount: null,
    duration: 14,
    rating: 4.9,
    reviewsCount: 67,
    image: 'https://images.unsplash.com/photo-1558862107-d49ef2a04d72?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80',
    hotelInfo: 'Отель 4★',
    food: 'Завтраки'
  },
  {
    id: 12,
    title: 'Солнечный Кипр',
    destination: 'Кипр, Айя-Напа',
    type: 'beach',
    price: 65000,
    oldPrice: 70000,
    discount: 7,
    duration: 7,
    rating: 4.7,
    reviewsCount: 112,
    image: 'https://images.unsplash.com/photo-1533664807229-8fc0c8cd42b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80',
    hotelInfo: 'Отель 4★',
    food: 'Всё включено'
  }
]);

// Функция для применения фильтров
const applyFilters = () => {
  currentPage.value = 1;
  // В реальном приложении здесь будет вызов API для получения отфильтрованных данных
};

// Отфильтрованные туры
const filteredTours = computed(() => {
  let result = [...tours.value];
  
  // Применение фильтров
  if (filters.value.destination) {
    result = result.filter(tour => tour.destination.toLowerCase().includes(filters.value.destination.toLowerCase()));
  }
  
  if (filters.value.type) {
    result = result.filter(tour => tour.type === filters.value.type);
  }
  
  if (filters.value.priceMin) {
    result = result.filter(tour => tour.price >= filters.value.priceMin);
  }
  
  if (filters.value.priceMax) {
    result = result.filter(tour => tour.price <= filters.value.priceMax);
  }
  
  if (filters.value.duration) {
    const [min, max] = filters.value.duration.split('-');
    if (max) {
      result = result.filter(tour => tour.duration >= parseInt(min) && tour.duration <= parseInt(max));
    } else if (min === '15+') {
      result = result.filter(tour => tour.duration >= 15);
    }
  }
  
  return result;
});

// Отсортированные туры
const sortedTours = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  
  let sorted = [...filteredTours.value];
  
  switch (sortOption.value) {
    case 'price_asc':
      sorted.sort((a, b) => a.price - b.price);
      break;
    case 'price_desc':
      sorted.sort((a, b) => b.price - a.price);
      break;
    case 'rating_desc':
      sorted.sort((a, b) => b.rating - a.rating);
      break;
    case 'duration_asc':
      sorted.sort((a, b) => a.duration - b.duration);
      break;
    case 'duration_desc':
      sorted.sort((a, b) => b.duration - a.duration);
      break;
  }
  
  return sorted.slice(start, end);
});

// Общее количество страниц
const totalPages = computed(() => Math.ceil(filteredTours.value.length / itemsPerPage));

// Функции пагинации
const goToPage = (page) => {
  currentPage.value = page;
};

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

// Функция форматирования валюты
const formatCurrency = (value) => {
  return new Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB', maximumFractionDigits: 0 }).format(value);
};
</script> 