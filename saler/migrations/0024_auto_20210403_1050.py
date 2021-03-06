# Generated by Django 3.0.7 on 2021-04-03 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0023_auto_20210403_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='product',
            name='parent',
        ),
        migrations.AddField(
            model_name='category',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='last_visit',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='num_visits',
            field=models.IntegerField(default=0),
        ),
    ]
