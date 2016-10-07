from django.shortcuts import render
from django.http import JsonResponse
from .models import Counter

# Create your views here.
def home(requst):
    new_num = -1
    if not Counter.objects.exists():
        c = Counter.objects.create(counter=1)
        new_num = 1
        c.save()
    else:
        c = Counter.objects.first()
        new_num = c.counter + 1
        c.counter = new_num
        c.save()

    return JsonResponse({"status": "success", "counter": new_num})