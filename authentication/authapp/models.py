from django.db import models
#gender choice field
gender_choices = (
    ("male","male"),
    ("female","female"),
    ("not specified","not specified")
)

# Create your models here.
class User(models.Model):
    # fields of the model.
    first_name = models.CharField(max_length = 10)
    last_name = models.CharField(max_length = 10)
    username = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 20)
    gender = models.CharField(max_length = 15,choices = gender_choices, default='1')
    password = models.CharField(max_length = 20)
    password_repeat = models.CharField(max_length = 20)
    def __str__(self):
       return self.first_name
    

   