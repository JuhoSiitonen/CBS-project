from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Posting, Comment
from django.urls import reverse
from .forms import PostingForm, CommentForm

@login_required
def index(request):
    latest_posting_list = Posting.objects.order_by('likes')[:10]
    if request.method == 'POST':
        form = PostingForm(request.POST)
        if form.is_valid():
            new_posting = form.save(commit=False)
            new_posting.user = request.user
            new_posting.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = PostingForm()
    context = {
        'latest_posting_list': latest_posting_list,
        'form': form
        }
    return render(request, 'pages/index.html', context)

@login_required
def posting(request, posting_id):
    posting = Posting.objects.get(pk=posting_id)
    posting = get_object_or_404(Posting, pk=posting_id)
    comments = Comment.objects.filter(posting=posting)
    if request.method == 'POST':
        posting = Posting.objects.get(pk=posting_id)
        posting.comments += 1
        posting.save()
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.posting = posting
            new_comment.save()
        return HttpResponseRedirect(reverse("posting", args=(posting_id,)))
    else:
        form = CommentForm()
    context = {
        'posting': posting,
        'comments': comments,
        'form': form
        }
    return render(request, 'pages/posting.html', context)

@login_required
def like(request, posting_id):
    posting = Posting.objects.get(pk=posting_id)
    posting.likes += 1
    posting.save()
    return HttpResponseRedirect(reverse('index'))


