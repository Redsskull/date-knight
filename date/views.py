from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import DateIdeaForm
from .models import DateIdea

# I know that we are going to create only one page for our project
# but I think it'll be more convenient to create
# a separate view for the home page and the date ideas page


def home(request):
    date_ideas = None
    if request.method == "POST":
        form = DateIdeaForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            print(form_data)
            date_ideas = DateIdea.get_matching_ideas(
                budget=form_data['budget'],
                place=form_data['place'],
                time=form_data['time']  # use 'time' instead of 'preferences'
            )
            print(date_ideas) 
            if not date_ideas:
                messages.info(request, 'No date ideas found matching your preferences. Showing all ideas.')
                date_ideas = DateIdea.objects.all()  # fallback to all date ideas
        else:
            print(form.errors)
            messages.error(request, 'There was an error with the form.')
    else:
        form = DateIdeaForm()
        print(form.fields['budget'].choices)  # add this line
        print(form.fields['place'].choices)  # add this line
        print(form.fields['time'].choices)  # add this line

    return render(request, "index.html", {"form": form, "date_ideas": date_ideas})
