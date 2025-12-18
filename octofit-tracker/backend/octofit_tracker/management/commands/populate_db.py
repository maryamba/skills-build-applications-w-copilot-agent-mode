from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from django.db import connection

# Define sample data
USERS = [
    {"email": "ironman@marvel.com", "username": "ironman", "team": "marvel"},
    {"email": "captainamerica@marvel.com", "username": "captainamerica", "team": "marvel"},
    {"email": "batman@dc.com", "username": "batman", "team": "dc"},
    {"email": "superman@dc.com", "username": "superman", "team": "dc"},
]

TEAMS = [
    {"name": "marvel", "members": ["ironman", "captainamerica"]},
    {"name": "dc", "members": ["batman", "superman"]},
]

ACTIVITIES = [
    {"user": "ironman", "activity": "run", "distance": 5},
    {"user": "batman", "activity": "cycle", "distance": 10},
]

LEADERBOARD = [
    {"team": "marvel", "points": 100},
    {"team": "dc", "points": 90},
]

WORKOUTS = [
    {"name": "Pushups", "difficulty": "easy"},
    {"name": "Sprints", "difficulty": "hard"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        db = connection.cursor().db_conn.client[connection.settings_dict['NAME']]

        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Insert users
        db.users.insert_many(USERS)
        # Insert teams
        db.teams.insert_many(TEAMS)
        # Insert activities
        db.activities.insert_many(ACTIVITIES)
        # Insert leaderboard
        db.leaderboard.insert_many(LEADERBOARD)
        # Insert workouts
        db.workouts.insert_many(WORKOUTS)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
