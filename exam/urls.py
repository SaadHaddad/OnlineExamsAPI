from django.urls import path, include
from exam import views
from exam import views


urlpatterns = [
    path('api/quiz/', views.Quiz_List.as_view()),
    path('api/quiz/<int:pk>', views.Quiz_pk.as_view()),
    path('api/question/', views.Question_List.as_view()),
    path('api/question/<int:pk>', views.Question_pk.as_view()),
    path('api/exam/', views.Answer_List.as_view()),
    path('api/exam/<int:pk>', views.Answer_pk.as_view()),
    path('api/profile/', views.Profile_List.as_view()),
    path('api/profile/<int:pk>', views.Profile_pk.as_view()),


]
