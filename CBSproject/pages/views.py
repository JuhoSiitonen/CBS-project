from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Posting, Comment
from django.urls import reverse
from .forms import PostingForm, CommentForm
from django.db import connection


@login_required
def index(request):
    latest_posting_list = Posting.objects.order_by('likes')[:10]
    if request.method == 'POST':
        
        #VULNERABLE CODE
        # Crafting a raw SQL query with string concatenation
        # This is highly vulnerable to SQL injection
        # An attacker could craft a malicious input that would drop the table
        # or do other harmful things

        user_input = request.POST['text']
        user_id = request.user.id
        raw_query = f"INSERT INTO pages_posting (text, user_id, likes, comments) VALUES ('{user_input}', {user_id}, 0, 0)"
        with connection.cursor() as cursor:
            cursor.execute(raw_query)
        return HttpResponseRedirect(reverse('index'))
        
        """
        # SAFER OPTION
        form = PostingForm(request.POST)
        if form.is_valid():
            new_posting = form.save(commit=False)
            new_posting.user = request.user
            new_posting.save()
            return HttpResponseRedirect(reverse('index'))
        
    else:
        form = PostingForm()
        """
    context = {
        'latest_posting_list': latest_posting_list,
        #'form': form
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

#@login_required
def like(request, posting_id):
    posting = Posting.objects.get(pk=posting_id)
    posting.likes += 1
    posting.save()
    return HttpResponseRedirect(reverse('index'))


