from django.db import models

# Create your models here.
class admin_customization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default="")
    number = models.BigIntegerField(default=0)

    class Meta:
        verbose_name_plural = "admin_customization"

    def __str__(self):
        return self.name