from django.urls import path

from accounts.views import send_otp, verified_otp


urlpatterns = [
    path('otp/', send_otp),
    path('verified-otp/', verified_otp),
]
