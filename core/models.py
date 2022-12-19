from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(null=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    img1 = models.CharField(max_length=255)
    img2 = models.CharField(max_length=255)
    content1 = models.TextField()
    content2 = models.TextField()

    
    def __str__(self) -> str:
        return self.name
