from django.db import models
import uuid # Required for unique book instances

class Subject(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular subject in the app")
    subject_name = models.CharField(max_length=20, help_text="Name of the subject to track")


    # Metadata
    class Meta:
        ordering = ["subject_name"]

    # Methods
    #def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Subject.
        """
    #    return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.subject_name


class Topic(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular topic in the app")
    topic_name = models.CharField(max_length=60, help_text="Name of the topic to track")
    subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True)

    # Metadata
    class Meta:
        ordering = ["topic_name"]

    # Methods
    #def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Subject.
        """
    #    return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.topic_name


class SubTopic(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular subtopic in the app")
    subtopic_name = models.CharField(max_length=200, help_text="Name of the topic to track")
    subject = models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True)

    # Metadata
    class Meta:
        ordering = ["subtopic_name"]

    # Methods
    #def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Subject.
        """
    #    return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.subtopic_name