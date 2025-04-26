from django.db import models
from django.contrib.auth.models import User  # Import the User model

class Task(models.Model):
    # Add the user field to associate tasks with a user
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    # Other task fields
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=[('todo', 'To-Do'), ('completed', 'Completed')])

    def __str__(self):
        return self.title
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='profile_photos/', default='default-profile.png')
    mobile_number = models.CharField(max_length=10, blank=True, null=True)  # For 10-digit numbers
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    feedback_text = models.TextField()
    star_rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 stars
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.star_rating} Stars"