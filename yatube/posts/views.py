from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Group, User
from django.shortcuts import redirect


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


def profile(request, username):
    author = get_object_or_404(User,username=username)
    posts = Post.objects.filter(author=author)
    paginator = Paginator(posts, quant_posts) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {  'page_obj':page_obj,
                 'author' : author
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
    
def only_user_view(request):
    if not request.user.is_authenticated:
        return redirect('/auth/login/')


