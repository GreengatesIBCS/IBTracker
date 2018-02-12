from django import forms

from .models import Subject

class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ('subject_name','subject_group',)

from .models import Login

class LoginForm (forms.ModelForm):

    class Meta:
        model = Login
        fields = ('id','Login_code', 'password')

from .models import Support


class SupportForm (forms.ModelForm):
    class Meta:
        model = Support
        fields = ('instructions', 'questions')


