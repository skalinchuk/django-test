from random import randint
import hashlib
import time
from .models import Visitor, VisitorAnswer, Question, Choice
from .exceptions import NoQuestionsException


def get_visitor_question(visitor: Visitor) -> Question:
    """
    Returns random question that has not been answered yet, for a visitor
    :param visitor: Visitor model instance
    :rtype: Question
    :raises: Exception: No questions found
    """
    answered_questions = VisitorAnswer.objects.filter(visitor=visitor.pk).values('question_id')
    questions = Question.objects.exclude(pk__in=answered_questions)
    if questions.count() > 0:
        random_index = randint(0, questions.count()-1)
        return questions.all()[random_index:random_index+1].get()
    else:
        raise NoQuestionsException("No questions found")


def save_choices(visitor: Visitor, question_id: int, choices: list):
    """
    Saves choices of the Visitor into the database
    :param visitor: Visitor model instance
    :param question_id: Question ID
    :type  question_id: int
    :param choices: List of choice IDs
    """
    question = Question.objects.get(pk=question_id)
    for choice_id in choices:
        choice = Choice.objects.get(pk=choice_id, question=question)
        visitor_answer = VisitorAnswer(visitor=visitor, question=question, choice=choice)
        visitor_answer.save()


def get_visitor(request) -> Visitor:
    """
    Identifies or creates a new Visitor using hash string from the session or creating a new one
    :param request: Django request object
    :rtype: Visitor
    """
    if 'hash' not in request.session:
        hash_str = hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()
        request.session['hash'] = hash_str
    else:
        hash_str = request.session.get('hash')
    (visitor, created) = Visitor.objects.get_or_create(visitor_hash=hash_str)

    return visitor