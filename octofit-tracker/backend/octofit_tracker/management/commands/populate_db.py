from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create_user(username='tony', email='tony@marvel.com', password='ironman', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@marvel.com', password='cap', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@marvel.com', password='hulk', team=marvel)
        clark = User.objects.create_user(username='clark', email='clark@dc.com', password='superman', team=dc)
        diana = User.objects.create_user(username='diana', email='diana@dc.com', password='wonderwoman', team=dc)
        bruce_dc = User.objects.create_user(username='bruce_dc', email='bruce@dc.com', password='batman', team=dc)

        # Create Activities
        Activity.objects.create(user=tony, type='run', duration=30, calories=300)
        Activity.objects.create(user=steve, type='cycle', duration=45, calories=400)
        Activity.objects.create(user=bruce, type='swim', duration=60, calories=500)
        Activity.objects.create(user=clark, type='run', duration=50, calories=450)
        Activity.objects.create(user=diana, type='cycle', duration=40, calories=350)
        Activity.objects.create(user=bruce_dc, type='swim', duration=55, calories=480)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=30)
        Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=45)

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=1200)
        Leaderboard.objects.create(team=dc, points=1100)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
