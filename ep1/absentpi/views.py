from django.db.models.aggregates import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from random import randint
from .models import Entry
from .forms import EntryForm

def index(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            unpi_title = form.cleaned_data['title'].replace('π', '_')
            unpi_text = form.cleaned_data['text'].replace('π', '_')
            entry = Entry(title=unpi_title, text=unpi_text)
            entry.save()
            url = reverse('absentpi-show', kwargs={'entry_id': entry.id})
            return HttpResponseRedirect(url)
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

def random(request):
    count = Entry.objects.aggregate(count=Count('id'))['count']
    if count <= 0:
        return HttpResponseRedirect(reverse('absentpi-index'))
    random_index = randint(0, count - 1)
    entry_id = Entry.objects.all()[random_index].id
    url = reverse('absentpi-show', kwargs={'entry_id': entry_id})
    response = HttpResponseRedirect(url)
    return response
