# Generated by Django 4.0.5 on 2022-10-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201212_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phno', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('address', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
