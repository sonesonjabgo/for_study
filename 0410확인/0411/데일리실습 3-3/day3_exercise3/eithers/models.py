from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.TextField(max_length=200)
    issue_a = models.TextField(max_length=100)
    issue_b = models.TextField(max_length=100)


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.BooleanField()
    comment = models.TimeField(max_length=100)