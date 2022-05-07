from django.urls import path, include
from exam import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/quiz/', views.Quiz_List.as_view()),
    path('api/quiz/<int:pk>', views.Quiz_pk.as_view()),
    path('api/question/', views.Question_List.as_view()),
    path('api/questionExam/<int:pk>', views.QuestionExam_List.as_view()),
    path('api/question/<int:pk>', views.Question_pk.as_view()),
    path('api/exam/', views.Answer_List.as_view()),
    path('api/exam/<int:pk>', views.Answer_pk.as_view()),
    path('api/profile/', views.Profile_List.as_view()),
    path('api/profile/<int:pk>', views.Profile_pk.as_view()),
    path('api/login/', obtain_auth_token, name="obtain_auth_token"),
    path('api/users/', views.User_List.as_view()),
    path('api/users_result/<int:pk>', views.User_result_pk.as_view()),
    path('api/test/<int:user_id>', views.Fun.as_view()),




]
