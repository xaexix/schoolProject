# Generated by Django 4.0.3 on 2022-04-16 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_exercise_id_alter_exercise_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
