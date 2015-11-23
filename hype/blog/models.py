from django.db import models

# Create your models here.

# this is just a comment for a dud pull request, ignore it and under no circumstance merge this request
# thank you for taking out the time to read this

class Tag(models.Model):
    slug = models.SlugField(max_length=255, blank=True)

    def __str__(self):
        return self.slug


class Post(models.Model):
    """ Model for post """
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Post')
    body = models.TextField()
    published_on = models.DateTimeField(auto_now=True )
    published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, blank=True)
    tag = models.ManyToManyField(Tag, related_name="post")

    def __str__(self):
        return self.slug


class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name
