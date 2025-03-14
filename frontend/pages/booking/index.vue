<template>
  <div class="bg-gray-50 min-h-screen py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12">
        <h1 class="text-3xl font-extrabold text-gray-900 sm:text-4xl">Бронирование тура</h1>
        <p class="mt-3 max-w-2xl mx-auto text-xl text-gray-500">Заполните информацию для бронирования выбранного тура</p>
      </div>
      
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <!-- Основная форма бронирования -->
        <div class="lg:col-span-2">
          <div class="bg-white rounded-lg shadow-md p-6 mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-6">Данные бронирования</h2>
            
            <form @submit.prevent="submitBooking" class="space-y-6">
              <!-- Персональные данные -->
              <div>
                <h3 class="text-lg font-semibold text-gray-900 mb-4">Информация о туристах</h3>
                
                <div v-for="(tourist, index) in booking.tourists" :key="index" class="p-4 border border-gray-200 rounded-md mb-4">
                  <div class="flex justify-between items-center mb-4">
                    <h4 class="text-md font-semibold">Турист #{{ index + 1 }}</h4>
                    <button 
                      v-if="index > 0" 
                      type="button" 
                      @click="removeTourist(index)"
                      class="text-red-500 hover:text-red-700"
                    >
                      Удалить
                    </button>
                  </div>
                  
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                      <label class="label">Имя</label>
                      <input v-model="tourist.firstName" type="text" class="input" required>
                    </div>
                    <div>
                      <label class="label">Фамилия</label>
                      <input v-model="tourist.lastName" type="text" class="input" required>
                    </div>
                    <div>
                      <label class="label">Дата рождения</label>
                      <input v-model="tourist.birthDate" type="date" class="input" required>
                    </div>
                    <div>
                      <label class="label">Номер паспорта</label>
                      <input v-model="tourist.passport" type="text" class="input" required>
                    </div>
                  </div>
                </div>
                
                <button 
                  type="button" 
                  @click="addTourist" 
                  class="mt-2 inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                  </svg>
                  Добавить туриста
                </button>
              </div>
              
              <!-- Контактные данные -->
              <div>
                <h3 class="text-lg font-semibold text-gray-900 mb-4">Контактная информация</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label class="label">Электронная почта</label>
                    <input v-model="booking.contactInfo.email" type="email" class="input" required>
                  </div>
                  <div>
                    <label class="label">Телефон</label>
                    <input v-model="booking.contactInfo.phone" type="tel" class="input" required>
                  </div>
                </div>
              </div>
              
              <!-- Дополнительные услуги -->
              <div>
                <h3 class="text-lg font-semibold text-gray-900 mb-4">Дополнительные услуги</h3>
                
                <div class="space-y-3">
                  <div class="flex items-start">
                    <div class="flex items-center h-5">
                      <input v-model="booking.additionalServices.insurance" id="insurance" type="checkbox" class="h-4 w-4 text-primary focus:ring-primary border-gray-300 rounded">
                    </div>
                    <div class="ml-3 text-sm">
                      <label for="insurance" class="font-medium text-gray-700">Страховка от невыезда</label>
                      <p class="text-gray-500">Защита на случай отмены поездки (+5000 ₽)</p>
                    </div>
                  </div>
                  
                  <div class="flex items-start">
                    <div class="flex items-center h-5">
                      <input v-model="booking.additionalServices.transfer" id="transfer" type="checkbox" class="h-4 w-4 text-primary focus:ring-primary border-gray-300 rounded">
                    </div>
                    <div class="ml-3 text-sm">
                      <label for="transfer" class="font-medium text-gray-700">Индивидуальный трансфер</label>
                      <p class="text-gray-500">Персональный автомобиль с водителем (+2500 ₽)</p>
                    </div>
                  </div>
                  
                  <div>
                    <label class="label">Тип питания</label>
                    <select v-model="booking.additionalServices.meal" class="input">
                      <option value="AI">Всё включено (включено в стоимость)</option>
                      <option value="FB">Полный пансион (+3000 ₽)</option>
                      <option value="HB">Полупансион (-2000 ₽)</option>
                      <option value="BB">Только завтраки (-4000 ₽)</option>
                    </select>
                  </div>
                </div>
              </div>
              
              <!-- Комментарий к заказу -->
              <div>
                <label class="label">Комментарий к заказу</label>
                <textarea v-model="booking.comment" rows="3" class="input"></textarea>
              </div>
              
              <!-- Способ оплаты -->
              <div>
                <h3 class="text-lg font-semibold text-gray-900 mb-4">Способ оплаты</h3>
                
                <div class="space-y-3">
                  <div class="flex items-center">
                    <input v-model="booking.paymentMethod" id="card" type="radio" value="card" class="h-4 w-4 text-primary focus:ring-primary border-gray-300">
                    <label for="card" class="ml-3 block text-sm font-medium text-gray-700">Банковская карта</label>
                  </div>
                  
                  <div class="flex items-center">
                    <input v-model="booking.paymentMethod" id="bank" type="radio" value="bank" class="h-4 w-4 text-primary focus:ring-primary border-gray-300">
                    <label for="bank" class="ml-3 block text-sm font-medium text-gray-700">Банковский перевод</label>
                  </div>
                  
                  <div class="flex items-center">
                    <input v-model="booking.paymentMethod" id="cash" type="radio" value="cash" class="h-4 w-4 text-primary focus:ring-primary border-gray-300">
                    <label for="cash" class="ml-3 block text-sm font-medium text-gray-700">Наличные в офисе</label>
                  </div>
                </div>
              </div>
              
              <!-- Согласие с условиями -->
              <div class="flex items-start">
                <div class="flex items-center h-5">
                  <input v-model="booking.termsAccepted" id="terms" type="checkbox" class="h-4 w-4 text-primary focus:ring-primary border-gray-300 rounded" required>
                </div>
                <div class="ml-3 text-sm">
                  <label for="terms" class="font-medium text-gray-700">Я согласен с условиями бронирования и правилами отмены</label>
                </div>
              </div>
              
              <!-- Кнопки -->
              <div class="flex flex-col md:flex-row justify-end space-y-3 md:space-y-0 md:space-x-4">
                <NuxtLink :to="`/tours/${tourId}`" class="btn-outline">Вернуться к туру</NuxtLink>
                <button type="submit" class="btn-primary">Оформить бронирование</button>
              </div>
            </form>
          </div>
        </div>
        
        <!-- Сводка по бронированию -->
        <div class="lg:col-span-1">
          <div class="bg-white rounded-lg shadow-md p-6 sticky top-6">
            <h2 class="text-2xl font-bold text-gray-900 mb-6">Ваш заказ</h2>
            
            <div class="mb-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-2">{{ tour.name }}</h3>
              <p class="text-gray-600 mb-1">{{ tour.country }}, {{ tour.city }}</p>
              <p class="text-gray-600 mb-4">{{ formatDate(tour.start_date) }} - {{ formatDate(tour.end_date) }}</p>
              
              <div class="border-t border-gray-200 pt-4">
                <div class="flex justify-between py-2">
                  <span class="text-gray-600">{{ booking.tourists.length }} x {{ formatPrice(tour.price) }}</span>
                  <span class="font-semibold">{{ formatPrice(tour.price * booking.tourists.length) }} ₽</span>
                </div>
                
                <div v-if="booking.additionalServices.insurance" class="flex justify-between py-2">
                  <span class="text-gray-600">Страховка от невыезда</span>
                  <span class="font-semibold">5 000 ₽</span>
                </div>
                
                <div v-if="booking.additionalServices.transfer" class="flex justify-between py-2">
                  <span class="text-gray-600">Индивидуальный трансфер</span>
                  <span class="font-semibold">2 500 ₽</span>
                </div>
                
                <div v-if="booking.additionalServices.meal !== 'AI'" class="flex justify-between py-2">
                  <span class="text-gray-600">Изменение типа питания</span>
                  <span class="font-semibold">{{ getMealPriceDifference() }} ₽</span>
                </div>
                
                <div class="flex justify-between py-2 mt-4 border-t border-gray-200">
                  <span class="text-lg font-bold">Итого:</span>
                  <span class="text-lg font-bold text-primary">{{ formatPrice(calculateTotalPrice()) }} ₽</span>
                </div>
              </div>
            </div>
            
            <div class="bg-blue-50 p-4 rounded-lg">
              <h4 class="font-semibold text-blue-800 mb-2">Важная информация</h4>
              <ul class="text-sm text-blue-700 list-disc list-inside space-y-1">
                <li>Бронирование происходит после внесения предоплаты 20%</li>
                <li>Полная оплата должна быть произведена не позднее чем за 14 дней до вылета</li>
                <li>При отмене бронирования более чем за 30 дней до вылета возвращается 100% стоимости</li>
              </ul>
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

