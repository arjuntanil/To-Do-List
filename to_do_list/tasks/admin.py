from django.contrib import admin
from .models import Task  # import your model

# Register your models here.
admin.site.register(Task)
# tasks/admin.py
from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'star_rating', 'feedback_text', 'created_at')
    search_fields = ('user__username', 'feedback_text')


# Register your models here.
