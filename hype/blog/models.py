from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, blank=True)
    create_on = models.DateTimeField(auto_now_add=False)

    def __unicode__(self):
        return self.tag_name


class Post(models.Model):
    """ Model for post """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    body = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    slug  = models.SlugField(max_length=255, blank=True)
    tag = models.ManyToManyField(Tag, related_name="post")

    def __unicode__(self):
        return self.slug



