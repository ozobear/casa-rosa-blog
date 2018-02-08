from django.shortcuts import render, get_object_or_404
from .models import Post
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list_view(request):
	posts = Post.objects.all()
	paginator = Paginator(posts, 6)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'list.html', {'posts': posts})

def post_detail_view(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'detail.html', {'post': post})