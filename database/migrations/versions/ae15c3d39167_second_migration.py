"""second migration

Revision ID: ae15c3d39167
Revises: 
Create Date: 2023-07-04 21:35:31.915196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae15c3d39167'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('phone_number', sa.String(length=15), nullable=True),
    sa.Column('gender', sa.Enum('FEMALE', 'MALE', name='genderoptions', create_constraint=True), nullable=True),
    sa.Column('birth_date', sa.DateTime(), nullable=True),
    sa.Column('education', sa.Enum('DIPLOMA', 'BACHELOR', 'MASTER', 'DOCTORATE', name='gradeoptions', create_constraint=True), nullable=True),
    sa.Column('enrollment_date', sa.DateTime(), nullable=True),
    sa.Column('graduation_date', sa.DateTime(), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone_number')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    # ### end Alembic commands ###
