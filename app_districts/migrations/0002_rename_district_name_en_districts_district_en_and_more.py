# Generated by Django 4.2.5 on 2023-09-15 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_districts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='districts',
            old_name='district_name_en',
            new_name='district_en',
        ),
        migrations.RenameField(
            model_name='districts',
            old_name='district_name_ru',
            new_name='district_ru',
        ),
        migrations.RenameField(
            model_name='districts',
            old_name='district_name_uz',
            new_name='district_uz',
        ),
    ]
