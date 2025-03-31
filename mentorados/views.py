from django.shortcuts import render
from django.http import HttpResponse

def mentorados(request):
    return HttpResponse("Hello, world. You're at the mentorados index.")