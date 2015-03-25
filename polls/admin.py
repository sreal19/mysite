from django.contrib import admin


from polls.models import  Question, Choice

# Register your models here.
class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields' : ['question_text']}),
        ('Date information', {'fields' : ['pu_date']}),
    ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)


