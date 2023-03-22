#---------------------------------------------------------------------------------------
# Name: cronJob.py
# Purpose: For every 24 hours, resetting the daily item history of the users to 0
#
# Author: Phil Cai
#---------------------------------------------------------------------------------------
from django_cron import CronJobBase, Schedule
from users.models import Profile


class CronJob(CronJobBase):
    # Schedules this to be run every 24 hours
    RUN_EVERY_MINS = 1440  # every 24 hours
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    
    code = 'clean_daily_foodRecord'  # a unique code

    
    def do(self) -> None:
        """
        Updates the daily item history of the users to 0
        :param self: When the instance of the object CrongJob is created
        :return: None
        """
        # The user profiles
        u = Profile.objects.all()
        for i in u:
            # Resetting the quantities to 0
            i.Drink = 0
            i.Fruit = 0
            i.Vegetable = 0
            i.Protein = 0
            i.Snack = 0
