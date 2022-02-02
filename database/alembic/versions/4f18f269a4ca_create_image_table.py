"""create image table

Revision ID: 4f18f269a4ca
Revises: 9605c2d997a0
Create Date: 2022-01-27 18:59:17.039175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f18f269a4ca'
down_revision = '9605c2d997a0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'labels',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
    )

    op.create_table(
        'images_labels',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('label_id', sa.Integer, nullable=False),
        sa.Column('image_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(["label_id"], ["labels.id"],),
        sa.ForeignKeyConstraint(["image_id"], ["images.id"],),
    )

def downgrade():
    op.drop_table('images_labels')
    op.drop_table('labels')
