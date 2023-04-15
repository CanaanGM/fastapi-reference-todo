"""add user for address

Revision ID: c37e0c68bf3e
Revises: 1e3119d8e916
Create Date: 2023-04-15 01:34:19.124284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c37e0c68bf3e'
down_revision = '1e3119d8e916'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', 'users', 'address', ['address_id'], ['id'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('address_users_fk', table_name="users")
    op.drop_column('users', 'address_id')
