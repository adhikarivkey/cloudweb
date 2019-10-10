from django.urls import path
from django.contrib.auth.views import LogoutView,LoginView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

app_name = 'account'


urlpatterns = [
    path('signup/',views.SignUpPage.as_view(),name='signup'),
    path('login/',LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='reset/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='reset/password_reset_done.html'), name='password_reset_done'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='reset/password_reset_complete.html'), name='password_reset_complete'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset/password_reset_confirm.html'), name='password_reset_confirm'),
]
