from django.db import models

status_choices = [("active", "Активно"), ("blocked", "Заблокировано")]


class GuestBook(models.Model):
    author = models.CharField(max_length=40, verbose_name='Автор')
    email = models.EmailField(max_length=254, verbose_name='Почта')
    text = models.TextField(verbose_name='Текст записи')
    created_at = models.DateField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Время редактирования')
    status = models.CharField(max_length=40, choices=status_choices, default='active', verbose_name='Статус')

    class Meta:
        db_table = 'guest_book'
        verbose_name = 'Гостевая книга'
        verbose_name_plural = 'Гостевая книга'

    def __str__(self):
        return f'{self.author}: {self.text}, {self.status}, {self.updated_at}'
