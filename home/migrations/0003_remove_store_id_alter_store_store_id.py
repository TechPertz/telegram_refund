# Generated by Django 4.0.2 on 2022-02-08 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_store_delete_stores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='id',
        ),
        migrations.AlterField(
            model_name='store',
            name='store_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]