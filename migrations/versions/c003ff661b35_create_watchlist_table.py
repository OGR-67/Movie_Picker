"""Create watchlist table

Revision ID: c003ff661b35
Revises: 33d8934b3515
Create Date: 2023-10-05 17:45:46.235720

"""
import os
from alembic import op


# revision identifiers, used by Alembic.
revision = 'c003ff661b35'
down_revision = '33d8934b3515'
branch_labels = None
depends_on = None

versions_directory = os.path.dirname(__file__)


def upgrade():
    with open(
            os.path.join(versions_directory,
                         "../queries/create_watchlist_table/up.sql"),
            "r") as file:
        sql = file.read()
        op.execute(sql)


def downgrade():
    with open(os.path.join(versions_directory,
                           "../queries/create_watchlist_table/down.sql"),
              "r") as file:
        sql = file.read()
        op.execute(sql)
