from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Entry
from .forms import EntryForm

def index(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = Entry(title=form.cleaned_data['title'], text=form.cleaned_data['text'])
            entry.save()
            return HttpResponseRedirect(reverse('absentpi-show', kwargs={'entry_id': entry.id}))
    else:
        context = {
            'form': EntryForm(),
            'latest_entries': Entry.objects.all().order_by('-id')[:5]
        }
        return render(request, 'absentpi/index.html', context)

def show(request, entry_id):
    context = {
        'entry': Entry.objects.get(id=entry_id)
    }
    return render(request, 'absentpi/show.html', context)
