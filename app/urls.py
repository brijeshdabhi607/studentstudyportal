from django.urls import path , include
from . import views
from .accountform import CustomLoginForm,CustomPasswordResetForm ,CustomPasswordSetForm
from django.contrib.auth.views import LoginView , LogoutView,PasswordResetView ,PasswordResetCompleteView,PasswordResetDoneView,PasswordResetConfirmView
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(form_class=CustomLoginForm,template_name='registration/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
]

urlpatterns +=[
    path('accounts/password_reset/',PasswordResetView.as_view(form_class=CustomPasswordResetForm),name="password_reset"),
    path('accounts/password_reset/done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(form_class=CustomPasswordSetForm),name='password_reset_confirm'),
    path('accounts/reset/done/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]