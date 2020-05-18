from django.db import models

# Create your models here.


class Message(models.Model):

	message = models.TextField()

	date_time = models.DateTimeField(auto_now=True)

	user = models.CharField(max_length=300)

	def getValues(self):

		return {'message': self.message, 'dateTime': self.date_time, 'user': self.user}

