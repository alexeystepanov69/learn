from django.db import models


# Create your models here.
class Floor(models.Model):
    number = models.IntegerField(verbose_name='Номер этажа', default=1)
    name = models.CharField(max_length=100, verbose_name='Описание')
    has_toilet = models.BooleanField(verbose_name='Есть туалет', default=False)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.IntegerField(verbose_name='Номер')
    description = models.CharField(max_length=100, verbose_name='Описание')
    floor = models.ForeignKey(Floor, related_name='floor', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.number}: {self.description}'