# Generated by Django 3.2.12 on 2022-03-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_alter_subscriber_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]