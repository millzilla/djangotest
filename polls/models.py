import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
  """Model representing a Question."""
  def __str__(self):
    return self.question_text

  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
  """Model representing a question Choice."""
  def __str__(self):
    return self.choice_text

  question = models.ForeignKey(Question)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
