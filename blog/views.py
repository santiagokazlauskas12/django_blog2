from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import  (TemplateView, ListView ,DetailView, CreateView, DeleteView,UpdateView)
from .models import Post,Comment
from django.urls import reverse_lazy
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView (TemplateView):
    template_name="blog/index.html"

class PostListView (ListView):
    model=Post

class PostDetailView (DetailView):
    model=Post
    context_object_name="post_detail"
    template_name="blog/post_detail.html"


class PostCreateView (LoginRequiredMixin,CreateView):
    login_url="login"
    model=Post   
    fields=('title','text','author')
    success_url = reverse_lazy('blog:post_list')

class PostUpdateView (LoginRequiredMixin,UpdateView):
    login_url="login"
    model=Post 
    fields=('title','text')
    success_url = reverse_lazy('blog:post_list')
    context_object_name="post_update"

class PostDeleteView (LoginRequiredMixin,DeleteView):
    login_url="login"
    model=Post
    success_url = reverse_lazy('blog:post_list')


class PostDraftsView (LoginRequiredMixin,ListView):
    login_url="login"
    model=Post    
    context_object_name="post_draft"
    template_name="blog/post_draft.html"

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.published()
    return redirect('blog:post_detail', pk=pk)




def add_comment_to_post (request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect( "blog:post_detail", pk=post.pk)
    else:
        form=CommentForm
        return render (request,"blog/comment_form.html",{"form":form})        

@login_required
def aprove_comment(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post=comment.post
    comment.aprove()
    comment.save()
    return redirect ("blog:post_detail", pk=post.pk)       

@login_required
def delete_comment(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post=comment.post
    comment.delete()
    return redirect ("blog:post_detail", pk=post.pk)    

