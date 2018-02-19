from django.contrib import admin
#Team1: Support
from .models import Subject, Topic, Subtopic, Login, Support, Resources

# Register your models here.
admin.site.register (Subject)
admin.site.register (Topic)
admin.site.register (Subtopic)
admin.site.register (Login)
#Team1: Support
admin.site.register (Support)
admin.site.register (Resources)

