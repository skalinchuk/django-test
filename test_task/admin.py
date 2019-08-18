from django.contrib import admin
from django.views.generic.base import TemplateView
from django.db.models import Count
from .models import Question, Choice, Visitor, VisitorAnswer
import json


admin.site.register(Question)
admin.site.register(Choice)


@admin.register(VisitorAnswer)
class VisitorAnswerAdmin(admin.ModelAdmin):
    list_display = ('visitor', 'question', 'choice')
    list_display_links = None


class StatisticsView(TemplateView):
    template_name = 'admin/statistics.html'

    def get(self, request, *args, **kwargs):
        total_visitors = Visitor.objects.count()
        total_respondents = VisitorAnswer.objects.values('visitor_id').distinct().count()

        total_questions = Question.objects.count()
        answered_questions = VisitorAnswer.objects.values('question_id').distinct().count()

        choices_stats = Choice.objects.all().values('question_id').annotate(total=Count('question_id')).order_by('total')
        if (choices_stats.count() > 0):
            choices_min = choices_stats[0]['total']
            choices_max = choices_stats[choices_stats.count()-1]['total']
        else:
            choices_min = 0
            choices_max = 0

        answers = {}
        questions = []

        for answer in VisitorAnswer.objects.values('choice_id').annotate(total=Count('choice_id')):
            answers[answer['choice_id']] = answer['total']

        for question in Question.objects.all():
            question_data = []
            question_labels = []

            for choice in question.choice_set.all():
                question_data.append(str(answers.get(choice.pk, 0)))
                question_labels.append(choice.choice_text)

            questions.append({
                'text': question.question_text,
                'data': json.dumps(question_data),
                'labels': json.dumps(question_labels)

            })

        context = {
            'stats': {
                'visitors': {
                    'total': total_visitors,
                    'respondents': total_respondents
                },
                'questions': {
                    'total': total_questions,
                    'no_answers': total_questions - answered_questions,
                    'with_answers': answered_questions
                },
                'choices': {
                    'min': choices_min,
                    'max': choices_max
                }
            },
            'questions': questions
        }
        return self.render_to_response(context)
