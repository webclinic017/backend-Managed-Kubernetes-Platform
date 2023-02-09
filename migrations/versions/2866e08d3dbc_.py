"""empty message

Revision ID: 2866e08d3dbc
Revises: bcb1c8c4f66a
Create Date: 2022-09-01 05:30:09.546229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2866e08d3dbc'
down_revision = 'bcb1c8c4f66a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('credit_assignments', sa.Column('expiry_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('credit_assignments', 'expiry_date')
    # ### end Alembic commands ###
