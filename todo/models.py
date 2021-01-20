from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField() #we're not requiring this
    completed = models.BooleanField(default=False) # not done the moment you make it

    #create string representation of title so we can read it out:
    def __str__(self):
        return self.title