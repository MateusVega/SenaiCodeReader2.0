from django.db import models

class eventos(models.Model):
    username = models.TextField(max_length=255)
    data = models.DateField()
    evento = models.TextField(max_length=255)

    def save(self, *args, **kwargs):
        if not eventos.objects.filter(id=self.id).exclude(pk=self.pk).exists():
            super(eventos, self).save(*args, **kwargs)

class mecanica(models.Model):
    numero = models.TextField(max_length=255)
    nome = models.TextField(max_length=255)
    local = models.TextField(max_length=255)
    instrutor = models.TextField(max_length=255)
    status = models.TextField(max_length=255)

    def save(self, *args, **kwargs):
        if not mecanica.objects.filter(numero=self.numero).exclude(pk=self.pk).exists():
            super(mecanica, self).save(*args, **kwargs)

class eletrica(models.Model):
    numero = models.TextField(max_length=255)
    nome = models.TextField(max_length=255)
    local = models.TextField(max_length=255)
    instrutor = models.TextField(max_length=255)
    status = models.TextField(max_length=255)

    def save(self, *args, **kwargs):
        if not eletrica.objects.filter(numero=self.numero).exclude(pk=self.pk).exists():
            super(eletrica, self).save(*args, **kwargs)

class eletronica(models.Model):
    numero = models.TextField(max_length=255)
    nome = models.TextField(max_length=255)
    local = models.TextField(max_length=255)
    instrutor = models.TextField(max_length=255)
    status = models.TextField(max_length=255)

    def save(self, *args, **kwargs):
        if not eletronica.objects.filter(numero=self.numero).exclude(pk=self.pk).exists():
            super(eletronica, self).save(*args, **kwargs)