from django.shortcuts import render, redirect, get_object_or_404
from .models import Link

def link_list(request):
    links = Link.objects.all()
    return render(request, 'links/list.html', {'links': links})

def link_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        url = request.POST.get('url', '').strip()
        if title and url:
            Link.objects.create(title=title, url=url)
        return redirect('link_list')
    return redirect('link_list')

def link_delete(request, pk):
    link = get_object_or_404(Link, pk=pk)
    if request.method == 'POST':
        link.delete()
    return redirect('link_list')
