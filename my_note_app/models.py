from django.db import models

# Create your models here.
class StateList(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=300)

    class Meta:
        managed = True
        db_table = 'state'