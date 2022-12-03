"""create job skill many to many table

Revision ID: 8da0b02579ea
Revises: d9bff00c9c2a
Create Date: 2022-12-03 23:18:28.107871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8da0b02579ea'
down_revision = 'd9bff00c9c2a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'job_skill',
        sa.Column('job_id', sa.Integer, sa.ForeignKey('data.job.id')),
        sa.Column('skill_id', sa.Integer, sa.ForeignKey('lookup.skill.id')),
        sa.PrimaryKeyConstraint('job_id', 'skill_id', name = 'job_skill_pkey'),
        schema='data'
    )


def downgrade() -> None:
    op.drop_table('job_skill', schema='data')
