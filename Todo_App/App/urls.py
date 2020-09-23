from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('add_todo/',views.add_todo,name='add_todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo,name='delete_todo'),
    path('register/',views.register,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('contact/',views.contact,name='contact'),
]