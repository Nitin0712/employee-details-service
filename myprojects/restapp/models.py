from django.db import models


class Employee(models.Model):
    emp_name = models.CharField(max_length=20)
    emp_email = models.EmailField()
    emp_contact = models.CharField(max_length=10)
    emp_address = models.CharField(max_length=100)

    class Meta:
        db_table = 'employee'

    def self(self):
        return self.emp_name