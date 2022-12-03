"""create company table

Revision ID: 1f8b1c0ae628
Revises: 5132ba935bbf
Create Date: 2022-12-03 22:41:23.062808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f8b1c0ae628'
down_revision = '5132ba935bbf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'company',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(64), nullable=False),
        sa.Column('description', sa.String(512), nullable=False),
        sa.Column('created_on', sa.DateTime, nullable=False),
        sa.Column('created_by', sa.String(64), nullable=False),
        sa.Column('updated_on', sa.DateTime, nullable=True),
        sa.Column('updated_by', sa.String(64), nullable=True),
        sa.Column('deleted_on', sa.DateTime, nullable=True),
        sa.Column('deleted_by', sa.String(64), nullable=True),
        schema='data'
    )


def downgrade() -> None:
    op.drop_table('company', schema='data')
