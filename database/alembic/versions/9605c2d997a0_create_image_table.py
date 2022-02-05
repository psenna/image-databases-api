"""create image table

Revision ID: 9605c2d997a0
Revises: 09fc8bf58fe6
Create Date: 2022-01-27 18:56:14.161208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9605c2d997a0'
down_revision = '09fc8bf58fe6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'images',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('data', sa.LargeBinary(), nullable=False),
        sa.Column('thumbnail', sa.LargeBinary(), nullable=False),
        sa.Column("dataset", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["dataset"], ["datasets.id"], ondelete='CASCADE', onupdate='CASCADE'),
    )

def downgrade():
    op.drop_table('images')
