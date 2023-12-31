# Generated by Django 2.2.5 on 2019-09-26 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cchNoticias', '0005_noticias_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='imagem',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('mensagem', models.CharField(max_length=300)),
                ('noticias', models.ManyToManyField(to='cchNoticias.Noticias')),
            ],
        ),
    ]
