import pytest
from users.serializers import UserSerializer
from django.contrib.auth.models import User as UserModel


@pytest.fixture
def sample_data():
    return {
        'email': 'mytestemail@gmail.com',
        'username': 'thetestuser123',
        'password': 'pAssw)(rd54%',
    }


@pytest.mark.django_db
def test_valid_serializer_data(sample_data):
    serializer = UserSerializer(data=sample_data)
    assert serializer.is_valid()


@pytest.mark.django_db
def test_invalid_serializer_data(sample_data):
    empty_email = sample_data.copy()
    del empty_email['email']
    invalid_email_serializer = UserSerializer(data=empty_email)

    empty_username = sample_data.copy()
    del empty_username['username']
    empty_username_serializer = UserSerializer(data=empty_username)

    empty_password = sample_data.copy()
    del empty_password['password']
    empty_password_serializer = UserSerializer(data=empty_password)

    assert not invalid_email_serializer.is_valid()
    assert empty_username_serializer.is_valid()
    assert not empty_password_serializer.is_valid()


@pytest.mark.django_db
def test_password_validation(sample_data):
    data = sample_data.copy()
    data['password'] = '12345678'
    easy_pass = UserSerializer(data=data)

    data = sample_data.copy()
    data['password'] = '5F&'
    short_pass = UserSerializer(data=data)

    data = sample_data.copy()
    data['password'] = '34768572562345'
    numeric_pass = UserSerializer(data=data)

    assert not easy_pass.is_valid()
    assert not short_pass.is_valid()
    assert not numeric_pass.is_valid()


@pytest.mark.django_db
def test_serializer_save(sample_data):
    serializer = UserSerializer(data=sample_data)
    assert serializer.is_valid()

    instance = serializer.create(sample_data)
    assert isinstance(instance, UserModel)


@pytest.mark.django_db
def test_serializer_save_without_username(sample_data):
    del sample_data['username']
    serializer = UserSerializer(data=sample_data)
    instance = serializer.create(sample_data)

    assert instance.username == sample_data['email']


