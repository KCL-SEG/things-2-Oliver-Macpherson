from django.shortcuts import render
from .forms import ThingForm
from .models import Thing

def home(request):
    form = ThingForm()
    if form.is_valid():
        name = form.cleaned_data.get('name')
        desc = form.cleaned_data.get('description')
        quantity = form.cleaned_data.get('quantity')
        thing = Thing.objects.create(name=name, description=desc, quantity=quantity)
    return render(request, 'home.html', {'form': form})
