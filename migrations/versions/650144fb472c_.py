"""empty message

Revision ID: 650144fb472c
Revises: bfeb757a2961
Create Date: 2019-01-17 10:28:47.159813

"""

# revision identifiers, used by Alembic.
revision = '650144fb472c'
down_revision = 'bfeb757a2961'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job_ad', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('email', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('name', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job_ad', schema=None) as batch_op:
        batch_op.drop_column('name')
        batch_op.drop_column('email')
        batch_op.drop_column('company')

    # ### end Alembic commands ###