from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Subject (models.Model):
    id= models.IntegerField (primary_key = True, help_text = "unique ID for this particular subject")
    subject_name= models.CharField (max_length= 20, help_text= "Name of the subject to track")
    subject_group= models.CharField(max_length=20, help_text= "Group for the subject")

    class Meta:
        ordering = ["subject_name"]

    def _str_(self):
#string for representing the MyModelName object (in Admin site etc)
        return self.subject_name

#Topic

class Topic (models.Model):
    SCOPE = (
        ('C', 'core'),
        ('H', 'High Level'),
        ('S', 'Standard Level'),
)
    #Fields
    id= models.IntegerField(primary_key=True, help_text="Unique ID for this particular topic")
    topic_name= models.CharField (max_length=60, help_text= "Name of the topic to track")
    subject= models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True)
    topic_code= models.CharField(max_length = 20, help_text="Code for the topic")
    hours= models.IntegerField(validators= [MaxValueValidator (240), MinValueValidator(1)])
    scope= models.CharField(choices=SCOPE,max_length=1, help_text="Scope of the topic")


    class Meta:
        ordering = ["topic_name"]

    def __str__(self):
        return self.topic_name

class Subtopic (models.Model):
    id =models.IntegerField(primary_key=True, help_text="Unique ID for this particular Subtopic")
    Subtopic_name = models.CharField(max_length=60, help_text="Name of the Subtopic to track")
    topic= models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True)
    Subtopic_code = models.CharField(max_length=20, help_text="Code for the Subtopic")
    hours = models.IntegerField(validators=[MaxValueValidator(240), MinValueValidator(1)])

    class Meta:
        ordering = ["Subtopic_name"]

    def __str__(self):
        return self.Subtopic_name

class Login (models.Model):
    id = models.IntegerField(primary_key=True, help_text="Unique ID for each student", validators=[MaxValueValidator(10000), MinValueValidator(1000)])
    Login_name = models.CharField(max_length=60, help_text="student name")
    last_name = models.CharField(max_length=60, help_text="last name")
    email = models.CharField(max_length=60, help_text="email")
    password = models.CharField(max_length=60, help_text="password")
    Login_code = models.CharField(max_length=20, help_text="Code for the Login")
    subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ["Login_code"]

    def __str__(self):
        return self.Login_name

class Support (models.Model):
    instructions = models.CharField(max_length=60, help_text="last name")
    questions = models.TextField (max_length= 200)

    class Meta:
        ordering = ["instructions"]


    def __str__(self):
        return self.instructions
