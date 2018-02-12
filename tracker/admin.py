from django.contrib import admin
from .models import Subject, Topic, Subtopic, Login, Support

# Register your models here.
admin.site.register (Subject)
admin.site.register (Topic)
admin.site.register (Subtopic)
admin.site.register (Login)
admin.site.register (Support)
