from django.db import models


class Theme(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=50,
    )
    description = models.TextField(
        verbose_name='Тема',
    )

    def get_absolute_url(self):
        return f'/theme-detail/{self.pk}'

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Exercise(models.Model):
    theme = models.ForeignKey(
        'Theme',
        on_delete=models.CASCADE,
        verbose_name='Тема',
    )
    number = models.PositiveSmallIntegerField(
        verbose_name='Номер задачи',
    )
    short_description = models.CharField(
        verbose_name='Описание',
        max_length=200,
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name='Условие задачи',
    )
    file = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        blank=True,
        null=True,
    )
    correct_answer = models.CharField(
        verbose_name='Правильный ответ',
        max_length=250,
    )

    def __str__(self):
        return self.theme.name + ' Задача ' + str(self.number)

    def get_absolute_url(self):
        return f'/exercise-detail/{self.pk}'

    class Meta:
        ordering = ['theme', 'number']
