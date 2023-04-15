"""create address table

Revision ID: 1e3119d8e916
Revises: 6a614d204c53
Create Date: 2023-04-15 01:26:54.764662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e3119d8e916'
down_revision = '6a614d204c53'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "address",
        sa.Column('id', sa.Integer, nullable=False, primary_key=True),
        sa.Column('address1', sa.String(), nullable=False),
        sa.Column('address2', sa.String(), nullable=False),
        sa.Column('city', sa.String(), nullable=False),
        sa.Column('state', sa.String(), nullable=True),
        sa.Column('country', sa.String(), nullable=False),
        sa.Column('postalcode', sa.String(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('address')
