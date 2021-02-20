
from django.contrib import admin
from django.urls import path
from bmi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('bmi',views.bmi, name='bmi'),
]
