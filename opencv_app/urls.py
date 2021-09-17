from django.contrib import admin
from django.urls import path
from opencv_app import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('finger_count',views.finger_count,name='finger_count'),
    path('finger_counts',views.finger_counts,name='finger_counts'),
    path('draw_virtual',views.draw_virtual,name='draw_virtual'),
    path('personal_trainer',views.personal_trainer,name='personal_trainer'),
    path('home',views.home,name='home'),

]
