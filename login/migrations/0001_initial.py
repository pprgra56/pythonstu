# Generated by Django 3.2.4 on 2021-06-02 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=22)),
                ('bpub_date', models.DateField()),
            ],
        ),
    ]
