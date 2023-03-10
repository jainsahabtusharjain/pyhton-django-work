# Generated by Django 4.1.3 on 2022-11-15 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Quizcategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("detail", models.TextField()),
                ("image", models.ImageField(upload_to="cate_img/")),
            ],
        ),
        migrations.CreateModel(
            name="Quizquestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.TextField()),
                ("opt_1", models.CharField(max_length=100)),
                ("opt_2", models.CharField(max_length=100)),
                ("opt_3", models.CharField(max_length=100)),
                ("opt_4", models.CharField(max_length=100)),
                ("level", models.CharField(max_length=100)),
                ("time_limit", models.IntegerField()),
                ("right_opt", models.CharField(max_length=100)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.quizcategory",
                    ),
                ),
            ],
        ),
    ]
