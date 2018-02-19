from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Subject(models.Model):
    id = models.IntegerField(primary_key=True,help_text="Unique ID for this paticular subject in the app")
    subject_name = models.CharField(max_length=20,help_text="Name of the subject to track")
    subject_group = models.CharField(max_length=20,help_text="Group for the subject")

    class Meta:
        ordering =["subject_name"]

    def __str__(self):
#string for representing the MyModelName object (in Admin site etc)
        return self.subject_name

#Topic

class Topic(models.Model):

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

class Subtopic(models.Model):
    id = models.IntegerField(primary_key=True, help_text="Unique ID for this particlar subtopic in the app")
    subtopic_name = models.CharField(max_length=60, help_text="Name of the subtopic to track")
    topic =models.ForeignKey('Topic',on_delete=models.SET_NULL,null=True)
    code = models.CharField(max_length=20, help_text="Code for subtopic")
    hours = models.IntegerField(validators=[MaxValueValidator(240), MinValueValidator(1)])

    class Meta:
        ordering = ["subtopic_name"]

    def __str__(self):
        return self.subtopic_name

#Javi: Register

class Student(models.Model):

    LEVEL = (
        ('C', 'Core'),
        ('H', 'High Level'),
        ('S', 'Standard Level'),
    )

    student_id = models.IntegerField(primary_key=True,validators=[MaxValueValidator(10000),MinValueValidator(1000)],help_text="Enter your student ID")
    first_name = models.CharField(max_length=60,help_text="write your name")
    last_name = models.CharField(max_length=60,help_text="Write your last name")
    password = models.CharField(max_length=60,help_text="Write a password here. This will be used to access ur account")
    subject1 = models.ForeignKey('Subject', on_delete=models.SET_NULL,related_name= "subject1",null=True)
    level1 = models.CharField(choices= LEVEL, max_length=1, help_text="Chose the level")
    subject2 = models.ForeignKey('Subject',on_delete=models.SET_NULL, related_name= "subject2",null=True)
    level2 = models.CharField(choices=LEVEL, max_length=1, help_text="Chose the level")
    subject3 = models.ForeignKey('Subject', on_delete=models.SET_NULL,related_name= "subject3",null=True)
    level3 = models.CharField(choices=LEVEL, max_length=1, help_text="Chose the level")

    class Meta:
        ordering = ["last_name","first_name"]

    def __str__(self):
        return self.last_name

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

#Team1: Support

class Support (models.Model):
    instructions = models.CharField(max_length=60, help_text="last name")
    questions = models.TextField (max_length= 200)

    class Meta:
        ordering = ["instructions"]


    def __str__(self):
        return self.instructions

class Tracker (models.Model):
    id = models.IntegerField (primary_key=True, validators=[MaxValueValidator(10000), MinValueValidator(1000)])
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subtopic_id = models.ForeignKey(Subtopic, on_delete=models.CASCADE)
    covered = models.BooleanField (default=True)

    class Meta:
        ordering = ["covered"]

    def __str__(self):
        return self.student_id.first_name + " " + self.student_id.first_name + " " + self.subtopic_id.subtopic_name + " " + str(self.covered)


