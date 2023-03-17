#-------------------------------------------------------------------------------
# Name:        testCustom.py
# Purpose:     Tests ran by github actions
#
# Author:      Evan Hocking
#-------------------------------------------------------------------------------

from openFoodFactsPull import getProduct, getPoints
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from .models import History
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import onCampus 
import pytest

def testOpenFoodFacts():
    """
    test suite for openFoodFactsPull.py
    """
    #tests Null input into getProduct() Function
    assert getProduct(),"OFFP Err: Null input Error"

    #tests a text input into getProduct()
    assert getProduct("hello"),"OFFP Err: text input error"

    #tests an int number into getProduct(), validity irrelevant
    assert getProduct(80135463),"OFFP Err: int input error"

    #tests a string number input to getProduct(), validity irrelevant
    assert getProduct("80135463"),"OFFP Err: string input error"

    #tests a number that is not a valid barcode
    assert getProduct(123),"OFFP Err: non present barcode"
    
    #tests if a dictionary is returned
    assert type(getProduct(80135463)) is dict,"OFFP Err: return type error"

    #tests when ecoscore is not present
    assert getProduct(3017620422003)['ecoRating'],'OFFP Err: Ecoscore Error'

    #tests when non english image is present
    assert getProduct(3228857001316)['image'],'OFFP Err: Foreign Img Error'
    
    #tests when no image is present
    assert  getProduct(7622210713780)['image'],'OFFP Err: No Img Error'

    #tests when no nutriscore is present
    assert getProduct(3033710084913)['nutriscore']== "n/a",'OFFP Err: No Nutriscore'

    #tests when no CO2 data is available
    assert getProduct(3017620422003)['co2'],'OFFP Err: co2 Error'

    #tests if points are type int
    assert type(getProduct(3017620422003)['points'])is str,'OFFP Err: points type Error'

    #tests if too high co2 used for score returns positive int
    assert type(getPoints("10000","E"))is str and int(getPoints("10000","E"))>=1, "OFFP Err: negative points 1"

    #tests if n/a used for points generation
    assert type(getPoints("100","n/a"))is str and int(getPoints("100","E"))>=1, "OFFP Err: negative points 2"

    print("OFFP TEST PASS")


def testOnCampus():
    """
    test suite for onCampus.py
    """
    #tests if geolocation pull was successful
    assert not(onCampus.getLocation()== "Err: Geolocation Failed"), "OC Err: Geolocation Failed"

    #tests if latitude is present
    assert not(onCampus.getLocation() ==  "Err: latitude not found"),"OC Err: Latitude not found"

    #tests if longitude is present
    assert not(onCampus.getLocation() ==  "Err Longitude not found"),"OC Err: Longitude not found"

    #tests return is bool
    assert type(onCampus.isOnCampus()) is bool,"OC Err wrong type return"
    
    print("OC TEST PASS")


@pytest.fixture
def client():
    """
    A pytest fixture that provide object to be used in the following tests
    :return client: The test client
        type - obj (Client)
    """
    client = Client()
    return client


@pytest.fixture
def user():
    """
    A pytest fixture that provide object to be used in the following tests
    :return user: The test user
        type - obj (User)
    """
    user = User.objects.create_user(
        username='testuser',
        email='testuser@example.com',
        password='testpass'
    )
    return user


@pytest.mark.django_db
def testRegister(client):
    url = reverse('users-register')
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url, data={
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password1': 'testpass',
        'password2': 'testpass'
    })
    assert response.status_code == 302

    user = User.objects.get(username='newuser')
    assert user.email == 'newuser@example.com'


@pytest.mark.django_db
def testProfile(client, user):
    url = reverse('users-profile')
    response = client.get(url)
    assert response.status_code == 302

    client.login(username='testuser', password='testpass')
    response = client.get(url)
    assert response.status_code == 200

    history = History.objects.create(user=user, item_name='Test item')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Test item' in response.content.decode()


@pytest.mark.django_db
def testProfileUpdate(client, user):
    url = reverse('users-profile-update')
    response = client.get(url)
    assert response.status_code == 302

    client.login(username='testuser', password='testpass')
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url, data={
        'username': 'updateduser',
        'email': 'updateduser@example.com',
    })
    assert response.status_code == 302

    user.refresh_from_db()
    assert user.username == 'updateduser'
    assert user.email == 'updateduser@example.com'

    
def main():
    testOpenFoodFacts()
    testOnCampus()
    
    # The pytest fixtures that provide object to be used in the following tests
    testClient = client()
    testUser = user()
    
    testRegister(testClient)
    testProfile(testClient, testUser)
    testProfileUpdate(testClient, testUser)
    
main()
