from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db.models.signals import post_save
from django.views.decorators.csrf import csrf_exempt, get_token
from .models import Message

import json

# Create your views here.


def home(request):

	# Check the request method
	if request.method == 'GET':

		return render(request, 'chat/home.html', {})

	elif request.method == 'POST':
		# Stores username and interfacecolor defined by user
		request.session['username'] = request.POST['username']
		request.session['interfaceColor'] = request.POST['interfaceColor']

		return JsonResponse({'status': True})


def messages(request):

	return render(request, 'chat/chat.html', {'interfaceColor': request.session['interfaceColor'], 'username': request.session['username']})
