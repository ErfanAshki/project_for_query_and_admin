from django.urls import path

from . import views

urlpatterns = [
    path('shop/<some>/', views.some_view, name='view'),

]