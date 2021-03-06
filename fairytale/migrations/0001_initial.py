# Generated by Django 2.1.3 on 2018-11-14 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True)),
                ('authors_name', models.ManyToManyField(to='fairytale.Authors')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='fairytale.Categories')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('story_id', models.IntegerField(default=0)),
                ('link_img', models.ImageField(upload_to='')),
                ('created', models.DateTimeField()),
                ('status', models.BooleanField(default=True)),
                ('ordering', models.IntegerField(default=0)),
                ('book_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fairytale.Books')),
            ],
        ),
        migrations.CreateModel(
            name='Generals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('description', models.TextField()),
                ('keywords', models.TextField()),
                ('email', models.CharField(max_length=220)),
                ('site_name', models.TextField()),
                ('facebook', models.CharField(max_length=225)),
                ('hotline', models.CharField(max_length=225)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=225)),
                ('fax', models.CharField(max_length=225)),
                ('logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('status', models.BooleanField(default=True)),
                ('view', models.IntegerField(default=0)),
                ('authors_name', models.ManyToManyField(to='fairytale.Authors')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fairytale.Categories')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='category_id',
            field=models.ManyToManyField(to='fairytale.Categories'),
        ),
        migrations.AlterUniqueTogether(
            name='categories',
            unique_together={('slug', 'parent')},
        ),
    ]
