from django.db import models

class hora_parqueo(models.Model):

    precio = models.TextField("Precio")
    servicio_id = models.IntegerField("Servicio")