from django.db import models

# Create your models here.

#Blog Posts
class Blog(models.Model):
    srno = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    slug = models.CharField(max_length = 200)
    content = models.TextField()
    meta = models.TextField()
    thumbnail = models.TextField()
    ImgAlt = models.CharField(max_length = 200)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
    

    def __str__(self):
        return self.title

# Contacts
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    desc = models.TextField()

#  Printing Contact Name In Django Istead Of Contact 1 , contact 2 ........
    def __str__(self):
        return self.name + " - " + self.email # concanating email 