# Generated by Django 4.0 on 2021-12-08 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='ytVideo',
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=150, unique=True, verbose_name='Titulo'),
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
