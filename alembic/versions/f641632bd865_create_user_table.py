"""create user table

Revision ID: f641632bd865
Revises: a886fa592e5e
Create Date: 2022-12-03 22:14:59.681543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f641632bd865'
down_revision = 'a886fa592e5e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(64), nullable=False),
        sa.Column('is_admin', sa.Boolean, server_default='f', nullable=False),
        sa.Column('created_on', sa.DateTime, nullable=False),
        sa.Column('created_by', sa.String(64), nullable=False),
        sa.Column('updated_on', sa.DateTime, nullable=True),
        sa.Column('updated_by', sa.String(64), nullable=True),
        sa.Column('deleted_on', sa.DateTime, nullable=True),
        sa.Column('deleted_by', sa.String(64), nullable=True),
        schema='data'
    )


def downgrade() -> None:
    op.drop_table('user', schema='data')
