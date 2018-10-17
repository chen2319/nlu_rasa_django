from django.db import models

# Create your models here.
class Intent(models.Model):
    intent = models.CharField(max_length=200)
    def __str__(self):
        return self.intent


class TrainingQuestion(models.Model):
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=2000)
    def __str__(self):
        return self.question_text