from django import forms

from .models import Subject,Student,Support,Login


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ('subject_name','subject_group',)

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('student_id','first_name','last_name','password', 'subject1', 'level1', 'subject2', 'level2', 'subject3', 'level3',)


class LoginForm (forms.ModelForm):

    class Meta:
        model = Login
        fields = ('id','Login_code', 'password')


class SupportForm (forms.ModelForm):
    class Meta:
        model = Support
        fields = ('instructions', 'questions')
