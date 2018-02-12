from django import forms

from .models import Subject, Login, Support

class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ('subject_name','subject_group',)


class LoginForm (forms.ModelForm):

    class Meta:
        model = Login
        fields = ('id','Login_code', 'password')



class SupportForm (forms.ModelForm):
    class Meta:
        model = Support
        fields = ('instructions', 'questions')


