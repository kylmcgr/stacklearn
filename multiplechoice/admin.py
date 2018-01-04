from django.contrib import admin
from multiplechoice.models import (
	ActiveMultipleChoiceQuestion, MultipleChoiceAnswer
	)
# Register your models here.
admin.site.register(ActiveMultipleChoiceQuestion)
admin.site.register(MultipleChoiceAnswer)