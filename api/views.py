import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Phone


@csrf_exempt
def check_phone(request):
    if request.content_type != 'application/json':
        return JsonResponse({'response': 'Invalid content type'})
    if Phone.objects.filter(pk=json.loads(request.body)['number']).exists():
        return JsonResponse({'found': '1'})
    return JsonResponse({'found': '0'})
