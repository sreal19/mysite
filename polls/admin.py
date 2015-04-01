from django.contrib import admin


from polls.models import  Question, Choice

# Register your models here.
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields' : ['question_text']}),
        ('Date information', {'fields' : ['pu_date']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pu_date', 'was_published_recently')
    list_filter = ['pu_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)


