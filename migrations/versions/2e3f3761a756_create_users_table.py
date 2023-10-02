"""create users table

Revision ID: 2e3f3761a756
Revises: 30940ac8df4d
Create Date: 2023-10-02 14:51:13.570848

"""
from alembic import op
import os


# revision identifiers, used by Alembic.
revision = '2e3f3761a756'
down_revision = '30940ac8df4d'
branch_labels = None
depends_on = None

versions_directory = os.path.dirname(__file__)


def upgrade():
    with open(os.path.join(versions_directory, "../queries/create_users_table/up.sql"), "r") as file:
        sql = file.read()
        op.execute(sql)


def downgrade():
    with open(os.path.join(versions_directory, "../queries/create_users_table/down.sql"), "r") as file:
        sql = file.read()
        op.execute(sql)
