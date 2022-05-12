from django.db import models
#from multiselectfield import MultiSelectField

# Create your models here.
GENRE_CHOICES=(
    ('Action','Action'),
    ('Adventure','Adventure'),
    ('Animation','Animation'),
    ('Biography','Biography'),
    ('Comedy','Comedy'),
    ('Crime','Crime'),
    ('Documentary','Documentary'),
    ('Drama','Drama'),
    ('Family','Family'),
    ('Fantasy','Fantasy'),
    ('Film-Noir','Film-Noir'),
    ('History','History'),
    ('Horror','Horror'),
    ('Music','Music'),
    ('Musical','Musical'),
    ('Mystery','Mystery'),
    ('Romance','Romance'),
    ('Sci-Fi','Sci-Fi'),
    ('Sport','Sport'),
    ('Thriller','Thriller'),
    ('War','War'),
)

LANGUAGE_CHOICES=(
    ('Nepali','Nepali'),
    ('English','English'),
    ('Newari','Newari'),
    ('Bhojpuri','Bhojpuri'),
    ('Limbu','Limbu'),
    ('Tamang','Tamang'),
    ('Gurung','Gurung'),
    ('Rai','Rai'),
)
STATUS_CHOICES=(
    ('RA','Recently Added'),
    ('MW','Most Watched'),
    ('TR','Top Rated'),
    ('FA','Featured'),
)
class Genre(models.Model):
    name=models.CharField(max_length=255,choices=GENRE_CHOICES)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='movies/',max_length=500)
    #category=models.CharField(max_length=255,choices=CATEGORY_CHOICES)
    genre=models.ManyToManyField(Genre,related_name='genres')
    language=models.CharField(max_length=255,choices=LANGUAGE_CHOICES)
    status=models.CharField(max_length=255,choices=STATUS_CHOICES)
    duration=models.IntegerField()
    year_of_production=models.DateField()
    views_count=models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Director(models.Model):
    name = models.CharField(max_length=255)
    image=models.ImageField(upload_to='directors/',max_length=500)
    born=models.DateField()
    description=models.TextField(max_length=1000)
    movies=models.ManyToManyField(Movie,related_name='directors')

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=255)
    image=models.ImageField(upload_to='actors/',max_length=500)
    born=models.DateField()
    description=models.TextField(max_length=1000)
    movies=models.ManyToManyField(Movie,related_name='actors')

    def __str__(self):
        return self.name
