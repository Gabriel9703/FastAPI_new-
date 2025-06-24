from dataclasses import asdict

from sqlalchemy import select

from fastapi_new.models import User


def test_create_user(session, mook_db_time):
    with mook_db_time(model=User) as time:
        new_user = User(
            username='alice', password='secret', email='teste@test'
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'email': 'teste@test',
        'password': 'secret',
        'created_at': time,
    }
