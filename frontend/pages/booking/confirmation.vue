<template>
  <div class="bg-gray-50 min-h-screen py-12">
    <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-white rounded-lg shadow-lg overflow-hidden">
        <!-- Верхняя часть с подтверждением -->
        <div class="bg-green-600 px-6 py-8 text-center">
          <div class="mx-auto flex items-center justify-center h-16 w-16 rounded-full bg-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <h1 class="mt-4 text-3xl font-extrabold text-white">Бронирование подтверждено!</h1>
          <p class="mt-2 text-lg text-green-100">Ваш номер заказа: {{ bookingId }}</p>
        </div>
        
        <!-- Информация о бронировании -->
        <div class="px-6 py-8">
          <div class="text-center mb-8">
            <p class="text-gray-500">Мы отправили детали вашего бронирования на адрес</p>
            <p class="text-lg font-semibold">{{ booking.email }}</p>
          </div>
          
          <h2 class="text-xl font-bold text-gray-900 mb-4">Детали бронирования</h2>
          
          <div class="border rounded-lg overflow-hidden">
            <div class="px-4 py-5 bg-gray-50 border-b">
              <div class="flex justify-between items-center">
                <h3 class="text-lg font-semibold text-gray-900">{{ tour.name }}</h3>
                <span class="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm font-semibold">Подтверждено</span>
              </div>
            </div>
            <div class="p-4 space-y-3">
              <div class="flex justify-between">
                <span class="text-gray-600">Направление:</span>
                <span class="font-semibold">{{ tour.country }}, {{ tour.city }}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-gray-600">Даты:</span>
                <span class="font-semibold">{{ formatDate(tour.start_date) }} - {{ formatDate(tour.end_date) }}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-gray-600">Количество туристов:</span>
                <span class="font-semibold">{{ booking.numPeople }} чел.</span>
              </div>
              <div class="flex justify-between">
                <span class="text-gray-600">Проживание:</span>
                <span class="font-semibold">{{ tour.accommodation }}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-gray-600">Тип питания:</span>
                <span class="font-semibold">{{ getMealType() }}</span>
              </div>
              
              <div class="pt-3 mt-3 border-t">
                <div class="flex justify-between">
                  <span class="text-gray-600">Стоимость:</span>
                  <span class="font-semibold">{{ formatPrice(booking.totalPrice) }} ₽</span>
                </div>
                <div class="flex justify-between mt-1">
                  <span class="text-gray-600">Предоплата (20%):</span>
                  <span class="font-semibold">{{ formatPrice(booking.totalPrice * 0.2) }} ₽</span>
                </div>
                <div class="flex justify-between text-primary mt-1">
                  <span class="font-semibold">Оставшаяся сумма:</span>
                  <span class="font-semibold">{{ formatPrice(booking.totalPrice * 0.8) }} ₽</span>
                </div>
              </div>
            </div>
          </div>
          
          <div class="mt-8">
            <h2 class="text-xl font-bold text-gray-900 mb-4">Что дальше?</h2>
            
            <div class="bg-blue-50 rounded-lg p-4 mb-6">
              <h3 class="font-semibold text-blue-800 mb-2">Следующие шаги</h3>
              <ol class="space-y-2 text-sm text-blue-700 list-decimal list-inside">
                <li>В ближайшее время с вами свяжется наш менеджер для подтверждения деталей</li>
                <li>Внесите предоплату в размере 20% в течение 48 часов для подтверждения бронирования</li>
                <li>За 2 недели до поездки необходимо внести полную оплату</li>
                <li>За 3 дня до вылета вы получите ваучер и все необходимые документы</li>
              </ol>
            </div>
            
            <div class="bg-yellow-50 rounded-lg p-4">
              <h3 class="font-semibold text-yellow-800 mb-2">Важно</h3>
              <p class="text-sm text-yellow-700">Пожалуйста, проверьте действительность ваших паспортов. Для международных поездок паспорт должен быть действителен не менее 6 месяцев с даты выезда из страны пребывания.</p>
            </div>
          </div>
          
          <div class="flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-4 mt-8">
            <button @click="printBooking" class="btn-outline flex items-center justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z" />
              </svg>
              Распечатать
            </button>
            <NuxtLink to="/account/bookings" class="btn-primary flex items-center justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4" />
              </svg>
              Мои бронирования
            </NuxtLink>
            <NuxtLink to="/" class="btn-outline flex items-center justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
              </svg>
              На главную
            </NuxtLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

// Получаем ID бронирования из query-параметра
const bookingId = computed(() => route.query.id || 'BK' + Math.floor(100000 + Math.random() * 900000));

// Состояние
const tour = ref({
  name: "Пляжный отдых в Анталии",
  country: "Турция",
  city: "Анталия",
  start_date: "2023-07-15",
  end_date: "2023-07-22",
  accommodation: "Отель 5*, номер Deluxe с видом на море"
});

const booking = ref({
  email: "user@example.com",
  numPeople: 2,
  totalPrice: 85000,
  mealType: "AI", // AI - все включено
  paymentMethod: "card"
});

// Методы
function formatDate(dateString) {
  const date = new Date(dateString);
  return new Intl.DateTimeFormat('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' }).format(date);
}

function formatPrice(price) {
  return new Intl.NumberFormat('ru-RU').format(price);
}

function getMealType() {
  const mealTypes = {
    'AI': 'Всё включено',
    'FB': 'Полный пансион',
    'HB': 'Полупансион',
    'BB': 'Только завтраки'
  };
  
  return mealTypes[booking.value.mealType] || 'Всё включено';
}

function printBooking() {
  window.print();
}

// В реальном приложении здесь был бы запрос к API для получения данных бронирования
onMounted(() => {
  // Имитация загрузки данных
  console.log(`Загрузка данных бронирования ${bookingId.value}`);
});
</script>

<style>
@media print {
  body * {
    visibility: hidden;
  }
  .bg-green-600 {
    background-color: #059669 !important;
    -webkit-print-color-adjust: exact;
    color-adjust: exact;
  }
  .bg-white, .bg-white * {
    visibility: visible;
  }
  .bg-white {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
  }
}
</style> 