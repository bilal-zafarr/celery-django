from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_func


# Create your views here.
def test(request):
    test_func.delay(1, 2)
    return HttpResponse("Hello World")
