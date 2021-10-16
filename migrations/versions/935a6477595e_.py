"""empty message

Revision ID: 935a6477595e
Revises: 
Create Date: 2021-10-15 16:13:42.009169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '935a6477595e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('document_types', sa.Column('modifiable', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('document_types', 'modifiable')
    # ### end Alembic commands ###