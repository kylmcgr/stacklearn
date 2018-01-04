"""  /multiplechoice/models.py
    Data models for the multiplechoice app.
"""

from django.db import models
from mathstack.models import Student
from django import forms


class MultipleChoiceAnswer(models.Model):
	""" A `MultipleChoiceAnswer` is a `Student`-created response to a mulitple choice question.
	"""
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	OPTIONS = (
		('a', 3),
		('b', 4),
		('c', 5),
		('d', 6),
	)
	raw_answer = models.CharField(max_length=50, choices=OPTIONS)
	right_answer = models.IntegerField()
	was_correct = models.BooleanField()
	question = models.CharField(max_length=50)

	def __str__(self):
	    return "{} selected {}".format(self.student.username, self.raw_answer) 