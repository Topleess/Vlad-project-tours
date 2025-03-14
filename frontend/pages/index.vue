<template>
  <div>
    <!-- Первый блок - Баннер -->
    <div class="relative bg-blue-900 overflow-hidden">
      <div class="max-w-7xl mx-auto">
        <div class="relative z-10 pb-8 bg-blue-900 sm:pb-16 md:pb-20 lg:max-w-2xl lg:w-full lg:pb-28 xl:pb-32">
          <div class="pt-10 mx-auto max-w-7xl px-4 sm:pt-12 sm:px-6 md:pt-16 lg:pt-20 lg:px-8 xl:pt-28">
            <div class="sm:text-center lg:text-left">
              <h1 class="text-4xl tracking-tight font-extrabold text-white sm:text-5xl md:text-6xl">
                <span class="block">Путешествуйте с</span>
                <span class="block text-accent">нашим агентством</span>
              </h1>
              <p class="mt-3 text-base text-gray-300 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0">
                Откройте для себя мир путешествий. Мы предлагаем лучшие туры по всему миру: пляжный отдых, горнолыжные курорты, экскурсионные туры и многое другое.
              </p>
              <div class="mt-5 sm:mt-8 sm:flex sm:justify-center lg:justify-start">
                <div class="rounded-md shadow">
                  <NuxtLink to="/tours" class="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-black bg-accent hover:bg-accent-dark md:py-4 md:text-lg md:px-10">
                    Выбрать тур
                  </NuxtLink>
                </div>
                <div class="mt-3 sm:mt-0 sm:ml-3">
                  <NuxtLink to="/about" class="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-700 hover:bg-blue-800 md:py-4 md:text-lg md:px-10">
                    О нас
                  </NuxtLink>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="hidden lg:block lg:absolute lg:inset-y-0 lg:right-0 lg:w-1/2">
        <img class="h-56 w-full object-cover sm:h-72 md:h-96 lg:w-full lg:h-full" src="https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1350&q=80" alt="Путешествия">
      </div>
    </div>

    <!-- Второй блок - Популярные направления -->
    <div class="section bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <h2 class="text-3xl font-extrabold text-gray-900 sm:text-4xl">
            Популярные направления
          </h2>
          <p class="mt-3 max-w-2xl mx-auto text-xl text-gray-500 sm:mt-4">
            Выбирайте из самых востребованных туристических направлений
          </p>
        </div>

        <div class="mt-12 grid gap-8 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
          <!-- Карточка направления 1 -->
          <div class="card group">
            <div class="relative h-80 w-full overflow-hidden bg-white">
              <img src="https://images.unsplash.com/photo-1606046604972-77cc76aee944?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1935&q=80" alt="Турция" class="w-full h-full object-cover object-center group-hover:opacity-75">
              <div class="absolute inset-0 bg-gradient-to-t from-black opacity-70"></div>
              <div class="absolute bottom-0 left-0 p-6">
                <h3 class="text-2xl font-bold text-white">Турция</h3>
                <p class="text-sm text-gray-200 mt-1">Пляжный отдых, отели "всё включено"</p>
                <NuxtLink to="/tours" class="inline-block mt-3 px-4 py-2 bg-accent text-black rounded-md hover:bg-accent-dark">Смотреть туры</NuxtLink>
              </div>
            </div>
          </div>

          <!-- Карточка направления 2 -->
          <div class="card group">
            <div class="relative h-80 w-full overflow-hidden bg-white">
              <img src="https://images.unsplash.com/photo-1515542622106-78bda8ba0e5b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1950&q=80" alt="Италия" class="w-full h-full object-cover object-center group-hover:opacity-75">
              <div class="absolute inset-0 bg-gradient-to-t from-black opacity-70"></div>
              <div class="absolute bottom-0 left-0 p-6">
                <h3 class="text-2xl font-bold text-white">Италия</h3>
                <p class="text-sm text-gray-200 mt-1">Экскурсии, история, культура</p>
                <NuxtLink to="/tours" class="inline-block mt-3 px-4 py-2 bg-accent text-black rounded-md hover:bg-accent-dark">Смотреть туры</NuxtLink>
              </div>
            </div>
          </div>

          <!-- Карточка направления 3 -->
          <div class="card group">
            <div class="relative h-80 w-full overflow-hidden bg-white">
              <img src="https://images.unsplash.com/photo-1605540436563-5bca919ae766?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1969&q=80" alt="Франция" class="w-full h-full object-cover object-center group-hover:opacity-75">
              <div class="absolute inset-0 bg-gradient-to-t from-black opacity-70"></div>
              <div class="absolute bottom-0 left-0 p-6">
                <h3 class="text-2xl font-bold text-white">Франция</h3>
                <p class="text-sm text-gray-200 mt-1">Горнолыжные курорты, активный отдых</p>
                <NuxtLink to="/tours" class="inline-block mt-3 px-4 py-2 bg-accent text-black rounded-md hover:bg-accent-dark">Смотреть туры</NuxtLink>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Третий блок - Преимущества -->
    <div class="section bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <h2 class="text-3xl font-extrabold text-gray-900 sm:text-4xl">
            Почему выбирают нас
          </h2>
          <p class="mt-3 max-w-2xl mx-auto text-xl text-gray-500 sm:mt-4">
            Мы предлагаем лучший сервис для наших клиентов
          </p>
        </div>

        <div class="mt-12 grid gap-8 grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
          <!-- Преимущество 1 -->
          <div class="text-center">
            <div class="flex items-center justify-center h-16 w-16 rounded-full bg-primary mx-auto">
              <i class="text-white text-2xl fas fa-money-bill-wave"></i>
            </div>
            <h3 class="mt-6 text-lg font-medium text-gray-900">Выгодные цены</h3>
            <p class="mt-2 text-base text-gray-500">
              Мы сотрудничаем напрямую с отелями и предлагаем лучшие цены на туры.
            </p>
          </div>

          <!-- Преимущество 2 -->
          <div class="text-center">
            <div class="flex items-center justify-center h-16 w-16 rounded-full bg-primary mx-auto">
              <i class="text-white text-2xl fas fa-headset"></i>
            </div>
            <h3 class="mt-6 text-lg font-medium text-gray-900">Поддержка 24/7</h3>
            <p class="mt-2 text-base text-gray-500">
              Наша служба поддержки готова помочь вам в любое время дня и ночи.
            </p>
          </div>

          <!-- Преимущество 3 -->
          <div class="text-center">
            <div class="flex items-center justify-center h-16 w-16 rounded-full bg-primary mx-auto">
              <i class="text-white text-2xl fas fa-shield-alt"></i>
            </div>
            <h3 class="mt-6 text-lg font-medium text-gray-900">Гарантия безопасности</h3>
            <p class="mt-2 text-base text-gray-500">
              Мы гарантируем безопасность ваших платежей и личных данных.
            </p>
          </div>

          <!-- Преимущество 4 -->
          <div class="text-center">
            <div class="flex items-center justify-center h-16 w-16 rounded-full bg-primary mx-auto">
              <i class="text-white text-2xl fas fa-star"></i>
            </div>
            <h3 class="mt-6 text-lg font-medium text-gray-900">Положительные отзывы</h3>
            <p class="mt-2 text-base text-gray-500">
              Тысячи довольных клиентов выбирают нас снова и снова.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Четвертый блок - Отзывы клиентов -->
    <div class="section bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <h2 class="text-3xl font-extrabold text-gray-900 sm:text-4xl">
            Отзывы наших клиентов
          </h2>
          <p class="mt-3 max-w-2xl mx-auto text-xl text-gray-500 sm:mt-4">
            Узнайте, что говорят о нас те, кто уже воспользовался нашими услугами
          </p>
        </div>

        <div class="mt-12 grid gap-8 grid-cols-1 md:grid-cols-3">
          <!-- Отзыв 1 -->
          <div class="bg-white p-6 rounded-lg shadow-md">
            <div class="flex items-center mb-4">
              <div class="flex-shrink-0">
                <img class="h-12 w-12 rounded-full" src="https://randomuser.me/api/portraits/women/32.jpg" alt="Клиент">
              </div>
              <div class="ml-4">
                <h4 class="text-lg font-bold text-gray-900">Анна Смирнова</h4>
                <div class="flex text-yellow-400">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                </div>
              </div>
            </div>
            <p class="text-gray-600">
              "Отличное агентство! Всё было организовано идеально. Отдыхали семьей в Турции, остались очень довольны. Обязательно обратимся еще раз."
            </p>
          </div>

          <!-- Отзыв 2 -->
          <div class="bg-white p-6 rounded-lg shadow-md">
            <div class="flex items-center mb-4">
              <div class="flex-shrink-0">
                <img class="h-12 w-12 rounded-full" src="https://randomuser.me/api/portraits/men/46.jpg" alt="Клиент">
              </div>
              <div class="ml-4">
                <h4 class="text-lg font-bold text-gray-900">Иван Петров</h4>
                <div class="flex text-yellow-400">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-300" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                </div>
              </div>
            </div>
            <p class="text-gray-600">
              "Большое спасибо за организацию тура в Италию! Очень насыщенная программа, интересные экскурсии. Всё было на высшем уровне."
            </p>
          </div>

          <!-- Отзыв 3 -->
          <div class="bg-white p-6 rounded-lg shadow-md">
            <div class="flex items-center mb-4">
              <div class="flex-shrink-0">
                <img class="h-12 w-12 rounded-full" src="https://randomuser.me/api/portraits/women/68.jpg" alt="Клиент">
              </div>
              <div class="ml-4">
                <h4 class="text-lg font-bold text-gray-900">Екатерина Иванова</h4>
                <div class="flex text-yellow-400">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                </div>
              </div>
            </div>
            <p class="text-gray-600">
              "Это было потрясающее путешествие! Горнолыжный курорт во Франции оказался именно таким, как мы и мечтали. Спасибо за прекрасно организованный отдых!"
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Пятый блок - CTA (призыв к действию) -->
    <div class="bg-primary">
      <div class="max-w-7xl mx-auto px-4 py-16 sm:px-6 lg:px-8 lg:py-20">
        <div class="lg:grid lg:grid-cols-2 lg:gap-8 items-center">
          <div>
            <h2 class="text-3xl font-extrabold text-white sm:text-4xl">
              Готовы отправиться в путешествие?
            </h2>
            <p class="mt-3 max-w-md text-lg text-blue-200">
              Забронируйте свой следующий тур уже сегодня и получите скидку 10% на любой тур при первом бронировании.
            </p>
            <div class="mt-8">
              <div class="inline-flex rounded-md shadow">
                <NuxtLink to="/tours" class="inline-flex items-center justify-center px-5 py-3 border border-transparent text-base font-medium rounded-md text-primary bg-white hover:bg-gray-100">
                  Подобрать тур
                </NuxtLink>
              </div>
              <div class="ml-3 inline-flex">
                <NuxtLink to="/contacts" class="inline-flex items-center justify-center px-5 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-800 hover:bg-blue-700">
                  Связаться с нами
                </NuxtLink>
              </div>
            </div>
          </div>
          <div class="mt-8 lg:mt-0">
            <div class="bg-white p-6 rounded-lg shadow-lg">
              <h3 class="text-2xl font-bold text-gray-900 mb-4">Подписаться на рассылку</h3>
              <p class="text-gray-600 mb-4">Получайте лучшие предложения и скидки на ваш email</p>
              <div class="flex flex-col space-y-4">
                <input type="text" placeholder="Ваше имя" class="input">
                <input type="email" placeholder="Ваш email" class="input">
                <button class="btn-primary">Подписаться</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// Здесь можно добавить логику для главной страницы
</script> 