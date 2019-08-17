from django.db import models
from datetime import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=500)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.question_text + ': ' + self.choice_text

class Visitor(models.Model):
    visitor_hash = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        createdFormatted = self.created.strftime('%d.%m.%Y %H:%M:%S')
        return '{} (created {})'.format(self.visitor_hash, createdFormatted)

    class Meta:
        indexes = [
            models.Index(fields=['visitor_hash']),
        ]


class VisitorAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        createdFormatted = self.created.strftime('%d.%m.%Y %H:%M:%S')
        return '{} (visitor: {}, {})'.format(createdFormatted, str(self.visitor), str(self.choice))
