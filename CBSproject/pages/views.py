from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Posting
from django.urls import reverse
from .forms import PostingForm

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

