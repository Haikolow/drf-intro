from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50,verbose_name='Название')
    description = models.CharField(max_length=50, verbose_name='Описание')

    class Meta:
        verbose_name = 'Сенсор'
        verbose_name_plural = 'Сенсоры'

    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')


# данные для админки
    class Meta:
        verbose_name = 'Показание' #дополнительная инфа
        verbose_name = 'Показания'