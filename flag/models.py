from django.db import models

class Flag(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='flag')
    def __str__(self):
        return str(self.title)
