"""update field user_id in all tables

Revision ID: 2e7505a2a253
Revises: 26b3bda28c13
Create Date: 2025-03-09 03:56:28.533611

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e7505a2a253'
down_revision: Union[str, None] = '26b3bda28c13'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'usermailrus', ['user_id'])
    op.create_unique_constraint(None, 'uservks', ['user_id'])
    op.create_unique_constraint(None, 'useryandexs', ['user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'useryandexs', type_='unique')
    op.drop_constraint(None, 'uservks', type_='unique')
    op.drop_constraint(None, 'usermailrus', type_='unique')
    # ### end Alembic commands ###
