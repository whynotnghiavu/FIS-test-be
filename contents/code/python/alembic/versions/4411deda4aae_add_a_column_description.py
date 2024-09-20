"""Add a column description

Revision ID: 4411deda4aae
Revises: 
Create Date: 2024-09-20 14:42:30.262394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4411deda4aae'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None




def upgrade():
  op.add_column('categories', sa.Column('description', sa.String(255), nullable=True))

def downgrade():
    op.drop_column('categories', 'description')