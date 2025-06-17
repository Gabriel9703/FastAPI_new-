from fastapi_new.models import User


def test_create_user():
    user = User(
        username='testuser', email='gaheb@gm.com', password='testpassword'
    )
    assert user.username == 'testuser'
    assert user.email == 'gaheb@gm.com'
    assert user.password == 'testpassword'
