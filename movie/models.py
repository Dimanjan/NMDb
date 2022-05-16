from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


#import reverse
from django.urls import reverse
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
class Director(models.Model):
    name = models.CharField(max_length=255)
    image=models.ImageField(upload_to='directors/',max_length=500)
    born=models.DateField()
    description=models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=255)
    image=models.ImageField(upload_to='actors/',max_length=500)
    born=models.DateField()
    description=models.TextField(max_length=1000)

    def __str__(self):
        return self.name


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
    director=models.ManyToManyField(Director,related_name='director')
    actor=models.ManyToManyField(Actor,related_name='actor')
    language=models.CharField(max_length=255,choices=LANGUAGE_CHOICES)
    status=models.CharField(max_length=255,choices=STATUS_CHOICES)
    duration=models.IntegerField()
    year_of_production=models.DateField()
    views_count=models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('movie_detail',kwargs={'pk':self.pk})


    def __str__(self):
        return self.title


# reviews
class Review(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE, related_name="reviews")
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE, related_name="reviews", default='1')
    rating=models.IntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering=['-created_on']

    def __str__(self):
        return self.name

