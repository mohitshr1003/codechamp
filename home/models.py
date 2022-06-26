from django.db import models

# Create your models here.
class UserInquery(models.Model):
    name = models.CharField(max_length=30)
    mail_id = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

class UserAccountDetails(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    rollno = models.IntegerField(primary_key=True)
    email_id = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.rollno)