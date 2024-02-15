from django.shortcuts import render
from .forms import DateIdeaForm


def home(request):
    return render(request, 'index.html', {})

def test(request):
    return render(request, "date/test_form.html", {"form": DateIdeaForm()})