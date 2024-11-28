from django.core.validators import EmailValidator
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=20, verbose_name= "Name")
    email = models.EmailField(validators=[EmailValidator],verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f"{self.name}({self.email}): {self.message}"


