<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Регистрация нового аккаунта
        </h2>
        <p class="mt-2 text-center text-sm text-gray-600">
          Или
          <NuxtLink to="/login" class="font-medium text-indigo-600 hover:text-indigo-500">
            войдите, если у вас уже есть аккаунт
          </NuxtLink>
        </p>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="handleRegister">
        <div v-if="errorMessage" class="rounded-md bg-red-50 p-4 mb-4">
          <div class="flex">
            <div class="ml-3">
              <h3 class="text-sm font-medium text-red-800">{{ errorMessage }}</h3>
            </div>
          </div>
        </div>
        
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="first-name" class="sr-only">Имя</label>
            <input
              id="first-name"
              name="first_name"
              type="text"
              required
              v-model="userData.first_name"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Имя"
            />
          </div>
          <div>
            <label for="last-name" class="sr-only">Фамилия</label>
            <input
              id="last-name"
              name="last_name"
              type="text"
              required
              v-model="userData.last_name"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Фамилия"
            />
          </div>
          <div>
            <label for="email-address" class="sr-only">Email</label>
            <input
              id="email-address"
              name="email"
              type="email"
              autocomplete="email"
              required
              v-model="userData.email"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Email"
            />
          </div>
          <div>
            <label for="phone" class="sr-only">Телефон</label>
            <input
              id="phone"
              name="phone"
              type="tel"
              v-model="userData.phone"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Телефон (необязательно)"
            />
          </div>
          <div>
            <label for="password" class="sr-only">Пароль</label>
            <input
              id="password"
              name="password"
              type="password"
              required
              v-model="userData.password"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Пароль"
            />
          </div>
          <div>
            <label for="confirm-password" class="sr-only">Подтверждение пароля</label>
            <input
              id="confirm-password"
              name="confirm_password"
              type="password"
              required
              v-model="confirmPassword"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Подтверждение пароля"
            />
          </div>
        </div>

        <div class="flex items-center">
          <input
            id="terms"
            name="terms"
            type="checkbox"
            required
            v-model="termsAccepted"
            class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
          />
          <label for="terms" class="ml-2 block text-sm text-gray-900">
            Я принимаю <a href="#" class="text-indigo-600 hover:text-indigo-500">условия использования</a> и <a href="#" class="text-indigo-600 hover:text-indigo-500">политику конфиденциальности</a>
          </label>
        </div>

        <div>
          <button
            type="submit"
            :disabled="loading || !termsAccepted || userData.password !== confirmPassword"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50"
          >
            <span v-if="loading" class="absolute left-0 inset-y-0 flex items-center pl-3">
              <!-- Spinner -->
              <svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            </span>
            <span v-else class="absolute left-0 inset-y-0 flex items-center pl-3">
              <!-- Heroicon name: solid/user-add -->
              <svg class="h-5 w-5 text-indigo-500 group-hover:text-indigo-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                <path d="M8 9a3 3 0 100-6 3 3 0 000 6zM8 11a6 6 0 016 6H2a6 6 0 016-6zM16 7a1 1 0 10-2 0v1h-1a1 1 0 100 2h1v1a1 1 0 102 0v-1h1a1 1 0 100-2h-1V7z" />
              </svg>
            </span>
            Зарегистрироваться
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue';
import { useAuthStore } from '~/store/auth';
import { storeToRefs } from 'pinia';

const authStore = useAuthStore();
const { loading, error } = storeToRefs(authStore);

const userData = reactive({
  first_name: '',
  last_name: '',
  email: '',
  phone: '',
  password: '',
});

const confirmPassword = ref('');
const termsAccepted = ref(false);
const errorMessage = ref('');

const router = useRouter();

const handleRegister = async () => {
  if (userData.password !== confirmPassword.value) {
    errorMessage.value = 'Пароли не совпадают';
    return;
  }
  
  const success = await authStore.register({ ...userData });
  
  if (success) {
    errorMessage.value = '';
    // Перенаправляем пользователя в личный кабинет
    router.push('/profile');
  } else {
    errorMessage.value = error.value || 'Ошибка при регистрации. Попробуйте еще раз.';
  }
};

// Если пользователь уже авторизован, перенаправляем его
onMounted(() => {
  if (authStore.isAuthenticated) {
    router.push('/profile');
  }
});
</script> 