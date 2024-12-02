"""initial migration

Revision ID: 0328bed0cebe
Revises: 
Create Date: 2024-12-02 08:12:15.790253

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0328bed0cebe'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('index', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.Float(), nullable=False),
    sa.Column('data', sa.Text(), nullable=False),
    sa.Column('previous_hash', sa.String(length=64), nullable=False),
    sa.Column('nonce', sa.Integer(), nullable=False),
    sa.Column('hash', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blocks')
    # ### end Alembic commands ###
