import { useAuthStore } from '~/store/auth';

export default defineNuxtPlugin((nuxtApp) => {
  // Установка плагина только на клиенте
  if (process.client) {
    const authStore = useAuthStore();
    
    // Инициализация аутентификации при загрузке приложения
    authStore.initAuth();
    
    // Добавление middleware для защищенных маршрутов
    addRouteMiddleware('auth', async (to) => {
      // Проверка сохраненного токена в localStorage и восстановление сессии если токен есть
      const authStore = useAuthStore();
      
      // Если пытаемся зайти на защищенный маршрут, но не авторизованы
      if (to.meta.requiresAuth && !authStore.isAuthenticated) {
        return navigateTo('/login', { redirectCode: 401 });
      }
      
      // Если пытаемся зайти на страницу, требующую административные права, но не админ
      if (to.meta.requiresAdmin && !authStore.isAdmin) {
        return navigateTo('/', { redirectCode: 403 });
      }
    }, { global: true });
  }
}); 