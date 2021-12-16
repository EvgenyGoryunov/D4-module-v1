# импортируем класс-представление для аутентификации LoginView и для выхода из системы — Logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import BaseRegisterView
# импорт для нашей кнопки проверки или добавления польз в группу премиум
from .views import upgrade_me

urlpatterns = [
    path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),

    # При выходе с сайта (кнопку, которую мы создали раньше в шаблоне index.html) Django
    # перенаправит пользователя на страницу, указанную в параметре template_name класса LogoutView
    path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),

    # модифицировать файл конфигурации URL, чтобы Django мог увидеть представление, которое расширяет кол-во
    # полей при регистрации пользователя
    path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup'),

    # для кнопки премиум
    path('upgrade/', upgrade_me, name='upgrade')
]
