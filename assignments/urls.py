
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.animals),
    path('porche/', views.porche),
    path('nike/', views.nike),
]
