from django.urls import path, include
from blog.views import blog_view
 
urlpatterns = [
    path('', blog_view.index, name='index'),
    path('create', blog_view.create, name='create'),
    path('detail/<int:blog_id>', blog_view.detail, name='detail'),
    path('edit/<int:blog_id>', blog_view.edit, name='edit'),
    path('delete/<int:blog_id>',blog_view.delete, name='delete'),
]