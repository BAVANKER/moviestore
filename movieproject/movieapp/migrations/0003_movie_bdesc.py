# Generated by Django 4.2.1 on 2023-06-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='bdesc',
            field=models.CharField(default='briefing', max_length=300),
            preserve_default=False,
        ),
    ]