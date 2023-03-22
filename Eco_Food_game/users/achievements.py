# -------------------------------------------------------------------------------
# Name:        achievements.py
# Purpose:     calculates the achievements
#
# Author:      Tom Sturgeon
# -------------------------------------------------------------------------------

from users.models import Profile, History, Achievements


def checkAchievements(request):

    profile = Profile.objects.get(user=request.user)

    achievements = Achievements.objects.all()

    userAchievements = None

    if len(achievements) == 0:
        userAchievements = Achievements.objects.create(
                Id_id=request.user.id)
    else:
        for x in range(0, len(achievements)):
            if achievements[x].Id_id == request.user.id:
                userAchievements = achievements[x]
                break
            else:
                userAchievements = Achievements.objects.create(Id_id=request.user.id)

    if History.objects.raw(f"SELECT * FROM users_history WHERE userId_id={profile.id}"):
        userAchievements.First_Scan = "True"
        userAchievements.save()

    if profile.score >= 50:
        userAchievements.points_50 = "True"
        userAchievements.save()

    if profile.score >= 250:
        userAchievements.points_250 = "True"
        userAchievements.save()

    if profile.score >= 500:
        userAchievements.points_500 = "True"
        userAchievements.save()

    rank = calcRank(request)

    if rank <= 10:
        userAchievements.Top_10 = "True"
        userAchievements.save()

    if rank <= 5:
        userAchievements.Top_5 = "True"
        userAchievements.save()

    if rank <= 3:
        userAchievements.Top_3 = "True"
        userAchievements.save()

    if rank == 1:
        userAchievements.Top_1 = "True"
        userAchievements.save()


def calcRank(request):
    profiles = Profile.objects.order_by('-score')

    for y in range(0, len(profiles)):
        if profiles[y].user_id == request.user.id:
            return y + 1


def check25(request, points):

    achievements = Achievements.objects.all()

    for x in range(0, len(achievements)):
        if achievements[x].Id_id == request.user.id:
            userAchievements = achievements[x]
            break
        Achievements.objects.create(Id_id=request.user.id)

    if points == 25:
        userAchievements.Top_5 = "max_score"
        userAchievements.save()
