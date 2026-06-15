from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.base import ContentFile
from .models import Note, NoteImage
import requests

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/list.html', {'notes': notes})

def note_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        image_url = request.POST.get('image_url', '').strip()

        if title and content:
            note = Note(title=title, content=content)

            screenshot = request.FILES.get('screenshot')
            if screenshot:
                note.screenshot = screenshot
            note.save()

            for f in request.FILES.getlist('extra_images'):
                NoteImage.objects.create(note=note, image=f)

            if image_url:
                try:
                    resp = requests.get(image_url, timeout=10)
                    if resp.status_code == 200:
                        ext = image_url.split('.')[-1].split('?')[0][:4]
                        if ext.lower() not in ['jpg', 'jpeg', 'png', 'webp', 'gif']:
                            ext = 'jpg'
                        filename = f"url_image_{note.pk}.{ext}"
                        if not note.screenshot:
                            note.screenshot.save(filename, ContentFile(resp.content), save=True)
                        else:
                            NoteImage.objects.create(
                                note=note,
                                image=ContentFile(resp.content, name=filename)
                            )
                except Exception:
                    pass

        return redirect('note_list')
    return render(request, 'notes/create.html')

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    extra_images = note.images.all()
    return render(request, 'notes/detail.html', {'note': note, 'extra_images': extra_images})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
    return redirect('note_list')
