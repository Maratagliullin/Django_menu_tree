from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    url = models.CharField(max_length=100, verbose_name='Ссылка')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True,
        blank=True,
        related_name='children_item', verbose_name='Родительский пункт меню')
    menu_name = models.CharField(max_length=50,
                                 verbose_name='Наименование меню')

    def __str__(self):
        return self.title
