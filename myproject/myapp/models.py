from django.db import models

class person(models.Model):
    name = models.CharField(max_length=100, default='')
    age = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name + ", " + str(self.age)