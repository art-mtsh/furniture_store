import pytest
from unittest.mock import patch
from users.serializers import CustomTokenObtainPairSerializer
from django.contrib.auth.models import User as UserModel


@pytest.fixture
def existing_user():
    return UserModel.objects.create(
        username='thetestuser123',
        email='mytestemail@gmail.com',
        password='pAssw)(rd54%'
    )


@pytest.fixture
def valid_credentials():
    return {
        'username':'thetestuser123',
        'password':'pAssw)(rd54%'
    }

@pytest.mark.django_db
def test_obtain_token(valid_credentials):

    username = 'thetestuser123'
    password = 'pAssw)(rd54%'

    user = UserModel.objects.create_user(username=username, password=password)

    with patch('users.serializers.User.objects.get') as mock_get_user:
        mock_get_user.return_value = user
        serializer = CustomTokenObtainPairSerializer(data=valid_credentials)
        assert serializer.is_valid()
