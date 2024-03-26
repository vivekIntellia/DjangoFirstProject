import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("viewflow", "0012_alter_process_data_alter_task_data"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_text', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            name="HelloWorldProcess",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("viewflow.process",),
        ),
        migrations.CreateModel(
            name="Profile_picture",

            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_10_school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('class_10_board_or_university', models.CharField(blank=True, max_length=100, null=True)),
                ('class_10_year_of_passing', models.IntegerField(blank=True, null=True)),
                ('class_10_grade_or_cgpa', models.FloatField(blank=True, null=True)),
                ('class_12_school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('class_12_board_or_university', models.CharField(blank=True, max_length=100, null=True)),
                ('class_12_year_of_passing', models.IntegerField(blank=True, null=True)),
                ('class_12_grade_or_cgpa', models.FloatField(blank=True, null=True)),
                ('graduation_college_name', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_board_or_university', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_year_of_passing', models.IntegerField(blank=True, null=True)),
                ('graduation_grade_or_cgpa', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="SignUp",
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
                ("fname", models.CharField(max_length=100)),
                ("lname", models.CharField(max_length=100)),
                ("gender", models.CharField(blank=True, max_length=10, null=True)),
                ("phone", models.CharField(max_length=15)),
                ("address", models.CharField(max_length=255)),
                ("zip_code", models.CharField(max_length=10)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("status", models.CharField(default=False, max_length=50)),
                ("approved", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserDetail",
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
                ("sport", models.CharField(max_length=100)),
                ("school_experience", models.CharField(max_length=100)),
                ("state_experience", models.CharField(max_length=100)),
                ("national_experience", models.CharField(max_length=100)),
                ("international_experience", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=50)),
                ("note", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                ("email_verified", models.BooleanField(default=False)),
                (
                    "verification_token",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
=======
            name='Profile_picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(default='default_profile_picture.jpg', upload_to='profile_pics/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(max_length=100)),
                ('school_experience', models.CharField(max_length=100)),
                ('state_experience', models.CharField(max_length=100)),
                ('national_experience', models.CharField(max_length=100)),
                ('international_experience', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('note', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_verified', models.BooleanField(default=False)),
                ('verification_token', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
