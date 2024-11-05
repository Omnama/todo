# from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
urlpatterns=[
    path('',views.home, name='home-page'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('delete/<str:todo_name>/', views.delete, name='delete'),  # Add this line for delete
    # path('update/<str:todo_name>/', views.update, name='update'),  # Ensure update path exists as well
    # Add other paths as needed
    path('logout/', views.logoutView, name='logout'),
    path('delete-task/<str:name>/', views.deleteTask, name='delete'),
    path('update-task/<str:name>/', views.updateTask, name='update'),
]
