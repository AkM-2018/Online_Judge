# Generated by Django 3.2.6 on 2021-08-29 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(max_length=10000)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('difficulty', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TestCases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.CharField(max_length=255)),
                ('output', models.CharField(max_length=255)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_judge.problems')),
            ],
        ),
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verdict', models.CharField(max_length=255)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_judge.problems')),
            ],
        ),
    ]
