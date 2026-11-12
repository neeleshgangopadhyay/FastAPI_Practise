"""Create phone number for user column

Revision ID: 5680543554fb
Revises: 
Create Date: 2026-11-12 06:41:27.637088

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5680543554fb'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    


def downgrade() -> None:
    """Downgrade schema."""
    pass
