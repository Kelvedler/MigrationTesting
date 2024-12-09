"""Added countries

Revision ID: 9eccdf8a5dc0
Revises: b15d1e0c2324
Create Date: 2024-12-09 10:26:17.934123+00:00

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9eccdf8a5dc0"
down_revision: Union[str, None] = "b15d1e0c2324"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "countries",
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_index(op.f("ix_countries_id"), "countries", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_countries_id"), table_name="countries")
    op.drop_table("countries")
    # ### end Alembic commands ###