from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Movie

def post_list(request):
    posts1 = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'blog/post_list.html', {'posts': posts1})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def movie_detail(request):
	movie = Movie("Hobbit", "nice movie")
	return render(request, 'blog/movie_detail.html', {'movie': movie})