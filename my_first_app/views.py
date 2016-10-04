from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(requst):
    return JsonResponse({"status": "success"})