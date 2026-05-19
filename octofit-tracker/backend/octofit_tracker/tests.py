from django.test import TestCase
from rest_framework.test import APIClient
from .models import Team, Activity, Leaderboard, Workout

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team A")
        self.assertEqual(str(team), "Team A")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user="user1", team="Team A", type="run", duration=30)
        self.assertEqual(str(activity), "user1 - run")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team="Team A", points=100)
        self.assertEqual(str(leaderboard), "Team A: 100")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Pushups", description="Do 20 pushups")
        self.assertEqual(str(workout), "Pushups")

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("teams", response.data)
        self.assertIn("activities", response.data)
        self.assertIn("leaderboard", response.data)
        self.assertIn("workouts", response.data)
