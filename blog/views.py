from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("О нас: ООО \"Техно\", г.Минск, ул. Садовая, д.34а, кв.2")
