from django.shortcuts import redirect, render

from .forms import DateIdeaForm
from .models import DateIdea

# I know that we are going to create only one page for our project
# but I think it'll be more convenient to create
# a separate view for the home page and the date ideas page


def home(request):
    return render(request, "index.html", {"form": DateIdeaForm()})


def date_ideas(request):
    if request.method == "POST":
        form = DateIdeaForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            print(form_data)
            # Implement a logic that create the date idea/s based on the form_data

            # While we don't have the logic we'll just return first 2 date ideas
            date_ideas = DateIdea.objects.all()[:2]
            return render(request, "date_ideas.html", {"date_ideas": date_ideas})
        
    # If the form is not valid, we'll just return the home page
    # or we can implement a logic to show the errors
    return redirect("home")
