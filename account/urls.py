from django.urls import path, include
# from .views import user_login
from django.contrib.auth import views as auth_views
from .views import dashboard, register

urlpatterns = [
    # previous login url
    # path('login/', user_login, name='login'),

    # login/logout urls
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # change password urls
    # path('password-change/', auth_views.PasswordChangeView.as_view(),
    #     name='password_change'),
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(),
    #     name='password_change_done'),
    # reset password urls
    # path('password-reset/', auth_views.PasswordResetView.as_view(),
    #     name="password_reset"),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done"),
    # path('password-reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm"),
    # path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete"),

    # using default URL patterns for authentication views provided by django, as
    # implemented above, but less verbose
    path('', include("django.contrib.auth.urls")),
    path('', dashboard, name='dashboard'),
    path('register/', register, name="register"),

]