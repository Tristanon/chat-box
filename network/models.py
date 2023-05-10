from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True, related_name='user_posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post {self.id} created by {self.author} on {self.created_at.strftime(' %H:%M:%S %Y-%m-%d')}"
    
class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user_who_following")
    user_follower = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user_who_is_being_followed")

    def __str__(self):
        return f"{self.user} is following {self.user_follower}"
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_like")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_like")

    def __str__(self):
        return f"{self.user} liked {self.post}"
    