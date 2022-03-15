# Generated by Django 3.2.12 on 2022-03-11 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(default='murgormail@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='name',
            field=models.CharField(default='collins', max_length=100),
        ),
    ]
