"""Change coice to ENUM.

Revision ID: 658d4ebd6ee2
Revises: 9fc32c1990ad
Create Date: 2024-11-02 12:21:18.232578

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy_utils.types import ChoiceType
from app.core.constants import Status

# revision identifiers, used by Alembic.
revision = '658d4ebd6ee2'
down_revision = '9fc32c1990ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('descr', sa.Text(), nullable=True),
    sa.Column('status', ChoiceType(Status), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('button')
    op.add_column('user', sa.Column('nic_name', sa.String(), nullable=False))
    op.add_column('user', sa.Column('first_name', sa.String(), nullable=False))
    op.add_column('user', sa.Column('last_name', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    op.drop_column('user', 'nic_name')
    op.create_table('button',
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('descr', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('created_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='button_pkey')
    )
    op.drop_table('task')
    # ### end Alembic commands ###