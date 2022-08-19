from django.urls import path

from . import views
# here to direct paths to the functions in views
urlpatterns = [
    path('', views.postsign, name='login'),
    path('home/', views.home, name="home"),
    path('logout/', views.user_logout, name='login'),
    path('register/', views.register, name="register"),
]
