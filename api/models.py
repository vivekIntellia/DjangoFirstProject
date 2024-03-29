
from django.db import models
from django.utils import timezone


class Post(models.Model):

    Category = (
        ('Web-dev', 'Web-dev'),
        ('Machine Learning', 'Machine Learning')
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)  # Use DateTimeField for date and time
    category = models.CharField(max_length=160, null=True, choices=Category, default='Web-dev')
    image= models.ImageField(upload_to='blog_image/')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'



