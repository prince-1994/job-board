"""create schemas for project

Revision ID: a886fa592e5e
Revises: 
Create Date: 2022-12-03 22:08:12.453294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a886fa592e5e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('CREATE SCHEMA lookup')
    op.execute('CREATE SCHEMA data')


def downgrade() -> None:
    op.execute('DROP SCHEMA data')
    op.execute('DROP SCHEMA lookup')
