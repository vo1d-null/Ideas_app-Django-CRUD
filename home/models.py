from django.db import models

class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='idea_images/', null=True, blank=True)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    '''
    title: CharField to store the title of the idea.
    
    description: TextField to store the description of the idea.
    
    image: ImageField to allow uploading images for each idea. The images will be stored in the idea_images/ directory.
    
    progress: IntegerField to track the progress of the idea.
    
    The __str__ method is added to provide a human-readable representation of the model object.
    
    '''