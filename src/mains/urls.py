from django.urls import path
from . import views

app_name = 'mains'

urlpatterns = [
    path('', views.index_fun, name='home'),
    path('update/<int:id>', views.update_student, name='updatedata'),
    path('delete/<int:id>', views.delete_student, name='deletedata'),
]