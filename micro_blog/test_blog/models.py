from django.db import models


# Create your models here.
class Example(models.Model):
    integer_field = models.IntegerField()
    positive_field = models.PositiveIntegerField()
    positive_small_field = models.PositiveSmallIntegerField()
    big_integer_field = models.BigIntegerField()
    float_field = models.FloatField()
    email = models.EmailField()
    text_field = models.TextField(max_length=20)
    char_field = models.CharField(max_length=10)
    boolean_field = models.BooleanField(default=False)


class Author(models.Model):
    name = models.CharField(max_length=25, verbose_name="Имя")
    surname = models.CharField(max_length=25, verbose_name="Фамилия")
    date_birth = models.DateField(auto_now=False, verbose_name="Дата рождения")


    def __str__(self):
        return "Имя: %s, Фамилия: %s", (self.name, self.surname)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    CHOICE_GENRE = (
        ('comedy', 'Comedy'),
        ('tragedy', 'Tragedy'),
        ('drama', 'Drama'),
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    genre = models.CharField(max_length=50, choices=CHOICE_GENRE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"


class Publication(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Article(models.Model):
    publications = models.ManyToManyField(Publication)
    headline = models.CharField(max_length=50)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)
