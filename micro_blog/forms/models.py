from django.db import models


# Create your models here.

class Author(models.Model):
    CHOICE_CITY = (
        ('minsk', 'Minsk'),
        ('moskow', 'Moskow'),
        ('london', 'London'),
    )

    name = models.CharField(max_length=50, verbose_name="Author name")
    surname = models.CharField(max_length=50, verbose_name="Author surname")
    city = models.CharField(choices=CHOICE_CITY, max_length=50, verbose_name="City", help_text="Choice city")

    def __str__(self):
        return "Name: %s" % self.name


class Article(models.Model):
    author = models.ForeignKey(Author, verbose_name="Article author", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Title")
    text = models.TextField(max_length=1000, verbose_name="Article text")

    def __str__(self):
        return self.title
