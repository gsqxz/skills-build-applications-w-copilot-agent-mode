from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Limpa dados existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Cria times
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Cria usuários
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='123'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='123'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='123'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='123'),
        ]

        # Cria atividades
        Activity.objects.create(user='ironman', team='Marvel', type='run', duration=30)
        Activity.objects.create(user='spiderman', team='Marvel', type='bike', duration=45)
        Activity.objects.create(user='batman', team='DC', type='swim', duration=25)
        Activity.objects.create(user='superman', team='DC', type='run', duration=50)

        # Cria leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=75)

        # Cria workouts
        Workout.objects.create(name='Treino Marvel', description='Treino especial dos heróis Marvel')
        Workout.objects.create(name='Treino DC', description='Treino especial dos heróis DC')

        self.stdout.write(self.style.SUCCESS('Banco populado com dados de teste!'))
