# Generated by Django 2.1.7 on 2022-05-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(max_length=500, upload_to='actors/')),
                ('born', models.DateField()),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(max_length=500, upload_to='directors/')),
                ('born', models.DateField()),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(max_length=500, upload_to='movies/'),
        ),
        migrations.AddField(
            model_name='director',
            name='movies',
            field=models.ManyToManyField(related_name='directors', to='movie.Movie'),
        ),
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(related_name='actors', to='movie.Movie'),
        ),
    ]