from django.db import models

# Create your models here.
class Content(models.Model):
    CATEGORY = (
            ('Text', 'Text'),
            ('Image', 'Image')
        )

    parent_id = models.ForeignKey("self", related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    category = models.CharField(max_length=255, choices=CATEGORY)
    content = models.TextField()

class Achievement(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    content = models.ForeignKey(Content, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Education(models.Model):
    school = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.school

class Experience(models.Model):
    place = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField(null=True)
    content = models.ForeignKey(Content, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.place

class Project(models.Model):
    STATUS = (
            ('Discontinued', 'DISCONTINUED'),
            ('Progress', 'PROGRESS'),
            ('Beta', 'BETA'),
            ('Finished', 'FINISHED')
        )

    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, choices=STATUS)
    content = models.ForeignKey(Content, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title