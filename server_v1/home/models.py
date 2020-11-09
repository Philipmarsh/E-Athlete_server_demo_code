from django.db import models
from tinymce import models as tinymce_models


class BlogPost(models.Model):
    """Model holding information of Blog posts"""

    created = models.DateTimeField(auto_created=True)
    author = models.CharField(max_length=80, blank=False, null=False)
    image = models.ImageField()
    title = models.CharField(default='Blog Post', blank=False, null=False, max_length=140)
    post = tinymce_models.HTMLField(null=False, blank=False)

    def __str__(self):
        return str(self.title) + ', ' + str(self.author) + ', ' + str(self.created)


# Create your models here.
