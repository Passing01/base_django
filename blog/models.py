from django.db import models

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenue = models.TextField()
    date_publication = models.DateTimeField()
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.titre