from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    subject = models.CharField(max_length=100, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    teacher = models.ManyToManyField(Teacher, related_name='students', on_delete=models.CASCADE)
    group = models.CharField(max_length=100, verbose_name='Класс')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name
