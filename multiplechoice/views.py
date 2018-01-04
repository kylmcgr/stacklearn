from django.shortcuts import render
from django.views import generic
from multiplechoice import models as multiplechoice_models
from multiplechoice.helpers import (
    compute_answer, get_next_q, parse_question
    )
# Create your views here.
class MultipleChoiceAnswerCreateView(generic.CreateView):  
    """ Class-based view to create answers to multiple choice questions.
    """
    model = multiplechoice_models.MultipleChoiceAnswer
    fields = ["raw_answer"]
    template_name = "multiple_choice_answer_create.html"

    def get_context_data(self, **kwargs):
        context_data = super(MultipleChoiceAnswerCreateView, self).get_context_data(**kwargs)
        # print("THE KEYS ARE:")
        # print(context_data.keys())
        # retrieve the question from `ActiveQuestion` object
        active_q = multiplechoice_models.ActiveMultipleChoiceQuestion.objects.filter(
           student__user=self.request.user).first()
        q_text = active_q.q_text  # fails if no object found
        q_dict = parse_question(q_text)
        context_data["mult1"] = q_dict["mult1"]
        context_data["mult2"] = q_dict["mult2"]
        return context_data