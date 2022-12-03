"""create skill table

Revision ID: 5132ba935bbf
Revises: f641632bd865
Create Date: 2022-12-03 22:28:15.722677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5132ba935bbf'
down_revision = 'f641632bd865'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'skill',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(64), nullable=False),
        sa.Column('created_on', sa.DateTime, nullable=False),
        sa.Column('created_by', sa.String(64), nullable=False),
        sa.Column('updated_on', sa.DateTime, nullable=True),
        sa.Column('updated_by', sa.String(64), nullable=True),
        sa.Column('deleted_on', sa.DateTime, nullable=True),
        sa.Column('deleted_by', sa.String(64), nullable=True),
        schema='lookup'
    )


def downgrade() -> None:
    op.drop_table('skill', schema='lookup')
