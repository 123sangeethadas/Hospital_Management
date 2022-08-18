from django.db import models


# Create your models here.
class Department(models.Model):
    dept = models.CharField(max_length=100)
    dept_desc = models.TextField()

    def __str__(self):
        return self.dept


class Doctors(models.Model):
    doc_name = models.CharField(max_length=200)
    doc_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return 'Dr.'+ self.doc_name+'- '+self.doc_spec




class Booking(models.Model):
    p_name = models.CharField(max_length=200)
    p_phone = models.CharField(max_length=10)
    p_mail = models.EmailField()
    Doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
