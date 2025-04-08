from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('imgPath', models.FileField(upload_to='')),
                ('duration', models.CharField(max_length=20)),
                ('genre', models.TextField()),
                ('language', models.CharField(max_length=200)),
                ('mpaaRating_type', models.TextField()),
                ('mpaaRating_label', models.TextField()),
                ('userRating', models.CharField(max_length=20)),
            ],
        ),
    ]
