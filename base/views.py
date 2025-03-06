from django.shortcuts import render
from django.http import HttpResponse
from base.models import Note
from base.models import NoteType



# Create your views here.
def home(request):
    notes_obj = Note.objects.all()
    return render(request, 'home.html', context={'notes': notes_obj})

  
def create_note(request):
    if request.method == "POST":
        name = request.POST.get('note-type')
        description = request.POST.get('description')
        file = request.POST.get('file')
        type = request.POST.get('type')
        deadline_at = request.POST.get('deadline_at')
        type_id = NoteType.objects.get(id = type)
        
        Note.objects.create(name=name, description=description, file=file, type=type_id, deadline_at=deadline_at)
        
    
    note_types = NoteType.objects.all()
    return render(request, 'create_note.html', {'note_types': note_types})


def view_notetype(request):
    notesType_obj = NoteType.objects.all()
    return render(request, 'view_notetype.html', context={'notesType': notesType_obj})

def create_noteType(request):
    if request.method == "POST":
        name = request.POST.get('note-type')
        NoteType.objects.create(name=name)
    
    return render(request, 'create_notetype.html')