from django.urls import path
from users import views

urlpatterns = [
    path('signup/', views.UserView.as_view()),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
