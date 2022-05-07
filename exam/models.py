import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Create and return a `User` with an email, username and password.
        """
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "login"


class Profile(models.Model):  # add this class and the following fields
    full_name = models.CharField(max_length=250)
    note = models.IntegerField(
        default=0, null=True, blank=True)
    state = models.BooleanField(default=0, blank=True)
   # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    Field_LIST = (
        ('Labo', 'LSP'),
        ('KINE', 'KINE'),
        ('HYG', 'HyG'),
        ('APP', 'APP'),
        ('OPTIC', 'OPTIC'),
        ('ORTHOPTIC', 'ORTHOPTIC'),
    )
    field = models.CharField(max_length=50, choices=Field_LIST)

    def __str__(self):
        return self.full_name


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
