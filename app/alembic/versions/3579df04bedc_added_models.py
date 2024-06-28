"""added models

Revision ID: 3579df04bedc
Revises: 0f2cf0ea5501
Create Date: 2024-06-28 13:45:27.535259

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3579df04bedc'
down_revision: Union[str, None] = '0f2cf0ea5501'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('close_status', sa.Boolean(), nullable=True, comment='Статус закрытия'),
    sa.Column('closed_at', sa.DateTime(), nullable=True, comment='Время закрытия'),
    sa.Column('task', sa.String(), nullable=True, comment='Представление задания на смену'),
    sa.Column('work_center', sa.String(), nullable=True, comment='Рабочий центр'),
    sa.Column('shift', sa.String(), nullable=True, comment='Смена'),
    sa.Column('crew', sa.String(), nullable=True, comment='Бригада'),
    sa.Column('lot_number', sa.Integer(), nullable=True, comment='Номер партии'),
    sa.Column('lot_date', sa.Date(), nullable=True, comment='Дата партии'),
    sa.Column('name', sa.String(), nullable=True, comment='Номенклатура'),
    sa.Column('codeEKN', sa.String(), nullable=True, comment='кодЕКН'),
    sa.Column('DC_id', sa.String(), nullable=True, comment='идентификатор РЦ '),
    sa.Column('shift_start', sa.DateTime(), nullable=True),
    sa.Column('shift_end', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tasks_id'), 'tasks', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tasks_id'), table_name='tasks')
    op.drop_table('tasks')
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_table('products')
    # ### end Alembic commands ###
