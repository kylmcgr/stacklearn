from django.shortcuts import render
from django.views import generic
from multiplechoice import models as multiplechoice_models
# Create your views here.
class MultipleChoiceAnswerCreateView(generic.CreateView):  
    """ Class-based view to create answers to multiple choice questions.
    """
    model = multiplechoice_models.MultipleChoiceAnswer
    fields = ["raw_answer"]
    template_name = "multiple_choice_answer_create.html"
    #context_object_name

    # def get_context_data(self, **kwargs):
    # 	context_data = super(MultipleChoiceAnswerCreateView, self).get_context_data()
    # 	context_data["operand1"] = 10
    # 	return context_data
