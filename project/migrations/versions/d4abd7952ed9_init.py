"""init

Revision ID: d4abd7952ed9
Revises: 
Create Date: 2022-07-24 03:35:42.978613

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = "d4abd7952ed9"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "employee",
        sa.Column("full_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("job_title", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column(
            "employment_date", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column("salary", sa.Integer(), nullable=False),
        sa.Column("id_chief", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_employee_employment_date"),
        "employee",
        ["employment_date"],
        unique=False,
    )
    op.create_index(
        op.f("ix_employee_full_name"), "employee", ["full_name"], unique=False
    )
    op.create_index(op.f("ix_employee_id"), "employee", ["id"], unique=False)
    op.create_index(
        op.f("ix_employee_id_chief"), "employee", ["id_chief"], unique=False
    )
    op.create_index(
        op.f("ix_employee_job_title"), "employee", ["job_title"], unique=False
    )
    op.create_index(op.f("ix_employee_salary"), "employee", ["salary"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_employee_salary"), table_name="employee")
    op.drop_index(op.f("ix_employee_job_title"), table_name="employee")
    op.drop_index(op.f("ix_employee_id_chief"), table_name="employee")
    op.drop_index(op.f("ix_employee_id"), table_name="employee")
    op.drop_index(op.f("ix_employee_full_name"), table_name="employee")
    op.drop_index(op.f("ix_employee_employment_date"), table_name="employee")
    op.drop_table("employee")
    # ### end Alembic commands ###