from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email='test@example.com', username='testuser', team='marvel')
        self.assertEqual(user.username, 'testuser')

    def test_team_creation(self):
        team = Team.objects.create(name='marvel', members=['testuser'])
        self.assertEqual(team.name, 'marvel')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='testuser', activity='run', distance=5)
        self.assertEqual(activity.activity, 'run')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='marvel', points=100)
        self.assertEqual(leaderboard.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', difficulty='easy')
        self.assertEqual(workout.name, 'Pushups')
