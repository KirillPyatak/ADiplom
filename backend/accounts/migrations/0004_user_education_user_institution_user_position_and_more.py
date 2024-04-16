# Generated by Django 5.0.3 on 2024-04-15 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_groups_alter_user_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='education',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='institution',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='elibrary_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
