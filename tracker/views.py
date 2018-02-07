from django.shortcuts import render

from .models import Subject, Topic, SubTopic


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_subjects = Subject.objects.all().count()
    num_topics = Topic.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_topics': num_topics, 'num_subjects': num_subjects,},
    )
