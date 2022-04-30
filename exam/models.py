from django.db import models

# Create your models here.


class Profile(models.Model):  # add this class and the following fields
    field = models.CharField(max_length=250)
    full_name = models.CharField(max_length=250)
    note = models.IntegerField(
        default=0, null=True, blank=True)
    state = models.BooleanField(default=0)
   # finished = models.BooleanField(default=0)

    def __str__(self):
        return self.user.username


class Quiz(models.Model):  # add this class and the following fields
    name = models.CharField(max_length=250)
    state = models.BooleanField(default=0)
    # has many question

    def __str__(self):
        return self.name


class Question(models.Model):  # add this class and the following fields
    question = models.CharField(max_length=500)
    answer1 = models.CharField(max_length=500)
    answer2 = models.CharField(max_length=500)
    answer3 = models.CharField(max_length=500)
    answer4 = models.CharField(max_length=500)
    correct = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class ExamAnswer(models.Model):  # add this class and the following fields
    question_title = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_title
