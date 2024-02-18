from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import DateIdeaForm
from .models import DateIdea


def home(request):
    date_ideas = None
    if request.method == "POST":
        form = DateIdeaForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            result = DateIdea.get_matching_ideas(
                budget=form_data['budget'],
                place=form_data['place'],
                time=form_data['time']
            )
            if result.exists():  # if the result is not empty, it's a queryset of date ideas
                date_ideas = list(result.values())
            else:  # if the result is empty, display a message to the user
                messages.info(request, "No matching date ideas found. Please try different criteria.")
                date_ideas = []
        else:
            messages.error(request, 'There was an error with the form.')
            date_ideas = []

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"date_ideas": date_ideas})

    else:
        form = DateIdeaForm()

    return render(request, 'index.html', {'form': form, 'date_ideas': date_ideas})

def about(request):
    return render(request, 'about.html')
