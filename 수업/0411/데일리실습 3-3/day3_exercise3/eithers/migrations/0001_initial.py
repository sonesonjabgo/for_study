# Generated by Django 3.2.12 on 2023-04-11 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('issue_a', models.TextField(max_length=100)),
                ('issue_b', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick', models.BooleanField()),
                ('comment', models.TimeField(max_length=100)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eithers.question')),
            ],
        ),
    ]
