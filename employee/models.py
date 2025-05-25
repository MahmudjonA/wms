from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Employee(models.Model):
    ROLE_CHOICES = [
        ("boss", "Boss"),
        ("tailor", "Tailor"),
        ("reaper", "Reaper"),
        ("manager", "Manager"),
        ("chef", "Chef"),
        ("cleaner", "Cleaner"),
        ("other", "Other"),
    ]
    full_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=13, unique=True)
    password = models.CharField(max_length=128)  # hashed password
    role = models.CharField(choices=ROLE_CHOICES, max_length=12)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.full_name
