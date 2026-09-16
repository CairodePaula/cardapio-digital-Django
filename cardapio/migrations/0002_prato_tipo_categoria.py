# Generated manually for the tipo/categoria classification fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prato',
            name='tipo',
            field=models.CharField(
                max_length=20,
                choices=[
                    ('entrada', 'Entrada'),
                    ('principal', 'Prato Principal'),
                    ('sobremesa', 'Sobremesa'),
                    ('bebida', 'Bebida'),
                    ('acompanhamento', 'Acompanhamento'),
                ],
                default='principal',
            ),
        ),
        migrations.AddField(
            model_name='prato',
            name='categoria',
            field=models.CharField(
                max_length=20,
                choices=[
                    ('brasileira', 'Brasileira'),
                    ('italiana', 'Italiana'),
                    ('japonesa', 'Japonesa'),
                    ('vegetariana', 'Vegetariana'),
                    ('vegana', 'Vegana'),
                    ('outra', 'Outra'),
                ],
                default='outra',
            ),
        ),
    ]
