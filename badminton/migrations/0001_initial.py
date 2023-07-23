# Generated by Django 4.2.3 on 2023-07-22 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Match",
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
                ("title", models.CharField(max_length=30)),
                ("address", models.CharField(max_length=50)),
                ("match_day", models.DateTimeField(blank=True)),
                ("match_time", models.IntegerField()),
                (
                    "match_rank",
                    models.IntegerField(
                        choices=[
                            (2800, "선수 출신"),
                            (2700, "A조"),
                            (2600, "B조"),
                            (2500, "C조"),
                            (2000, "D조"),
                            (1500, "기본적인 스트로크 구사 가능자"),
                            (1000, "초보자"),
                        ],
                        default=1500,
                    ),
                ),
                ("cost", models.IntegerField()),
                (
                    "manager",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="manage_match_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "player",
                    models.ManyToManyField(
                        related_name="play_match_set", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "ordering": ["-match_day"],
            },
        ),
        migrations.CreateModel(
            name="Review",
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
                ("message", models.TextField()),
                (
                    "satisfaction",
                    models.IntegerField(
                        choices=[(3, "최고에요"), (2, "보통이에요"), (1, "아쉬워요")]
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="badminton.match",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]