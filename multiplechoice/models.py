"""  /multiplechoice/models.py
    Data models for the multiplechoice app.
"""

from django.db import models
from mathstack.models import Student
from django import forms
from multiplechoice.helpers import compute_answer, get_next_q
import random

class ActiveMultipleChoiceQuestion(models.Model):
    """ A `User` may have up to one `ActiveMultipleChoiceQuestion` object at a time.
    The `ActiveMultipleChoiceQuestion` will be deleted when an answer is submitted.
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    q_text = models.CharField(max_length=50)  # post-processed by compute_answer()

    class Meta:
        unique_together = ("student", "q_text")

    def __str__(self):
        return "question for {} re: ".format(
            self.student, self.q_text)


class MultipleChoiceAnswer(models.Model):
	""" A `MultipleChoiceAnswer` is a `Student`-created response to a mulitple choice question.
	"""
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	# active_q = ActiveMultipleChoiceQuestion.objects.filter(student=student).first()
	# q_text = active_q.q_text
	q_text = "10 * 15"
	answer = compute_answer(q_text)
	answers = [0,0,0,0]
	ran = random.randint(0,3)
	answers[ran] = answer
	for i in answers:
		while i == 0:
			i = answer + random.randint(-40,40)
	OPTIONS = (
		(answers[0], answers[0]),
		(answers[1], answers[1]),
		(answers[2], answers[2]),
		(answers[3], answers[3]),
	)
	raw_answer = models.IntegerField(max_length=50, choices=OPTIONS)
	right_answer = models.IntegerField()
	was_correct = models.BooleanField()
	question = models.CharField(max_length=50)

	def save(self, *args, **kwargs):
		print("LOGGING AN ANSWER OBJECT....")
		# retrieve the current `ActiveQuestion` for this `Student`
		created_at = models.DateTimeField(auto_now_add=True)
		active_q = ActiveMultipleChoiceQuestion.objects.filter(student=self.student).first()
		q_text = active_q.q_text
		answer = compute_answer(q_text)
		if type(answer) is int:
		    self.right_answer = answer
		else:
		    raise TypeError("Question-Answer type mismatch")
		self.question = q_text
		self.was_correct = (self.raw_answer == self.right_answer)
		active_q.question = get_next_q()
		active_q.save()
		super(MultipleChoiceAnswer, self).save(*args, **kwargs)

	def __str__(self):
	    return "{} selected {}".format(self.student, self.raw_answer) 