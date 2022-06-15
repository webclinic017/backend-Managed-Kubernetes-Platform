"""empty message

Revision ID: 011c3345849a
Revises: c3ec36708cee
Create Date: 2022-04-28 23:53:19.547431

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '011c3345849a'
down_revision = 'c3ec36708cee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaction_record', sa.Column('project_id', postgresql.UUID(as_uuid=True), nullable=False))
    op.create_foreign_key(None, 'transaction_record', 'project', ['project_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'transaction_record', type_='foreignkey')
    op.drop_column('transaction_record', 'project_id')
    # ### end Alembic commands ###