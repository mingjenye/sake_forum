from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    
    return render(request, 'posts/post_create.html', {'form': form})
