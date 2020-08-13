#Post View
from django.shortcuts import render,redirect
#utils
from posts.forms import PostForm
from posts.models import Post
from django.contrib.auth.decorators import login_required

@login_required
def list_posts(request):
    posts = Post.objects.all().order_by('-created')
    return render(request,'posts/feed.html',{'posts': posts})

@login_required
def create_posts(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')

    else: 
        form = PostForm()
    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form':form,
            'user':request.user,
            'profile':request.user.profile
        }
    )