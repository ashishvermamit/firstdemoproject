# Generated by Django 4.1.3 on 2022-12-01 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='drishyamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.CharField(max_length=200)),
                ('review', models.CharField(max_length=500)),
            ],
        ),
    ]
