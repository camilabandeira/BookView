from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.templatetags.static import static


CATEGORY_CHOICES = (
    ('fiction', 'Fiction'),
    ('non_fiction', 'Non-Fiction'),
    ('mystery', 'Mystery'),
    ('fantasy', 'Fantasy'),
    ('biography', 'Biography'),
    ('history', 'History'),
    ('science', 'Science'),
    ('romance', 'Romance'),
    ('others', 'Others'),
)

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    cover_image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_post_image(self):
        return self.cover_image.url if self.cover_image else static('images/default-post-image.svg')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

    class Meta:
        ordering = ['-created_on']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'
