from django.shortcuts import render,HttpResponseRedirect
from .models import Message,Comment,Like
from .form import FeedsForm,sign_form,CommentForm,LikeForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q,Count,F
from django.contrib.auth.models import User


def likeview(r,message_id,id):

    obj = Like.objects.filter(Q(message_id=message_id) & Q(liked_by_id=id))
    if len(obj)==0:
        Like.objects.create(message_id=message_id,liked_by_id=id)
        Message.objects.filter(id=message_id).update(like_count=F('like_count') + 1)
    else:
        Like.objects.get(Q(message_id=message_id) & Q(liked_by_id=id)).delete()
        Message.objects.filter(id=message_id).update(like_count=F('like_count') - 1)
    

    
    
    return HttpResponseRedirect('/')


@login_required
def FeedsPost(request):
    if request.method == 'POST':
        form = FeedsForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect('/')  
    else:
        form = FeedsForm()

    return render(request, 'feedform.html', {'form': form})


@login_required
def CommentView(request,id):
    obj=Comment.objects.filter(message_id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.message_id=id
            form.save()
            return HttpResponseRedirect('/comments/'+str(id)) 
    else:
        form = CommentForm()

    return render(request, 'commentform.html', {'form': form, 'obj':obj})


@login_required
def delete_Feed(r,id):
    obj=Message.objects.get(id=id).delete()
    return HttpResponseRedirect('/')


@login_required
def FeedsView(r):
    obj=Message.objects.all()
    obj1=Like.objects.values('message_id').annotate(count=Count('liked_by_id'))
    return render(r,'feedsView.html',{'obj':obj})


def Sign_up(r):
    form=sign_form
    if r.method=='POST':
        form=sign_form(r.POST)
        if form.is_valid():
            abc=form.save()
            abc.set_password(abc.password)
            abc.save()
            return HttpResponseRedirect('/accounts/login')
    return render(r,'signup.html',{'form':form})

