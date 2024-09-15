from django.shortcuts import render
from django.http import HttpResponse
from .models import Posting


def index(request):
    latest_posting_list = Posting.objects.order_by('likes')[:10]
    context = {'latest_posting_list': latest_posting_list}
    return render(request, 'pages/index.html', context)
