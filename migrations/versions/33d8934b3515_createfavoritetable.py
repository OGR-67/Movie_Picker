"""createFavoriteTable

Revision ID: 33d8934b3515
Revises: 2e3f3761a756
Create Date: 2023-10-04 16:14:53.659644

"""
import os
from alembic import op


# revision identifiers, used by Alembic.
revision = '33d8934b3515'
down_revision = '2e3f3761a756'
branch_labels = None
depends_on = None

versions_directory = os.path.dirname(__file__)


def upgrade():
    with open(
            os.path.join(versions_directory,
                         "../queries/create_favorites_table/up.sql"),
            "r") as file:
        sql = file.read()
        op.execute(sql)


def downgrade():
    with open(os.path.join(versions_directory,
                           "../queries/create_favorites_table/down.sql"),
              "r") as file:
        sql = file.read()
        op.execute(sql)
