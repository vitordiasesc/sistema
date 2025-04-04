# Generated by Django 5.1.6 on 2025-03-30 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0012_turma_turno_alter_aluno_turma_alter_turma_serie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('funcao', models.CharField(choices=[('Diretor(a)', 'Diretor(a)'), ('Secretario(a)', 'Secretário(a)'), ('Coordenador(a)', 'Coordenador(a)')], max_length=20)),
                ('numero_matricula', models.CharField(max_length=20)),
                ('decreto_nomeacao', models.CharField(max_length=100)),
            ],
        ),
    ]
