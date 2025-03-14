import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: null,
    isAuthenticated: false,
    loading: false,
    error: null
  }),
  
  getters: {
    isAdmin: (state) => state.user?.is_admin === true,
    currentUser: (state) => state.user
  },
  
  actions: {
    async login(email, password) {
      this.loading = true;
      this.error = null;
      
      try {
        // Убрано для тестирования: вместо реального API используем моки
        /*
        const response = await fetch(`${useRuntimeConfig().public.apiBase}/auth/login`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
          body: new URLSearchParams({
            username: email, // OAuth2 использует username для email
            password: password,
          }),
        });
        
        const data = await response.json();
        
        if (!response.ok) {
          throw new Error(data.detail || 'Ошибка авторизации');
        }
        
        this.token = data.access_token;
        localStorage.setItem('token', data.access_token);
        */
        
        // Мок-данные для тестирования
        console.log('Вход с данными:', email, password);
        await new Promise(resolve => setTimeout(resolve, 500)); // Имитация задержки сети
        
        if (email === 'admin@example.com' && password === 'admin123') {
          this.token = 'mock_admin_token';
          localStorage.setItem('token', 'mock_admin_token');
          this.user = {
            id: 1,
            email: 'admin@example.com',
            first_name: 'Админ',
            last_name: 'Системы',
            is_admin: true
          };
        } else if (email === 'user@example.com' && password === 'user123') {
          this.token = 'mock_user_token';
          localStorage.setItem('token', 'mock_user_token');
          this.user = {
            id: 2,
            email: 'user@example.com',
            first_name: 'Тестовый',
            last_name: 'Пользователь',
            is_admin: false
          };
        } else {
          // Для тестирования позволим любому пользователю зайти
          this.token = 'mock_token_' + email;
          localStorage.setItem('token', 'mock_token_' + email);
          this.user = {
            id: Math.floor(Math.random() * 1000) + 10,
            email: email,
            first_name: 'Новый',
            last_name: 'Пользователь',
            is_admin: false
          };
        }
        
        this.isAuthenticated = true;
        
        return true;
      } catch (error) {
        this.error = error.message;
        return false;
      } finally {
        this.loading = false;
      }
    },
    
    async register(userData) {
      this.loading = true;
      this.error = null;
      
      try {
        // Убрано для тестирования: вместо реального API используем моки
        /*
        const response = await fetch(`${useRuntimeConfig().public.apiBase}/auth/signup`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(userData),
        });
        
        const data = await response.json();
        
        if (!response.ok) {
          throw new Error(data.detail || 'Ошибка при регистрации');
        }
        */
        
        // Мок-данные для тестирования
        console.log('Регистрация с данными:', userData);
        await new Promise(resolve => setTimeout(resolve, 500)); // Имитация задержки сети
        
        // После успешной регистрации, выполняем вход
        return await this.login(userData.email, userData.password);
      } catch (error) {
        this.error = error.message;
        return false;
      } finally {
        this.loading = false;
      }
    },
    
    async fetchUserInfo() {
      if (!this.token) return;
      
      try {
        // Убрано для тестирования: вместо реального API используем моки
        /*
        const response = await fetch(`${useRuntimeConfig().public.apiBase}/users/me`, {
          headers: {
            'Authorization': `Bearer ${this.token}`
          }
        });
        
        if (!response.ok) {
          throw new Error('Не удалось получить информацию о пользователе');
        }
        
        this.user = await response.json();
        */
        
        // Мок-данные - если пользователь уже установлен, используем его, иначе создаем по токену
        if (!this.user) {
          // Определяем пользователя по токену
          if (this.token === 'mock_admin_token') {
            this.user = {
              id: 1,
              email: 'admin@example.com',
              first_name: 'Админ',
              last_name: 'Системы',
              is_admin: true
            };
          } else if (this.token === 'mock_user_token') {
            this.user = {
              id: 2,
              email: 'user@example.com',
              first_name: 'Тестовый',
              last_name: 'Пользователь',
              is_admin: false
            };
          } else {
            // Для других токенов генерируем случайного пользователя
            this.user = {
              id: Math.floor(Math.random() * 1000) + 10,
              email: 'user' + Math.floor(Math.random() * 100) + '@example.com',
              first_name: 'Тестовый',
              last_name: 'Пользователь ' + Math.floor(Math.random() * 100),
              is_admin: false
            };
          }
        }
      } catch (error) {
        this.error = error.message;
        this.logout();
      }
    },
    
    logout() {
      this.user = null;
      this.token = null;
      this.isAuthenticated = false;
      localStorage.removeItem('token');
    },
    
    initAuth() {
      const token = localStorage.getItem('token');
      if (token) {
        this.token = token;
        this.fetchUserInfo();
        this.isAuthenticated = true;
      }
    }
  }
}); 