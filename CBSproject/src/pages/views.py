from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from . import forms
from django.utils import timezone


from .models import Posting

def index(request):
    return render(request, 'pages/index.html')

def mainpage(request):
    latest_posting_list = Posting.objects.order_by('likes')[:10]
    context = {'latest_posting_list': latest_posting_list}
    return render(request, 'pages/mainpage.html', context)

def new_posting(request):
    if request.method == 'POST':
        form = forms.PostingForm(request.POST)
        if form.is_valid():
            new_posting = Posting()
            new_posting.text = form.cleaned_data['text']
            new_posting.user = request.user
            new_posting.pub_date = timezone.now()
            new_posting.save()
            return HttpResponseRedirect(reverse('mainpage'))
    else:
        form = forms.PostingForm()
    return render(request, 'pages/new_posting.html', {'form': form})