#------------------------------------------------------------------------------------------------------
# Name: cronJob.py
# Purpose: 
#
# Author: 
#------------------------------------------------------------------------------------------------------
from django_cron import CronJobBase, Schedule
from users.models import Profile


class CronJob(CronJobBase):
    RUN_EVERY_MINS = 1440  # every 24 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'clean_daily_foodRecord'  # a unique code

    def do(self):
        u = Profile.objects.all()
        for i in u:
            i.Drink = 0
            i.Fruit = 0
            i.Vegetable = 0
            i.Protein = 0
            i.Snack = 0
