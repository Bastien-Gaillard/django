import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=100)),
                ('date_sortie', models.DateField()),
                ('realisateur', models.CharField(max_length=200)),
                ('acteurs', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utilisateur', models.CharField(max_length=200)),
                ('avis', models.TextField()),
                ('note_initiale', models.FloatField()),
                ('note_finale', models.FloatField(blank=True, default=None, null=True)),
                ('date_avis', models.DateTimeField(auto_now_add=True)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avis', to='reviews.film')),
            ],
        ),
    ]
