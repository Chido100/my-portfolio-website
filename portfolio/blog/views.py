from django.shortcuts import render, get_object_or_404
from .models import Blog
from .forms import BlogForm





# View all posts
def all_posts(request):
    posts = Blog.objects.all().order_by('-date_created')
    return render(request, 'blog/all_posts.html', {'posts': posts})



# View post detail
def post_details(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/post_details.html', {'post': post})
