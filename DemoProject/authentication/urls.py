from django.urls import path
from .views import SignupView, LoginView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup-api'), 
     path('login/', LoginView.as_view(), name='login-api'),
]
