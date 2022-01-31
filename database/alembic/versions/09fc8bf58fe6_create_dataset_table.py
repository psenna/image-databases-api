"""create dataset table

Revision ID: 09fc8bf58fe6
Revises: 54298c1875d0
Create Date: 2022-01-27 18:52:45.620403

"""
from enum import unique
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09fc8bf58fe6'
down_revision = '54298c1875d0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'datasets',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False, unique=True),
    ) 
    op.create_index(op.f("ix_datasets_name"), "datasets", ["name"], unique=True)


def downgrade():
    op.drop_table('datasets')
