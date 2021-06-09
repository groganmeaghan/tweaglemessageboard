from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

#def home(request):
    #return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
