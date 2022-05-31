from django.urls import path, include
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('detail/<int:blog_id>', views.detail, name='detail'),
    path('edit/<int:blog_id>', views.edit, name='edit'),
    path('delete/<int:blog_id>',views.delete, name='delete'),
]