"""create job table

Revision ID: d9bff00c9c2a
Revises: 1f8b1c0ae628
Create Date: 2022-12-03 22:51:13.077384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9bff00c9c2a'
down_revision = '1f8b1c0ae628'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'job',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(64), nullable=False),
        sa.Column('description', sa.String(512), nullable=False),
        sa.Column('responsibilities', sa.ARRAY(sa.String(256)), nullable=False),
        sa.Column('requirements', sa.ARRAY(sa.String(256)), nullable=False),
        sa.Column('benefits', sa.ARRAY(sa.String(256)), nullable=False),
        sa.Column('company_id', sa.Integer, sa.ForeignKey('data.company.id')),
        sa.Column('recruiter_id', sa.Integer, sa.ForeignKey('data.user.id')),
        sa.Column('is_published', sa.Boolean, nullable=False, default=False),
        sa.Column('created_on', sa.DateTime, nullable=False),
        sa.Column('created_by', sa.String(64), nullable=False),
        sa.Column('updated_on', sa.DateTime, nullable=True),
        sa.Column('updated_by', sa.String(64), nullable=True),
        sa.Column('deleted_on', sa.DateTime, nullable=True),
        sa.Column('deleted_by', sa.String(64), nullable=True),
        schema='data'
    )


def downgrade() -> None:
    op.drop_table('job', schema='data')
