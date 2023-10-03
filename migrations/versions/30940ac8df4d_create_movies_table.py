"""Create movies table

Revision ID: 30940ac8df4d
Revises:
Create Date: 2023-09-28 08:41:12.133279

"""
from alembic import op
import os


# revision identifiers, used by Alembic.
revision = '30940ac8df4d'
down_revision = None
branch_labels = None
depends_on = None

versions_directory = os.path.dirname(__file__)


def upgrade():
    with open(
            os.path.join(versions_directory,
                         "../queries/create_movies_table/up.sql"),
            "r") as file:
        sql = file.read()
        op.execute(sql)


def downgrade():
    with open(os.path.join(versions_directory,
                           "../queries/create_movies_table/down.sql"),
              "r") as file:
        sql = file.read()
        op.execute(sql)