// Получаем ID тура из query-параметра
const tourId = computed(() => route.query.tourId);

// Состояние
const isLoading = ref(true);
const tour = ref({});

// Данные бронирования
const booking = ref({
  tourists: [
    {
      firstName: '',
      lastName: '',
      birthDate: '',
      passport: ''
    }
  ],
  contactInfo: {
    email: '',
    phone: ''
  },
  additionalServices: {
    insurance: false,
    transfer: false,
    meal: 'AI' // AI - все включено
  },
  comment: '',
  paymentMethod: 'card',
  termsAccepted: false
});

// Загрузка данных
onMounted(async () => {
  try {
    // В реальном приложении здесь был бы API запрос к бэкенду
    // Для примера используем моковые данные
    tour.value = {
      id: tourId.value,
      name: "Пляжный отдых в Анталии",
      description: "Насладитесь прекрасными пляжами и теплым морем на курортах Турции.",
      country: "Турция",
      city: "Анталия",
      start_date: "2023-07-15",
      end_date: "2023-07-22",
      price: 75000
    };
    
    isLoading.value = false;
  } catch (error) {
    console.error('Ошибка при загрузке данных:', error);
  }
});

// Методы
function formatDate(dateString) {
  const date = new Date(dateString);
  return new Intl.DateTimeFormat('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' }).format(date);
}

