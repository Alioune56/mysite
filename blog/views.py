from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    post_list = Post.published.all()
    # Pagination with number per page
    paginator = Paginator(post_list,3)
    page_number = request.GET.get('page',1)
    posts = paginator.page(page_number)
    context = {'posts':posts}
    return render(request,'blog/post/list.html',context)

def post_detail(request, year,month,day,post):
    post = get_object_or_404(
        Post,
        slug = post,
        publish__day = day,
        publish__month=month,
        publish__year=year,
        status = Post.Status.PUBLISHED
    )
    context = {'post':post}
    return render (request,'blog/post/detail.html',context)
