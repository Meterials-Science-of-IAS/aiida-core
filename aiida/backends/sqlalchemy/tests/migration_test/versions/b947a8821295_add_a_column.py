# -*- coding: utf-8 -*-
"""Add a column

Revision ID: b947a8821295
Revises: 470e57bc0936
Create Date: 2017-06-16 18:09:03.152982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b947a8821295'
down_revision = '470e57bc0936'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))

def downgrade():
    op.drop_column('account', 'last_transaction_date')
