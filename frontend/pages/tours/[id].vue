<template>
  <div class="bg-gray-50 min-h-screen">
    <!-- Верхний блок с основной информацией о туре -->
    <div class="relative bg-blue-900 overflow-hidden">
      <div class="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:py-16 lg:px-8">
        <div class="relative z-10">
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <div>
              <span class="inline-block px-3 py-1 text-sm font-semibold bg-accent text-black rounded-full mb-4">{{ tour.type === 'beach' ? 'Пляжный отдых' : tour.type === 'excursion' ? 'Экскурсионный тур' : 'Горнолыжный курорт' }}</span>
              <h1 class="text-4xl font-extrabold text-white sm:text-5xl">{{ tour.name }}</h1>
              <div class="mt-3 flex items-center">
                <span class="text-xl text-white font-bold mr-2">{{ tour.country }}</span>
                <span class="text-lg text-gray-300">{{ tour.city }}</span>
              </div>
              <p class="mt-5 text-xl text-gray-300">{{ tour.description }}</p>
              <div class="mt-6 flex flex-wrap items-center gap-4">
                <div class="flex items-center">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-accent" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                  <span class="ml-2 text-white">{{ formatDate(tour.start_date) }} - {{ formatDate(tour.end_date) }}</span>
                </div>
                <div class="flex items-center">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-accent" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <span class="ml-2 text-white">{{ getDuration(tour.start_date, tour.end_date) }} дней</span>
                </div>
              </div>
            </div>

            <div class="bg-white p-6 rounded-lg shadow-lg">
              <div class="flex justify-between items-start">
                <div>
                  <h2 class="text-3xl font-bold text-gray-900">{{ formatPrice(tour.price) }} ₽</h2>
                  <p class="text-gray-500">на человека</p>
                </div>
                <div class="flex items-center bg-green-100 text-green-800 px-3 py-1 rounded-full">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                  В наличии
                </div>
              </div>
              
              <div class="mt-6 space-y-4">
                <div class="flex justify-between">
                  <span class="text-gray-700">Дата вылета:</span>
                  <span class="font-semibold">{{ formatDate(tour.start_date) }}</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-gray-700">Дата возвращения:</span>
                  <span class="font-semibold">{{ formatDate(tour.end_date) }}</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-gray-700">Количество ночей:</span>
                  <span class="font-semibold">{{ getDuration(tour.start_date, tour.end_date) - 1 }}</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-gray-700">Проживание:</span>
                  <span class="font-semibold">{{ tour.accommodation_details }}</span>
                </div>
              </div>
              
              <div class="mt-8">
                <form @submit.prevent="bookTour" class="space-y-4">
                  <div>
                    <label for="people" class="label">Количество человек</label>
                    <select id="people" v-model="booking.numPeople" class="input">
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                      <option value="5">5</option>
                    </select>
                  </div>
                  
                  <div>
                    <label for="room" class="label">Тип номера</label>
                    <select id="room" v-model="booking.roomType" class="input">
                      <option value="Standard">Стандартный</option>
                      <option value="Deluxe">Делюкс</option>
                      <option value="Suite">Люкс</option>
                    </select>
                  </div>
                  
                  <div class="pt-4">
                    <button type="submit" class="w-full btn-primary text-lg py-3">Забронировать</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="absolute inset-0 bg-gradient-to-t from-blue-900 opacity-70"></div>
    </div>
    
    <!-- Галерея фотографий -->
    <div class="section bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-extrabold text-gray-900 mb-8">Фотогалерея</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="(photo, index) in tourPhotos" :key="index" class="aspect-w-16 aspect-h-9 overflow-hidden rounded-lg shadow-md">
            <img :src="getPhotoUrl(photo)" :alt="`${tour.name} - фото ${index + 1}`" class="w-full h-full object-cover transform hover:scale-105 transition-transform duration-300 cursor-pointer" @click="openGallery(index)">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Программа тура -->
    <div class="section bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-extrabold text-gray-900 mb-8">Программа тура</h2>
        <div class="bg-white rounded-lg shadow-md p-6">
          <div v-for="(activity, day) in tourProgram" :key="day" class="mb-6 pb-6 border-b border-gray-200 last:border-b-0 last:mb-0 last:pb-0">
            <h3 class="text-xl font-bold text-gray-900 mb-2">День {{ day }}</h3>
            <p class="text-gray-700">{{ activity }}</p>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Что включено в тур -->
    <div class="section bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-extrabold text-gray-900 mb-8">Что включено в тур</h2>
        <div class="bg-gray-50 rounded-lg shadow-md p-6">
          <div class="prose max-w-none">
            <p>{{ tour.included_services }}</p>
          </div>
          
          <div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="flex items-start">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
              <span>Проживание в {{ tour.accommodation_details }}</span>
            </div>
            <div class="flex items-start">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
              <span>Авиаперелет туда и обратно</span>
            </div>
            <div class="flex items-start">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
              <span>Трансфер из/в аэропорт</span>
            </div>
            <div class="flex items-start">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
              <span>Страхование</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Отзывы -->
    <div class="section bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center mb-8">
          <h2 class="text-3xl font-extrabold text-gray-900">Отзывы туристов</h2>
          <button v-if="isAuthenticated" @click="showReviewForm = !showReviewForm" class="btn-primary">
            {{ showReviewForm ? 'Скрыть форму' : 'Оставить отзыв' }}
          </button>
        </div>
        
        <!-- Форма для добавления отзыва -->
        <div v-if="showReviewForm" class="bg-white rounded-lg shadow-md p-6 mb-8">
          <h3 class="text-xl font-bold text-gray-900 mb-4">Оставить отзыв</h3>
          <form @submit.prevent="submitReview" class="space-y-4">
            <div>
              <label for="rating" class="label">Оценка</label>
              <div class="flex space-x-2">
                <button 
                  v-for="star in 5" 
                  :key="star"
                  type="button"
                  @click="newReview.rating = star"
                  class="focus:outline-none"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" viewBox="0 0 20 20" :fill="newReview.rating >= star ? '#FBBF24' : '#E5E7EB'">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                </button>
              </div>
            </div>
            
            <div>
              <label for="comment" class="label">Комментарий</label>
              <textarea id="comment" v-model="newReview.comment" rows="4" class="input"></textarea>
            </div>
            
            <div>
              <button type="submit" class="btn-primary">Отправить отзыв</button>
            </div>
          </form>
        </div>
        
        <!-- Список отзывов -->
        <div v-if="reviews.length > 0" class="space-y-6">
          <div v-for="review in reviews" :key="review.id" class="bg-white p-6 rounded-lg shadow-md">
            <div class="flex items-center mb-4">
              <div class="flex-shrink-0">
                <div class="h-12 w-12 rounded-full bg-primary flex items-center justify-center text-white text-xl font-bold">
                  {{ review.user.first_name[0] }}{{ review.user.last_name[0] }}
                </div>
              </div>
              <div class="ml-4">
                <h4 class="text-lg font-bold text-gray-900">{{ review.user.first_name }} {{ review.user.last_name }}</h4>
                <div class="flex text-yellow-400">
                  <svg v-for="i in 5" :key="i" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" :fill="i <= review.rating ? 'currentColor' : '#E5E7EB'">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                </div>
              </div>
            </div>
            <p class="text-gray-600">
              "{{ review.comment }}"
            </p>
          </div>
        </div>
        
        <!-- Если нет отзывов -->
        <div v-else class="bg-white p-8 rounded-lg shadow-md text-center">
          <p class="text-gray-600 text-lg">У этого тура пока нет отзывов. Будьте первым, кто оставит отзыв!</p>
        </div>
      </div>
    </div>
    
    <!-- Похожие туры -->
    <div class="section bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-extrabold text-gray-900 mb-8">Похожие туры</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="similarTour in similarTours" :key="similarTour.id" class="card overflow-hidden flex flex-col">
            <div class="relative">
              <img :src="getPhotoUrl(similarTour.photos[0])" :alt="similarTour.name" class="w-full h-48 object-cover">
              <div class="absolute top-0 right-0 m-2 bg-white px-2 py-1 rounded-full text-sm font-semibold text-primary">
                {{ similarTour.type === 'beach' ? 'Пляжный' : similarTour.type === 'excursion' ? 'Экскурсия' : 'Горные лыжи' }}
              </div>
            </div>
            <div class="p-4 flex-grow">
              <h3 class="text-lg font-bold text-gray-900 mb-1">{{ similarTour.name }}</h3>
              <p class="text-gray-500 text-sm mb-2">{{ similarTour.country }}, {{ similarTour.city }}</p>
              <p class="text-sm text-gray-600 mb-4">{{ truncateDescription(similarTour.description, 100) }}</p>
              <div class="flex justify-between items-center">
                <span class="text-xl font-bold text-primary">{{ formatPrice(similarTour.price) }} ₽</span>
                <NuxtLink :to="`/tours/${similarTour.id}`" class="btn-outline">Подробнее</NuxtLink>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

