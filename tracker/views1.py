from django.shortcuts import render, redirect

from .models import Subject, Topic, Subtopic

from .forms import SubjectForm

# Views Changes
def index(request):
    """
    View functions for home page of sites.
    """
    # Generate counts of some of the main objects
    num_subjects = Subject.objects.all().count()
    num_topics = Topic.objects.all().count()
    my_subject = Subject.objects.all()
    subject_name = my_subject[0].subject_name

    return render (
        request,
        'index.html',
        context={'myvar': num_subjects,'myvar2': num_topics,
                 'myvar3': my_subject, 'myvar4': subject_name, }
    )


def subject_new(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.save()
        return redirect('subject_all')
    else:
        form = SubjectForm()
    return render(request, 'subject_edit.html', {'form': form})

def home(request):
    if request.method == "POST":
        redirect('index.html')
    else:
        redirect('index.html')

def subject_all(request):
    """
    View functions for home page of sites.
    """
    # Generate counts of some of the main objects
    subjects = Subject.objects.all()

    return render (
        request,
        '../../IBTracker/tracker/templates/subject_all.html',
        context={'all_subjects': subjects, }
    )