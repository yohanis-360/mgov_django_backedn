from django.urls import path
from .views import UserRegistration, DeveloperRegistration, CustomLoginView,send_otp,verify_otp

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user_register'),
    path('developer/register/', DeveloperRegistration.as_view(), name='developer_register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path("send-otp/", send_otp, name="send_otp"),
    path("verify-otp/", verify_otp, name="verify_otp"),
]