function formatPrice(price) {
  return new Intl.NumberFormat('ru-RU').format(price);
}

function addTourist() {
  booking.value.tourists.push({
    firstName: '',
    lastName: '',
    birthDate: '',
    passport: ''
  });
}

function removeTourist(index) {
  booking.value.tourists.splice(index, 1);
}

function getMealPriceDifference() {
  const mealPrices = {
    'AI': 0,      // Всё включено (базовая опция)
    'FB': 3000,   // Полный пансион (доплата)
    'HB': -2000,  // Полупансион (скидка)
    'BB': -4000   // Только завтраки (скидка)
  };
  
  return mealPrices[booking.value.additionalServices.meal];
}

function calculateTotalPrice() {
  let total = tour.value.price * booking.value.tourists.length;
  
  if (booking.value.additionalServices.insurance) {
    total += 5000;
  }
  
  if (booking.value.additionalServices.transfer) {
    total += 2500;
  }
  
  total += getMealPriceDifference();
  
  return total;
}

function submitBooking() {
  // В реальном приложении здесь логика отправки данных на сервер
  console.log('Данные бронирования:', {
    tourId: tourId.value,
    tourists: booking.value.tourists,
    contactInfo: booking.value.contactInfo,
    additionalServices: booking.value.additionalServices,
    comment: booking.value.comment,
    paymentMethod: booking.value.paymentMethod,
    totalPrice: calculateTotalPrice()
  });
  
  // Перенаправление на страницу подтверждения
  router.push(`/booking/confirmation?id=${Date.now()}`);
}
</script> 