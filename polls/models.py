import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
  """Model representing a Question."""
  def __str__(self):
    return self.question_text

  # Question properties
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  # Question instance methods
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

  # Additional properties that permit sorting/filtering on Admin page
  # 'admin_order_field': associate the method with a particular property
  was_published_recently.admin_order_field = 'pub_date'
  # 'boolean': use a pretty icon instead of T/F
  was_published_recently.boolean = True
  # 'short_description': list column heading
  was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
  """Model representing a question Choice."""
  def __str__(self):
    return self.choice_text

  # Choice properties
  question = models.ForeignKey(Question)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  