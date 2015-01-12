from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader

from polls.models import Poll

# Create your views here.
from django.http import HttpResponse

def index(request):
#    return HttpResponse("Hello, world. You're at the poll index.")
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    # return HttpResponse("You're looking at poll %s." % poll_id)
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)