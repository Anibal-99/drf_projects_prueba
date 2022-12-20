from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    decriptios=models.TextField()
    technology=models.CharField(max_length=200)
    create_at=models.DateTimeField(auto_now_add=True)
