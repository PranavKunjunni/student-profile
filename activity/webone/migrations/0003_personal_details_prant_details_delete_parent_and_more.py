# Generated by Django 4.0.2 on 2023-03-08 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webone', '0002_remove_student_tc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=200)),
                ('Aname', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=100)),
                ('Adate', models.CharField(max_length=300)),
                ('division', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('db_birth', models.CharField(max_length=300)),
                ('age', models.CharField(max_length=300)),
                ('nationality', models.CharField(max_length=300)),
                ('religion', models.CharField(max_length=200)),
                ('cast', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('sylubus', models.CharField(max_length=200)),
                ('tongues', models.CharField(max_length=200)),
                ('id_marks', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Prant_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ad_Number', models.CharField(max_length=200)),
                ('Parent_Name', models.CharField(max_length=200)),
                ('relation', models.CharField(max_length=250)),
                ('Parent_Occ', models.CharField(max_length=200)),
                ('Parent_Add', models.CharField(max_length=200)),
                ('tele_number', models.CharField(max_length=100)),
                ('G_name', models.CharField(max_length=200)),
                ('G_address', models.CharField(max_length=200)),
                ('G_tele_number', models.CharField(max_length=100)),
                ('Prant_Mobile_num', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('G_Mobile_num', models.CharField(max_length=100)),
                ('Pincode', models.CharField(max_length=100)),
                ('Income', models.CharField(max_length=300)),
                ('Parent_ID', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Parent',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
