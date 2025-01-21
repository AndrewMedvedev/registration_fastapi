"""add table mail.ru

Revision ID: 4cdd553c55f5
Revises: 392f8b24d68c
Create Date: 2025-01-21 22:30:33.986969

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4cdd553c55f5'
down_revision: Union[str, None] = '392f8b24d68c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usermailrus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_mail_ru', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('birthday', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id_mail_ru')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usermailrus')
    # ### end Alembic commands ###
