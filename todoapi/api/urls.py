from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('auth/', obtain_auth_token),
    path('login-test/', views.apiLoginTest),
    path('register/', views.UserCreateAPIView.as_view()),
    path('create/', views.TaskCreateView.as_view()),
    path('list/', views.TaskList),
    path('detail/<int:pk>', views.TaskRetriveUpdateDestroyView.as_view()),
]