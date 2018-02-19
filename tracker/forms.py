from django import forms

from .models import Subject, Support, Student, Resources

class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ('subject_name','subject_group',)


#Team1: Support

class SupportForm (forms.ModelForm):
    class Meta:
        model = Support
        fields = ('instructions', 'questions')

#Javi: Register
class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('student_id','first_name','last_name','password', 'subject1', 'level1', 'subject2', 'level2', 'subject3', 'level3',)


class ResourcesForm(forms.ModelForm):
    class Meta:
        model = Resources
        fields = ('resource_name', 'subtopic', 'id', 'Resourceid')

