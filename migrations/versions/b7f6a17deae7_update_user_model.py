"""update User model

Revision ID: b7f6a17deae7
Revises: 83688092945f
Create Date: 2017-09-17 16:56:39.279358

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7f6a17deae7'
down_revision = '83688092945f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('realname', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'realname')
    # ### end Alembic commands ###