"""empty message

Revision ID: 49813da07ecc
Revises: 
Create Date: 2020-12-18 13:29:23.186821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49813da07ecc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('uid', sa.VARCHAR(length=20), nullable=False, comment='用户uid'),
    sa.Column('name', sa.VARCHAR(length=20), nullable=False, comment='用户名'),
    sa.Column('password', sa.VARCHAR(length=255), nullable=True, comment='密码'),
    sa.Column('email', sa.VARCHAR(length=255), nullable=False, comment='邮箱'),
    sa.Column('phone', sa.VARCHAR(length=11), nullable=True, comment='手机号'),
    sa.Column('permission', sa.Integer(), nullable=True, comment='权限'),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('base_ref',
    sa.Column('base_ref_id', sa.VARCHAR(length=20), nullable=False, comment='中间表id'),
    sa.Column('uid', sa.VARCHAR(length=20), nullable=True, comment='用户id'),
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('modify_time', sa.DateTime(), nullable=True, comment='修改时间'),
    sa.Column('suifang', sa.DateTime(), nullable=True, comment='随访时间'),
    sa.Column('beizhu', sa.Text(), nullable=True, comment='备注'),
    sa.ForeignKeyConstraint(['uid'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('base_ref_id')
    )
    op.create_table('base_info',
    sa.Column('base_info_id', sa.VARCHAR(length=20), nullable=False, comment='基本信息id'),
    sa.Column('base_ref_id', sa.VARCHAR(length=20), nullable=True, comment='中间表id'),
    sa.Column('uid', sa.VARCHAR(length=20), nullable=False, comment='患者id'),
    sa.Column('data_type', sa.VARCHAR(length=20), nullable=False, comment='数据类别'),
    sa.Column('name', sa.VARCHAR(length=20), nullable=False, comment='姓名'),
    sa.Column('sex', sa.VARCHAR(length=2), nullable=False, comment='性别'),
    sa.Column('age', sa.VARCHAR(length=10), nullable=False, comment='年龄'),
    sa.Column('id_number', sa.VARCHAR(length=18), nullable=False, comment='身份证号'),
    sa.Column('phone_number', sa.VARCHAR(length=11), nullable=False, comment='手机号'),
    sa.Column('order_number', sa.VARCHAR(length=20), nullable=False, comment='登记号/顺序号'),
    sa.ForeignKeyConstraint(['base_ref_id'], ['base_ref.base_ref_id'], ),
    sa.PrimaryKeyConstraint('base_info_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('base_info')
    op.drop_table('base_ref')
    op.drop_table('user')
    # ### end Alembic commands ###
