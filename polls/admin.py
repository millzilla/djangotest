from django.contrib import admin

from .models import Choice, Question


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
  """Customization for inline Choice options."""
  model = Choice
  extra = 1  # Provide 1 extra blank Choice by default


class QuestionAdmin(admin.ModelAdmin):
  """Customization for the Question admin page."""
  # Control the ordering of the Question properties
  # fields = ['pub_date', 'question_text']

  # Control both the ordering and the grouping of the Question properties
  fieldsets = [
    (None,               {'fields': ['question_text']}),
    ('Date information', {'fields': ['pub_date']})
  ]

  # Also allow us to modify Choices inline
  inlines = [ChoiceInline]

  # Show more columns than just the question text on the list page
  list_display = ('question_text', 'pub_date', 'was_published_recently')

  # Show filtering options - use pub_date
  list_filter = ['pub_date']

  # Add a search box over the question_text field
  search_fields = ['question_text']

# Register the Question admin site with the QuestionAdmin options
admin.site.register(Question, QuestionAdmin)

# Register the Choice admin site
# This allows you to add individual choices and associate them with an existing
# or a new Question; not the optimal way to do this
# admin.site.register(Choice)