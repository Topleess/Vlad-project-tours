<template>
  <div>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useAuthStore } from '~/store/auth';

// Инициализация аутентификации при загрузке приложения
onMounted(() => {
  const authStore = useAuthStore();
  authStore.initAuth();
});
</script>

<style>
/* Можно добавить глобальные стили */
body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
}

.text-primary {
  color: #4f46e5;
}

.bg-primary {
  background-color: #4f46e5;
}
</style> 