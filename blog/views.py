from django.shortcuts import render
from django.shortcuts import redirect
from .models import Blog
from .forms import BlogForm
from django.contrib import messages

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    params = {
        'blogs': blogs,
    }
    return render(request, 'blog/index.html', params)

def create(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        description = request.POST['description']
        blog = Blog(title=title, description= description)
        blog.save()
        messages.success(request,"Blog created successfully")
        return redirect('index')
    else:
        params = {
            'form': BlogForm(),
        }
        return render(request, 'blog/create.html',params)

def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    params = {
        'blog': blog,
    }
    return render(request, 'blog/detail.html', params)

def edit(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    if(request.method == 'POST'):
        blog.title = request.POST['title']
        blog.description = request.POST['description']
        blog.save()
        return redirect('detail', blog_id)
    else:
        form = BlogForm(initial={
            'title':blog.title,
            'description' : blog.description,
        })
        params = {
            'blog': blog,
            'form': form
            }
        return render(request, 'blog/edit.html', params)

def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if(request.method == 'POST'):
        blog.delete()
        return redirect('index')
    else:
        params = {
            'blog': blog,
        }
        return render(request, 'blog/delete.html', params)