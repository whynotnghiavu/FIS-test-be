"""Add a column description

Revision ID: 7035d09b3a99
Revises: 
Create Date: 2024-09-20 10:45:23.139299

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7035d09b3a99'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None





def upgrade():
  op.add_column('categories', sa.Column('description', sa.String(255), nullable=True))

def downgrade():
    op.drop_column('categories', 'description')