from django.db import models

# Create your models here.
class UserInquery(models.Model):
    name = models.CharField(max_length=30)
    mail_id = models.EmailField(max_length=50)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

class UserAccountDetails(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    rollno = models.IntegerField(primary_key=True, max_length=6)
    email_id = models.EmailField()
    phone = models.IntegerField(max_length=10)
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.rollno)