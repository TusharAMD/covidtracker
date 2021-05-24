from django.db import models
from django.db.models.fields import IPAddressField

# Create your models here.

class Information(models.Model):
    Health_Status=(
        ('Safe','Safe'),
        ('Vaccinated','Vaccinated'),
        ('Vulnerable','Vulnerable'),
        ('Covid Positive','Covid Positive'),
        ('Recovered','Recovered'),
    )

    name=models.CharField(max_length=200)
    phoneNo=models.IntegerField()
    #status=models.CharField(max_length=100, choices=Health_Status)
    status=models.CharField(max_length=100)
    ip=models.CharField(max_length=200)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name