from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from .models import Post, Group, User
from . forms import PostForm


from django.contrib.auth.decorators import login_required

quant_posts = 10



def index(request):
    posts = Post.objects.all()[:quant_posts]
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, quant_posts) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)
    
    

def group_posts(request, slug):

    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:quant_posts]
    return render(request, 'posts/group_list.html',
                  {'posts': posts, 'grous': group})

@login_required
def post_create(request):
    template = 'posts/post_create.html'
    form = PostForm(request.POST or None)
    context = {
        'form': form,
        }
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:profile', username=request.user)
    return render(request, template, context)


def profile(request, username):
    author = get_object_or_404(User,username=username)
    posts = Post.objects.all().order_by('-pub_date').filter(author__username=username)
    paginator = Paginator(posts, quant_posts) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'author': author,
        'posts': posts,
        'page_obj':page_obj,
       
    }

    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    
    post = get_object_or_404(Post, pk=post_id)
    posts_count = Post.objects.filter(author=post.author).count()
    context = {
        
        'post': post,
        'posts_count':posts_count

    }
    return render(request, 'posts/post_detail.html', context)


def post_edit(request,post_id):
    post = get_object_or_404(Post.objects.select_related(),pk=post_id)
    form = PostForm(request.POST, instance=post)
    
    context = {
        'post' : post,
        'form': form,
        'is_edit': True
    }
    
    if post.author != request.user:
        return redirect('posts:post_detail',post.pk)

    if form.is_valid():
        post = form.save()
        post.save()
            
    return render (request,'posts/post_create.html', context)

        
        
        
        
        

        
       