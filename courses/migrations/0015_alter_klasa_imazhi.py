# Generated by Django 4.1.1 on 2022-09-26 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20200317_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klasa',
            name='imazhi',
            field=models.ImageField(default='cat_images/default.jpg', upload_to='cat_images'),
        ),
    ]
