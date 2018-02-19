from django.shortcuts import render,redirect,get_object_or_404
from .models import Subtopic,Subject,Topic,Student, Login, Support, Resources
from .forms import SubjectForm,StudentForm, SupportForm, LoginForm, ResourcesForm

# Create your views here.
def index(request):
    num_subject = Subject.objects.all().count()
    num_topic = Topic.objects.all().count()
    num_subtopic =Subtopic.objects.all().count()

    name_subject= Subject.objects.all()
    subject_name= name_subject[0].id
    all_topics= Topic.objects.all()
    my_subject = Subject.objects.all()
    subject_name = my_subject[0].subject_name
    Login_code = Login.objects.all()
    Sub_topic = Subtopic.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_topic': num_topic,
                 'num_subject': num_subject,
                 'num_subtopics':num_subtopic,
                 'name_subject':name_subject,
                 'topics':all_topics,
                 'subject_name': subject_name,},
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

def subject_all(request):
    all_subject = Subject.objects.all()
    return render(
        request,
        'subject_all.html',
        context={'subjects': all_subject,},
    )

def subject_display (request):
    num_subject = Subject.objects.all().count()
    num_topic= Topic.objects.all().count()
    num_subtopic =Subtopic.objects.all().count()

    name_subject= Subject.objects.all()
    subject_name= name_subject[0].id
    all_topics= Topic.objects.all()
    return render(
        request,
        'subjects_display.html',
        context={'num_topics': num_topic,'num_subject':num_subject,'num_subtopics':num_subtopic,
                 'name_subject':subject_name,'topics':all_topics,'subject':name_subject},
    )

def login_new (request):
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

#Team1: Support
def support_new (request):
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

#javi: Register
def student_new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail', id=student.student_id)
    else:
        form = StudentForm()
    return render(request, 'student_edit.html', {'form': form})

def student_detail(request,id):
    student = Student.objects.get(student_id=id)

    return render(
        request,
        'Student_details.html',
        context={'student': student,}
    )
#Javi: Home page after login
def student_subject(request, id):
    student= get_object_or_404(Student,pk=id)
    student_subject= list()
    student_subject.append(get_object_or_404(Subject, subject_name=student.subject1))
    student_subject.append(get_object_or_404(Subject, subject_name=student.subject2))
    student_subject.append(get_object_or_404(Subject, subject_name=student.subject3))

    return render(
        request,
        'student_record.html',
        context={'student':student,'student_subject':student_subject}

    )

def Resources(request):
        if request.method == "POST":
            # POST, the request
            form = ResourcesForm(request.POST)
            if form.is_valid():
                Support = form.save(commit=False)
                Support.save()
                return redirect('index')

                return redirect('Resources_detail', pk=Resources.pk)
        else:
            form = ResourcesForm()
        return render(request, 'Resources_edit.html', {'form': form})