# Generated by Django 2.0.1 on 2018-06-11 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=20)),
                ('pcost', models.DecimalField(decimal_places=4, max_digits=10)),
                ('pmfd', models.DateField()),
                ('pexpdt', models.DateField()),
            ],
        ),
    ]