# Generated by Django 2.0.7 on 2018-07-07 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('artist', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='album')),
                ('genre', models.CharField(default='slow', max_length=20)),
                ('released', models.DateField()),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100)),
                ('song_artist', models.CharField(blank=True, max_length=100, null=True)),
                ('duration', models.DecimalField(decimal_places=2, max_digits=4)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('song', models.FileField(upload_to='song')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
            ],
        ),
    ]