// Состояние
const tourId = computed(() => route.params.id);
const isLoading = ref(true);
const tour = ref({});
const reviews = ref([]);
const similarTours = ref([]);
const isAuthenticated = ref(false); // В реальном приложении будет получаться из хранилища или API
const showReviewForm = ref(false);

// Данные для бронирования
const booking = ref({
  numPeople: 2,
  roomType: 'Standard'
});

// Данные для нового отзыва
const newReview = ref({
  rating: 5,
  comment: ''
});

// Преобразованные данные
const tourPhotos = computed(() => {
  if (!tour.value.photos) return [];
  return typeof tour.value.photos === 'string' ? JSON.parse(tour.value.photos) : tour.value.photos;
});

const tourProgram = computed(() => {
  if (!tour.value.tour_program) return {};
  return typeof tour.value.tour_program === 'string' ? JSON.parse(tour.value.tour_program) : tour.value.tour_program;
});

// Загрузка данных
onMounted(async () => {
  try {
    // В реальном приложении здесь были бы API запросы к бэкенду
    // Для примера используем моковые данные
    
    // Получение данных о туре
    tour.value = {
      id: tourId.value,
      name: "Пляжный отдых в Анталии",
      description: "Насладитесь прекрасными пляжами и теплым морем на курортах Турции. В стоимость включены: перелет, трансфер, проживание в отеле 5* по системе «Все включено».",
      country: "Турция",
      city: "Анталия",
      start_date: "2023-07-15",
      end_date: "2023-07-22",
      price: 75000,
      photos: ["turkey1.jpg", "turkey2.jpg", "turkey3.jpg"],
      type: "beach",
      tour_program: {
        "1": "Прибытие, заселение в отель, приветственный ужин",
        "2": "Отдых на пляже, вечерняя анимация",
        "3": "Экскурсия в старый город",
        "4-6": "Свободное время, отдых на пляже",
        "7": "Прощальный ужин",
        "8": "Выезд из отеля, трансфер в аэропорт"
      },
      accommodation_details: "Отель 5*, номер Deluxe с видом на море, все включено",
      included_services: "Перелет, трансфер, проживание, питание по системе «Все включено», страховка"
    };
    
    // Получение отзывов о туре
    reviews.value = [
      {
        id: 1,
        user: {
          first_name: "Анна",
          last_name: "Смирнова"
        },
        rating: 5,
        comment: "Отличный отель, прекрасный сервис, чистый пляж. Очень понравилось!"
      }
    ];
    
    // Получение похожих туров
    similarTours.value = [
      {
        id: 2,
        name: "Классическая Италия",
        description: "Увлекательное путешествие по историческим городам Италии. Вы посетите Рим, Флоренцию и Венецию, увидите главные достопримечательности и погрузитесь в атмосферу итальянской культуры.",
        country: "Италия",
        city: "Рим, Флоренция, Венеция",
        price: 95000,
        photos: ["italy1.jpg"],
        type: "excursion"
      },
      {
        id: 3,
        name: "Горнолыжный отдых в Альпах",
        description: "Потрясающий отдых на лучших трассах французских Альп. Идеально подходит как для начинающих, так и для опытных лыжников.",
        country: "Франция",
        city: "Шамони",
        price: 120000,
        photos: ["ski1.jpg"],
        type: "ski"
      }
    ];
    
    isLoading.value = false;
  } catch (error) {
    console.error('Ошибка при загрузке данных:', error);
  }
});

