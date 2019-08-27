from django.shortcuts import render
import requests
# Create your views here.


def show_users_list(request):
    response = requests.get('http://127.0.0.1:8000/rest-api/users/list/')
    data = response.json()
    return render(request, 'show_api_data.html', {
        'data':data
    })


def show_choices(request):
    response = requests.get('http://127.0.0.1:8000/rest-api/choices/')
    data = response.json()
    return render(request, 'show_api_data.html', {
        'data': data
    })
