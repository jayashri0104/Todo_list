# Generated by Django 4.2.18 on 2025-07-21 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('descreptions', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]
