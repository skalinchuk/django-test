from django.views import generic
from django.views.generic.base import TemplateResponseMixin
from .helpers import get_visitor_question, save_choices, get_visitor
from .exceptions import NoQuestionsException


class PollView(TemplateResponseMixin, generic.View):
    template_name = 'index.html'

    def get(self, request):
        """Shows the question form"""
        try:
            context = {'question': get_visitor_question(get_visitor(request))}
        except NoQuestionsException:
            context = {'error_message': 'You seem to have answered all our questions. Congratulations!'}

        return self.render_to_response(context)

    def post(self, request):
        """Processes answers from the Visitor and shows another question"""
        visitor = get_visitor(request)
        question_id = request.POST['question']
        choices = request.POST.getlist('choices[]')
        save_choices(visitor, question_id, choices)

        return self.get(request)
