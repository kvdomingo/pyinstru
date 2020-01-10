"""empty message

Revision ID: 703226b2365c
Revises: 20a1770f4e8c
Create Date: 2020-01-10 18:04:25.274910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '703226b2365c'
down_revision = '20a1770f4e8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('publications', sa.Column('subgroup', sa.String(length=3), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('publications', 'subgroup')
    # ### end Alembic commands ###
