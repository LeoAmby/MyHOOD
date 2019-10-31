# Generated by Django 2.2 on 2019-10-31 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('occupants', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('identity', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.Neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='images')),
                ('bio', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('Neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.Neighborhood')),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='hood.User')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.Neighborhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.User')),
            ],
        ),
    ]
