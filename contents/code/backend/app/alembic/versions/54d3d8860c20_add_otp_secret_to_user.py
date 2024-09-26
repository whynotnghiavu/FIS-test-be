"""add otp_secret to user

Revision ID: 54d3d8860c20
Revises: 992434de822b
Create Date: 2024-09-24 03:23:45.449276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54d3d8860c20'
down_revision: Union[str, None] = '992434de822b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('otp_secret', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'otp_secret')
    # ### end Alembic commands ###