// Методы
function formatDate(dateString) {
  if (!dateString) return '';
  
  try {
    const date = new Date(dateString);
    if (isNaN(date.getTime())) {
      console.error('Недопустимое значение даты:', dateString);
      return 'Дата не указана';
    }
    return new Intl.DateTimeFormat('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' }).format(date);
  } catch (error) {
    console.error('Ошибка при форматировании даты:', error);
    return 'Дата не указана';
  }
}

function getDuration(startDate, endDate) {
  try {
    const start = new Date(startDate);
    const end = new Date(endDate);
    
    if (isNaN(start.getTime()) || isNaN(end.getTime())) {
      return 0;
    }
    
    return Math.round((end - start) / (1000 * 60 * 60 * 24)) + 1;
  } catch (error) {
    console.error('Ошибка при расчете продолжительности:', error);
    return 0;
  }
}

function formatPrice(price) {
  return new Intl.NumberFormat('ru-RU').format(price);
}

function getPhotoUrl(photo) {
  // В реальном приложении здесь логика получения URL фотографии
  return `https://picsum.photos/seed/${photo}/800/600`;
}

function truncateDescription(description, length) {
  if (description.length <= length) return description;
  return description.substring(0, length) + '...';
}

function openGallery(index) {
  // Здесь логика открытия галереи фотографий
  console.log('Открыть галерею с индекса:', index);
}

function bookTour() {
  // В реальном приложении здесь логика бронирования тура
  console.log('Бронирование тура:', {
    tourId: tourId.value,
    numPeople: booking.value.numPeople,
    roomType: booking.value.roomType,
    totalPrice: tour.value.price * booking.value.numPeople
  });
  
  // Перенаправление на страницу бронирования
  router.push(`/booking?tourId=${tourId.value}`);
}

function submitReview() {
  // В реальном приложении здесь логика отправки отзыва
  console.log('Отправка отзыва:', {
    tourId: tourId.value,
    rating: newReview.value.rating,
    comment: newReview.value.comment
  });
  
  // Добавляем отзыв в список (в реальном приложении это делал бы сервер)
  reviews.value.push({
    id: reviews.value.length + 1,
    user: {
      first_name: "Текущий",
      last_name: "Пользователь"
    },
    rating: newReview.value.rating,
    comment: newReview.value.comment
  });
  
  // Сбрасываем форму
  newReview.value = {
    rating: 5,
    comment: ''
  };
  
  showReviewForm.value = false;
}
</script> 