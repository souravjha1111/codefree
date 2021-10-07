from .models import irisModel
from .serializers import irisModelSeriallizer
from rest_framework.response import Response
from django.views import View
from django.http import HttpResponse
from .forms import IrisDataForm
from django.shortcuts import render, redirect

def recieve(request):
    if request.method == 'GET':
        return HttpResponse("Service is up")


def send(request):
    form = IrisDataForm(request.POST)
    if form.is_valid():
        serializer = irisModelSeriallizer(data=form.cleaned_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Data is added post a get request on '/send/' end point to get get data or refresh to add new data")
    else:
        form = IrisDataForm()
        return render(request, 'api/send.html', {'form': form})
