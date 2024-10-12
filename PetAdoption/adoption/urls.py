from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page route
    path('pets/', views.pet_list, name='pet_list'),
    path('<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('create/', views.pet_create, name='pet_create'),
    path('<int:pet_id>/update/', views.pet_update, name='pet_update'),
    path('<int:pet_id>/delete/', views.pet_delete, name='pet_delete'),
    path('<int:pet_id>/request_adopt/', views.request_adopt, name='request_adopt'),  # New URL for adoption requests

    # User Authentication URLs
    #path('login/', auth_views.LoginView.as_view(template_name='adoption/login.html'), name='login'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),  # New URL for user signup
]
