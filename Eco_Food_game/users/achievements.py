# -------------------------------------------------------------------------------
# Name:        achievements.py
# Purpose:     calculates the achievements
#
# Author:      Tom Sturgeon
# -------------------------------------------------------------------------------
from users.models import Profile, History, Achievements


def checkAchievements(request) -> None:
    """
    Checks if the user achieved the achievements objectives and gives it to them
    :param request: The pull request of the user information
        type - HttpRequest
    :return: None
    """

    profile = Profile.objects.get(user=request.user)
    achievements = Achievements.objects.all()

    userAchievements = None

    if len(achievements) == 0:
        userAchievements = Achievements.objects.create(
                Id_id=request.user.id)
        userAchievements.save()
    else:
        for x in range(0, len(achievements)):
            if achievements[x].Id_id == request.user.id:
                userAchievements = achievements[x]
                break
            else:
                # userAchievements = Achievements.objects.raw(f"INSERT INTO users_achievements (Id_id) VALUES ({request.user.id})")
                userAchievements = Achievements.objects.create(
                Id_id=request.user.id)
                userAchievements.save()

    # Checks the history of the user to see if they achieved the First Scan achievement
    if History.objects.raw(f"SELECT * FROM users_history WHERE userId_id={profile.id}"):
        userAchievements.First_Scan = "True"
        userAchievements.save()

    # Checking if the user has a score over 50
    if profile.score >= 50:
        # Give achievement to user
        userAchievements.points_50 = "True"
        userAchievements.save()

    # Checking if the user has a score over 250
    if profile.score >= 250:
        # Give achievement to user
        userAchievements.points_250 = "True"
        userAchievements.save()

    # Checking if the user has a score over 500
    if profile.score >= 500:
        # Give achievement to user
        userAchievements.points_500 = "True"
        userAchievements.save()
    
    # Gets the rank of the user
    rank = calcRank(request)

    # Checking if the user is ranked in the top 10
    if rank <= 10:
        # Give achievement to user
        userAchievements.Top_10 = "True"
        userAchievements.save()

    # Checking if the user is ranked in the top 5
    if rank <= 5:
        # Give achievement to user
        userAchievements.Top_5 = "True"
        userAchievements.save()

    # Checking if the user is ranked top 3
    if rank <= 3:
        # Give achievement to user
        userAchievements.Top_3 = "True"
        userAchievements.save()

    # Checking if the user is ranked 1
    if rank == 1:
        # Give achievement to user
        userAchievements.Top_1 = "True"
        userAchievements.save()


def calcRank(request) -> int:
    """
    Calculates the rank of the user
    :param request: The pull request of the users
        type - HttpRequest
    :return: The rank of the user
        type - int
    """
    profiles = Profile.objects.order_by('-score')

    for y in range(0, len(profiles)):
        if profiles[y].user_id == request.user.id:
            return y + 1


def check25(request, points) -> None:
    """
    Checks if the user has gotten max amount of points from a scan
    :param request: The pull request of the user
    :param points: The points of the scanned item
    :return: None
    """
    achievements = Achievements.objects.all()

    for x in range(0, len(achievements)):
        if achievements[x].Id_id == request.user.id:
            userAchievements = achievements[x]
            break
        Achievements.objects.create(Id_id=request.user.id)

    if points == 25:
        userAchievements.Top_5 = "max_score"
        userAchievements.save()
