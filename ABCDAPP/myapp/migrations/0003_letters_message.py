# Generated by Django 2.0.4 on 2018-04-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180420_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='letters',
            name='message',
            field=models.CharField(max_length=10, null=True, verbose_name='Enter the text : Ex: A FOR APPLE'),
        ),
    ]
