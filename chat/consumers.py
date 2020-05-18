from channels.generic.websocket import WebsocketConsumer
from chat.models import Message

from django.db.models.signals import post_save

import json


class ChatConsumer(WebsocketConsumer):

	def checkMessages(self, **kwargs):

		# Get all messages in DB
		allMessages = Message.objects.all()

		messages = []

		for message in allMessages:
			# Create a dict object with each message info
			messages.append({'user': message.user, 'message': message.message, 'dateTime': [message.date_time.hour, message.date_time.minute]})

		self.send(text_data=json.dumps({'messages': messages}))

		# Connect a signal to when a new message be saved
		post_save.connect(self.checkMessages, Message)

	def connect(self):
		# Create a reference to username
		self.username = ''
		self.accept()

		# Check messages in database and send it to user.
		self.checkMessages()

	def disconnect(self, disconnect_code):

		print(disconnect_code)
	
	def receive(self, text_data):
		
		data = json.loads(text_data)
		
		message = Message(user=data['user'], message=data['message'])
		message.save()

