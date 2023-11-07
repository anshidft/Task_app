from django.urls import path
from. import views

urlpatterns = [
    path('',views.home, name=""),

    # CRUD OPERATIONS

    # create task
    path('create-task', views.createTask, name='create-task'),

    # read task
    path('view-tasks', views.ViewTask, name='view-tasks'),

    # UPDATE TASK
    path('update-tasks/<str:pk>/', views.updateTask, name='update-tasks'),

    # Delete task
    path('delete-tasks/<str:pk>/', views.DeleteTask, name='delete-tasks'),

    # -------------------REGISTER USER----------------------
    
    path('registers', views.Register, name="registers"),

    # -------------------LOGIN USER----------------------

    path('my-login', views.my_login, name="my-login"),

        # -------------------Dashboard----------------------
    path('dashboard', views.dashboard, name="dashboard"),


    # LOGOUT
    path('user-logout', views.user_logout, name="user-logout"),





]

