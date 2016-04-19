from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .forms import AddForm

def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data.get('a',0)
            b = form.cleaned_data.get('b',0)
            return HttpResponse(str(int(a) + int(b)))
    else:
        form = AddForm()
    return  render(request,'blog/index.html', {'form': form})

