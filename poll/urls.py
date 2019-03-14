from django.urls import path ,include
from . import views


app_name  = 'poll'
urlpatterns = [
    path('', views.index.as_view(), name = 'index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/result/', views.result, name='result'),
    path('<int:question_id>/vots/', views.vote, name='vots'),
]
