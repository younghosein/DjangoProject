from django.db import models

class Member(models.Model):
    fname = models.CharField(max_length=225)
    lname = models.CharField(max_length=225)
    phone = models.IntegerField(null=True)
    date_joined = models.DateField(null=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"