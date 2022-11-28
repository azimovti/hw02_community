from django.shortcuts import render, get_object_or_404

from .models import Post, Group

quant_posts = 10


def index(request):
    posts = Post.objects.all()[:quant_posts]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):

    group = get_object_or_404(Group, slug=slug)

    posts = group.posts.all()[:quant_posts]
#Post.objects.all()[:quant_posts]
    return render(request, 'posts/group_list.html',
                  {'posts': posts, 'grous': group})
