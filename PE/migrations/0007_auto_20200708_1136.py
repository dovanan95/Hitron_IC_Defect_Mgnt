# Generated by Django 3.0.6 on 2020-07-08 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PE', '0006_auto_20200708_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterdata',
            name='dot_pos',
            field=models.ImageField(upload_to=''),
        ),
    ]
