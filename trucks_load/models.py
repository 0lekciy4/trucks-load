from django.db import models


# Create your models here.
class TruckModel(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Модель грузовика',
    )
    carrying = models.IntegerField(
        verbose_name='Максимальная грузоподьемность',
    )

    def __str__(self):
        return '{}'.format(self.title)


class Truck(models.Model):
    truck_type = models.ForeignKey(
        TruckModel,
        verbose_name='Модель грузовика',
        related_name='truck',
        on_delete=models.CASCADE,
    )
    board_number = models.CharField(
        max_length=16,
        verbose_name='Бортовой номер'
    )
    current_weight = models.IntegerField(
        default=0,
        verbose_name='Текущий вес',
    )

    def __str__(self):
        return '{} {}'.format(self.board_number, self.truck_type)
