from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# class Snippet(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100, blank=True, default='')
#     code = models.TextField()
#     linenos = models.BooleanField(default=False)
#     language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
#     style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

#     class Meta:
#         ordering = ['created']


class Booking(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    roomid = models.TextField()
    etage = models.TextField(default = "pas d'etage")
    date = models.TextField(default = "pas de date")

    class Meta:
        ordering = ['created']

class Inactivity(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    date = models.TextField(default = "pas de date")
    etage_kdmap = models.TextField(default = "pas d'etage")

    class Meta:
        ordering = ['created']

class Test(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    date = models.TextField(default = "pas de texte")
    etage_kdmap = models.TextField(default = "pas d'etage")
    ip = models.TextField(default = "pas d'IP")

    class Meta:
        ordering = ['created']