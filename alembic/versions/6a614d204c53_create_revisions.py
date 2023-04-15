"""create revisions

Revision ID: 6a614d204c53
Revises: 
Create Date: 2023-04-14 17:34:54.186629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a614d204c53'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'users', 
        sa.Column(
            'phone_number', 
            sa.String(),
            nullable=True
            ))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
