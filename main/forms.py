from django import forms

Health_Status=[
        ('Safe','Safe'),
        ('Vaccinated','Vaccinated'),
        ('Vulnerable','Vulnerable'),
        ('Covid Positive','Covid Positive'),
        ('Recovered','Recovered'),
]

class GetEntry(forms.Form):
    name=forms.CharField(label="Your Name")
    phoneNo=forms.IntegerField(label="Your Phone No.")
    status=forms.CharField(label="Please select current status",widget=forms.RadioSelect(choices=Health_Status))
    #ip=forms.IPAddressField()