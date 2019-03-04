from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Archives, Order, OrderPp
from django.template import loader
from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'index.html')


def archives_list(request):
    try:
        my_context = Archives.objects.all()
    except Archives.DoesNotExist:
        raise Http404("Archives does not exist")
    return render(request, "archives_list.html", {'my_context': my_context})


def order_list(request):
    try:
        order_content = Order.objects.all()
    except Order.DoesNotExist:
        raise Http404("Order does not exist")
    return render(request, "order_list.html", {'order_content': order_content})


def order_detail(request, question_id):
    try:
        player_content = Order.objects.get(pk=question_id)
    except Order.DoesNotExist:
        raise Http404("No this player!")
    return render(request, "details.html", {'player_content': player_content})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
