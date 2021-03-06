"""empty message

Revision ID: 490875df28b
Revises: 5547aa9024a7
Create Date: 2015-11-21 18:15:32.082798

"""

# revision identifiers, used by Alembic.
revision = '490875df28b'
down_revision = '5547aa9024a7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('major', sa.Integer(), nullable=False),
    sa.Column('minor', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('speaker_name', sa.String(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text(u'now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.Unicode(length=256), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text(u'now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['room_id'], [u'rooms.id'], ),
    sa.ForeignKeyConstraint(['user_id'], [u'users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    op.drop_table('users')
    op.drop_table('rooms')
    ### end Alembic commands ###
