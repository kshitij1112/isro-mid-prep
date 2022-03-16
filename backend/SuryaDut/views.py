from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect  
from django.shortcuts import render, redirect                                                               # for rendering the template http file
from django.urls import reverse
from django.http import JsonResponse
import datetime, json
from SuryaDut.utils import myFunction



def brightness(request):
    if request.method == 'GET':
        print(request.GET.get('time', None))
        time = request.GET.get('time', None)
        if time is None:
            return JsonResponse({'error': 'time is not specified'}, status = 500)

        result = myFunction(float(time))
        print("result is", result)
        return JsonResponse({"result": result}, status = 200)
