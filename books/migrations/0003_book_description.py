# Generated by Django 4.2.2 on 2023-06-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='No description provided.'),
            preserve_default=False,
        ),
    ]