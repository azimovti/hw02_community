from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from .models import Post, Group, User
from . forms import PostForm


from django.contrib.auth.decorators import login_required

quant_posts = 10


@login_required
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


def post_create(request):
    template = 'posts/post_create.html'
    form = PostForm(request.POST or None)
    context = {
        'form': form,
        
        }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        return redirect('posts:profile', username=request.user)
    return render(request, template, context)


def post_edit(request,post_id):
    is_edit = get_object_or_404(Post,pk=post_id)
    template =  'posts/post_create.html'
    context = {'form' : form
        }
    if is_edit.author == request.user:
        form = PostForm(request.POST or None)
        if form.is_valid():  
            form.save()
            return redirect('posts:post_detail', post_id=post_id)
    return render(request, template, context)


def profile(request, username):
    author = get_object_or_404(User,username=username)
    posts = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(posts, quant_posts) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'author' : author,  
        'page_obj':page_obj
                 
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
    


