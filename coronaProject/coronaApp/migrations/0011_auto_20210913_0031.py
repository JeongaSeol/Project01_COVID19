# Generated by Django 3.2.6 on 2021-09-13 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coronaApp', '0010_board'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='author',
        ),
        migrations.RemoveField(
            model_name='board',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='board',
            name='modified_date',
        ),
        migrations.RemoveField(
            model_name='board',
            name='title',
        ),
        migrations.AlterField(
            model_name='board',
            name='content',
            field=models.CharField(max_length=255),
        ),
    ]
