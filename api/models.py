from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Box(models.Model):

    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    area = models.IntegerField()
    volume = models.IntegerField()
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    lastUpdated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.createdBy.username} | {self.length} | {self.width} |{self.height} |{self.area} | {self.volume}"

    def save(self, *args, **kwargs):
        self.area = (
            self.length * self.width
            + self.length * self.height
            + self.height * self.width
        ) * 2

        self.volume = self.length * self.width * self.height
        super().save(*args, **kwargs)