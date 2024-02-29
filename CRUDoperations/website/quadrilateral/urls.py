from django.urls import path
from . import views

urlpatterns = [
        path('', views.user_list),
    path('create/', views.AddUser),
    path('update/<id>', views.EditUser),
    path('delete/<eid>', views.DeleteUser),
    path('View/<eid>', views.ViewUser),
    
]