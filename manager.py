# -*- coding:utf-8 -*-
# Run a test server.
import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app, db

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def recreate_db():
    """
    Recreates a local database. You probably should not use this on
    production.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


# @manager.command
# def seed():
#     from app.models import User
#     from faker import Faker
#     fake = Faker()
#     users = [User(username=fake.user_name(), name=fake.name(),
#                   email=fake.email(), password='qwer1234') for i in range(20)]
#     db.session.add_all(users)
#     db.session.commit()
#
#     addresses = []
#     for user in users:
#         address = Address()
#         address.user = user
#         address.address = fake.address()
#         addresses.append(address)
#     db.session.add_all(addresses)
#     db.session.commit()


# @manager.command
# def test():
#     """Run unit tests."""
#     tests = unittest.TestLoader().discover('app.tests', pattern='*.py')
#     unittest.TextTestRunner(verbosity=1).run(tests)


if __name__ == '__main__':
    manager.run()
