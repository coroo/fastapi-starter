"""create users table

Revision ID: 016712d9f3f4
Revises:
Create Date: 2020-10-15 15:53:00.114337

"""
from alembic import op
import sqlalchemy as sa
from app.utils.uuid import generate_uuid
from app.utils.hash import create_hashing


# revision identifiers, used by Alembic.
revision = '016712d9f3f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    users = op.create_table(
        'users',
        sa.Column('id', sa.String(50), primary_key=True, index=True),
        sa.Column('email', sa.String(100),
                  unique=True,
                  index=True,
                  nullable=False),
        sa.Column('full_name', sa.String(100)),
        sa.Column('hashed_password', sa.String(100), nullable=False),
        sa.Column('is_active', sa.Boolean, default=True),
        sa.Column('created_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column('updated_at', sa.DateTime(),
                  server_default=sa.func.current_timestamp(), nullable=False),
    )

    uuid = generate_uuid()
    password = create_hashing('Abcd1234')

    op.bulk_insert(users,
                   [
                        {'id': uuid,
                         'email': 'admin@superyou.com',
                         'full_name': 'Administrator',
                         'hashed_password': password,
                         'is_active': 1}
                    ])
    pass


def downgrade():
    op.drop_table('users')
    pass
