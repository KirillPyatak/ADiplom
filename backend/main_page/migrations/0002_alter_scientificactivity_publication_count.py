# Generated by Django 5.0.3 on 2024-03-10 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scientificactivity',
            name='publication_count',
            field=models.IntegerField(default=0),
        ),
    ]