from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Idea
from .forms import IdeaForm

def idea_list(request):
    ideas = Idea.objects.all()
    return render(request, 'idea_list.html', {'ideas': ideas})

def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'idea_detail.html', {'idea': idea})

def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm()
    return render(request, 'idea_form.html', {'form': form})

def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'idea_form.html', {'form': form})

def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        idea.delete()
        return redirect('idea_list')
    return render(request, 'idea_confirm_delete.html', {'idea': idea})

# Create your views here.
