from django.db import models

class Title(models.Model):
    title = models.CharField(max_length=100)
    position_in_menu = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Título Numeral'
        verbose_name_plural = 'Títulos Numerales'
        ordering = ['position_in_menu']

class Numeral(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position_in_menu = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Numeral'
        verbose_name_plural = 'Numerales'
        ordering = ['position_in_menu']

class SubNumeral(models.Model):
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=1024, default='No hay documentos obligatorios, sin embargo se aconseja constatar todo control a través de un documento, físico o digital.')
    position_in_menu = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubNumeral'
        verbose_name_plural = 'SubNumerales'
        ordering = ['position_in_menu']
