# Generated by Django 4.2.1 on 2023-06-02 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumnus',
            options={'verbose_name_plural': 'Alumnus'},
        ),
        migrations.RenameField(
            model_name='alumnus',
            old_name='fullname',
            new_name='fullname',
        ),
        migrations.RemoveField(
            model_name='alumnus',
            name='graduated_from',
        ),
        migrations.RemoveField(
            model_name='alumnus',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='alumnus',
            name='phone',
        ),
        migrations.AlterField(
            model_name='alumnus',
            name='gender',
            field=models.CharField(choices=[('ወ', 'ወንድ'), ('ሴ', 'ሴት')], default='Male', max_length=10),
        ),
        migrations.AlterField(
            model_name='alumnus',
            name='no_of_course_years',
            field=models.CharField(choices=[('2', '2 ዓመት'), ('3', '3 ዓመት'), ('4', '4 ዓመት'), ('5', '3 ዓመት')], default='4', max_length=10),
        ),
    ]
