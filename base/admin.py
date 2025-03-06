from django.contrib import admin
from base.models import Note, NoteType

# Register your models here.
admin.site.register(Note)
admin.site.register(NoteType)