from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect 
from .models import Posting
from django.urls import reverse


def index(request):
    latest_posting_list = Posting.objects.order_by('likes')[:10]
    context = {'latest_posting_list': latest_posting_list}
    return render(request, 'pages/index.html', context)

def new_posting(request):
    if request.method == 'POST':
        new_posting = Posting()
        new_posting.text = request.POST['text']
        new_posting.user = request.user
        new_posting.save()
        return HttpResponseRedirect(reverse('index'))
