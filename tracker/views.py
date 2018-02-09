
from django.shortcuts import render, redirect
from .forms import SubjectForm, LoginForm, SupportForm


from .models import Subject, Topic, Subtopic, Login, Support

# Create your views here.
def index(request):

    num_subjects = Subject.objects.all().count()
    num_topics = Topic.objects.all().count()
    my_subject = Subject.objects.all()
    subject_name = my_subject[0].subject_name
    Login_code = Login.objects.all()
    Sub_topic = Subtopic.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_topics': num_topics, 'num_subjects': num_subjects, 'subject_name': subject_name,},
    )
def subject_new(request):
    if request.method == "POST":
        #POST, the request
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.save()
            return redirect('subject_detail', pk=subject.pk)
    else:
        form = SubjectForm()
    return render(request, 'subject_edit.html', {'form': form})

def Login_new (request):
    if request.method == "POST":
        #POST, the request
        form = LoginForm (request.POST)
        if form.is_valid():
            Login = form.save(commit=False)
            Login.save()
            return redirect('index')

            return redirect('Login_detail', pk=Login.pk)
    else:
        form = LoginForm()
    return render(request, 'Login_edit.html', {'form': form})

def Support_new (request):
    if request.method == "POST":
        # POST, the request
        form = SupportForm(request.POST)
        if form.is_valid():
            Support = form.save(commit=False)
            Support.save()
            return redirect('index')

            return redirect('Support_detail', pk=Support.pk)
    else:
        form = SupportForm()
    return render(request, 'Support_edit.html', {'form': form})



