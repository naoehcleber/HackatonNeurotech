from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import PacienteForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request)
    else:
        form = PacienteForm()            
    return render(request, 'index.html', {'form': form})
