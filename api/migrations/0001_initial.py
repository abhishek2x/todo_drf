# Generated by Django 3.0.7 on 2020-06-10 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.IntegerField(max_length=50)),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
