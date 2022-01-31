"""create user table

Revision ID: 54298c1875d0
Revises: 
Create Date: 2022-01-27 18:43:10.945429

"""
from enum import unique
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54298c1875d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('email', sa.String(100), nullable=False, unique=True),
        sa.Column('hash_password', sa.String(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=True),
    )


def downgrade():
    op.drop_table('users')
