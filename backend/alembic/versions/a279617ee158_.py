"""empty message

Revision ID: a279617ee158
Revises: de0cde5224d6
Create Date: 2024-11-01 18:22:38.968440

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a279617ee158'
down_revision: Union[str, None] = 'de0cde5224d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
