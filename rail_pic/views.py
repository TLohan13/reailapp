from django.shortcuts import render
from django.http import HttpResponse
from rail_pic.models import Content


def railpic(request):

    all_content = Content.objects.all

    return render(request, 'index.html', {'all_content': all_content})
