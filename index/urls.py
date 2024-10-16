from django.urls import path
from . import views

urlpatterns=[
    path('', views.home_page, name='home'),
    path('news/<int:pk>', views.news_page),
    path('news/<int:pk>', views.category_page)
]