<template>
  <div class="bg-gray-50 min-h-screen">
    <!-- Верхний блок с заголовком -->
    <div class="bg-primary">
      <div class="max-w-7xl mx-auto px-4 py-16 sm:px-6 lg:px-8 lg:py-20">
        <div class="text-center">
          <h1 class="text-4xl font-extrabold text-white sm:text-5xl">Контакты</h1>
          <p class="max-w-3xl mt-4 mx-auto text-xl text-blue-100">
            Мы всегда рады ответить на ваши вопросы и помочь в организации путешествия
          </p>
        </div>
      </div>
    </div>
    
    <!-- Основной контент страницы -->
    <div class="section bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-5 gap-8">
          <!-- Левая колонка с контактной информацией -->
          <div class="lg:col-span-2">
            <div class="bg-gray-50 p-6 rounded-lg shadow-md">
              <h2 class="text-2xl font-bold text-gray-900 mb-6">Наши контакты</h2>
              
              <div class="space-y-6">
                <!-- Адрес -->
                <div class="flex">
                  <div class="flex-shrink-0">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                    </svg>
                  </div>
                  <div class="ml-4">
                    <h3 class="text-lg font-semibold text-gray-900">Адрес офиса</h3>
                    <p class="mt-1 text-gray-600">г. Москва, ул. Примерная, 123</p>
                    <p class="text-gray-600">Бизнес-центр "Горизонт", офис 45</p>
                  </div>
                </div>
                
                <!-- Телефоны -->
                <div class="flex">
                  <div class="flex-shrink-0">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                    </svg>
                  </div>
                  <div class="ml-4">
                    <h3 class="text-lg font-semibold text-gray-900">Телефоны</h3>
                    <p class="mt-1 text-gray-600">+7 (999) 123-45-67 - общие вопросы</p>
                    <p class="text-gray-600">+7 (999) 765-43-21 - отдел бронирования</p>
                  </div>
                </div>
                
                <!-- Email -->
                <div class="flex">
                  <div class="flex-shrink-0">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                    </svg>
                  </div>
                  <div class="ml-4">
                    <h3 class="text-lg font-semibold text-gray-900">Email</h3>
                    <p class="mt-1 text-gray-600">info@example.com - общие вопросы</p>
                    <p class="text-gray-600">support@example.com - техническая поддержка</p>
                  </div>
                </div>
                
                <!-- Режим работы -->
                <div class="flex">
                  <div class="flex-shrink-0">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                  </div>
                  <div class="ml-4">
                    <h3 class="text-lg font-semibold text-gray-900">Режим работы</h3>
                    <p class="mt-1 text-gray-600">Пн-Пт: 9:00 - 19:00</p>
                    <p class="text-gray-600">Сб: 10:00 - 17:00</p>
                    <p class="text-gray-600">Вс: выходной</p>
                  </div>
                </div>
              </div>
              
              <!-- Социальные сети -->
              <div class="mt-8">
                <h3 class="text-lg font-semibold text-gray-900 mb-3">Мы в социальных сетях</h3>
                <div class="flex space-x-4">
                  <a href="#" class="text-gray-600 hover:text-primary">
                    <span class="sr-only">Facebook</span>
                    <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                      <path fill-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" clip-rule="evenodd" />
                    </svg>
                  </a>
                  
                  <a href="#" class="text-gray-600 hover:text-primary">
                    <span class="sr-only">Instagram</span>
                    <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                      <path fill-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z" clip-rule="evenodd" />
                    </svg>
                  </a>
                  
                  <a href="#" class="text-gray-600 hover:text-primary">
                    <span class="sr-only">Twitter</span>
                    <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                      <path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" />
                    </svg>
                  </a>
                  
                  <a href="#" class="text-gray-600 hover:text-primary">
                    <span class="sr-only">Telegram</span>
                    <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                      <path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.96 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/>
                    </svg>
                  </a>
                </div>
              </div>
            </div>
          </div>
          
          <!-- Правая колонка с формой обратной связи -->
          <div class="lg:col-span-3">
            <div class="bg-white p-6 rounded-lg shadow-md">
              <h2 class="text-2xl font-bold text-gray-900 mb-6">Свяжитесь с нами</h2>
              
              <form @submit.prevent="submitForm" class="space-y-6">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label for="firstName" class="label">Имя</label>
                    <input type="text" id="firstName" v-model="form.firstName" class="input" required>
                  </div>
                  <div>
                    <label for="lastName" class="label">Фамилия</label>
                    <input type="text" id="lastName" v-model="form.lastName" class="input" required>
                  </div>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label for="email" class="label">Email</label>
                    <input type="email" id="email" v-model="form.email" class="input" required>
                  </div>
                  <div>
                    <label for="phone" class="label">Телефон</label>
                    <input type="tel" id="phone" v-model="form.phone" class="input" required>
                  </div>
                </div>
                
                <div>
                  <label for="subject" class="label">Тема</label>
                  <select id="subject" v-model="form.subject" class="input" required>
                    <option value="" disabled selected>Выберите тему обращения</option>
                    <option value="booking">Бронирование тура</option>
                    <option value="question">Вопрос о турах</option>
                    <option value="feedback">Отзыв о работе</option>
                    <option value="partnership">Сотрудничество</option>
                    <option value="other">Другое</option>
                  </select>
                </div>
                
                <div>
                  <label for="message" class="label">Сообщение</label>
                  <textarea id="message" v-model="form.message" rows="5" class="input" required></textarea>
                </div>
                
                <div class="flex items-start">
                  <div class="flex items-center h-5">
                    <input id="privacy" type="checkbox" v-model="form.privacy" class="h-4 w-4 text-primary focus:ring-primary border-gray-300 rounded" required>
                  </div>
                  <div class="ml-3 text-sm">
                    <label for="privacy" class="font-medium text-gray-700">Я согласен на обработку персональных данных</label>
                  </div>
                </div>
                
                <div v-if="formSubmitted" class="bg-green-50 p-4 rounded-md">
                  <div class="flex">
                    <div class="flex-shrink-0">
                      <svg class="h-5 w-5 text-green-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                      </svg>
                    </div>
                    <div class="ml-3">
                      <h3 class="text-sm font-medium text-green-800">Сообщение отправлено</h3>
                      <div class="mt-2 text-sm text-green-700">
                        <p>Спасибо за ваше обращение! Мы свяжемся с вами в ближайшее время.</p>
                      </div>
                    </div>
                  </div>
                </div>
                
                <div>
                  <button type="submit" class="btn-primary w-full">Отправить сообщение</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Карта -->
    <div class="section bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-8">
          <h2 class="text-3xl font-extrabold text-gray-900">Как нас найти</h2>
          <p class="mt-4 max-w-3xl mx-auto text-xl text-gray-500">
            Мы находимся в центре города, недалеко от метро
          </p>
        </div>
        
        <div class="h-96 rounded-lg overflow-hidden shadow-md">
          <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2245.5458990469594!2d37.618675815593!3d55.75639998055643!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46b54a50b315e573%3A0xa886bf5a3d9b2e68!2z0JzQvtGB0LrQvtCy0YHQutC40Lkg0JrRgNC10LzQu9GM!5e0!3m2!1sru!2sru!4v1616611324961!5m2!1sru!2sru" 
            width="100%" 
            height="100%" 
            style="border:0;" 
            allowfullscreen="" 
            loading="lazy">
          </iframe>
        </div>
      </div>
    </div>
    
    <!-- FAQ -->
    <div class="section bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <h2 class="text-3xl font-extrabold text-gray-900">Часто задаваемые вопросы</h2>
          <p class="mt-4 max-w-3xl mx-auto text-xl text-gray-500">
            Ответы на популярные вопросы о нашем агентстве
          </p>
        </div>
        
        <div class="mt-12 space-y-6">
          <div v-for="(faq, index) in faqs" :key="index" class="bg-gray-50 rounded-lg p-6">
            <button 
              @click="toggleFaq(index)"
              class="flex w-full text-left"
            >
              <span class="text-lg font-semibold text-gray-900">{{ faq.question }}</span>
              <span class="ml-auto">
                <svg v-if="faq.open" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7" />
                </svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </span>
            </button>
            <div v-if="faq.open" class="mt-4 text-gray-600">
              <p>{{ faq.answer }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// Состояние формы
const form = ref({
  firstName: '',
  lastName: '',
  email: '',
  phone: '',
  subject: '',
  message: '',
  privacy: false
});

const formSubmitted = ref(false);

// Отправка формы
function submitForm() {
  // В реальном приложении здесь был бы API запрос
  console.log('Форма отправлена:', form.value);
  
  // Показываем сообщение об успешной отправке
  formSubmitted.value = true;
  
  // Сбрасываем форму
  setTimeout(() => {
    form.value = {
      firstName: '',
      lastName: '',
      email: '',
      phone: '',
      subject: '',
      message: '',
      privacy: false
    };
    formSubmitted.value = false;
  }, 5000);
}

// FAQ
const faqs = ref([
  {
    question: 'Как забронировать тур?',
    answer: 'Для бронирования тура вы можете воспользоваться нашим сайтом, позвонить по телефону или посетить наш офис. При бронировании через сайт выберите интересующий вас тур, заполните форму бронирования и внесите предоплату. После этого с вами свяжется наш менеджер для подтверждения деталей.',
    open: true
  },
  {
    question: 'Какие способы оплаты вы принимаете?',
    answer: 'Мы принимаем различные способы оплаты, включая оплату банковской картой онлайн, банковский перевод и наличные в офисе. Для обеспечения бронирования требуется предоплата в размере 20%, полная оплата должна быть произведена не позднее чем за 14 дней до начала тура.',
    open: false
  },
  {
    question: 'Что делать, если мне нужно отменить тур?',
    answer: 'Условия отмены зависят от конкретного тура и времени до его начала. При отмене более чем за 30 дней до начала тура, возвращается 100% стоимости. При отмене за 15-30 дней взимается штраф 30%, за 7-14 дней - 50%, менее чем за 7 дней - 100%. В некоторых случаях возможен перенос тура или возврат в виде сертификата.',
    open: false
  },
  {
    question: 'Нужна ли мне страховка для путешествия?',
    answer: 'Да, страховка является обязательной для большинства международных поездок. Мы включаем базовую медицинскую страховку в стоимость тура, но рекомендуем приобрести дополнительную страховку от невыезда, которая защитит вас в случае непредвиденных обстоятельств, из-за которых вы не сможете отправиться в путешествие.',
    open: false
  },
  {
    question: 'Можно ли изменить даты тура после бронирования?',
    answer: 'Изменение дат возможно, но зависит от наличия мест на новые даты и политики отдельных поставщиков услуг (отелей, авиакомпаний). В случае изменения дат могут взиматься дополнительные сборы. Свяжитесь с нами как можно раньше, если вам необходимо изменить даты вашего тура.',
    open: false
  }
]);

function toggleFaq(index) {
  faqs.value[index].open = !faqs.value[index].open;
}
</script> 