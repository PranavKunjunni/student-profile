# Generated by Django 4.0.2 on 2023-03-15 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webone', '0005_rename_age_pupil_details_ages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PUPIL_Details',
            new_name='webone_student',
        ),
    ]