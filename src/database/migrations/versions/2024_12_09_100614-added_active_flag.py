"""Added active flag

Revision ID: 6e0d663a1340
Revises: b15d1e0c2324
Create Date: 2024-12-09 10:06:14.107808+00:00

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6e0d663a1340"
down_revision: Union[str, None] = "b15d1e0c2324"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column(
            "is_active",
            sa.Boolean(),
            server_default=sa.text("1"),
            nullable=False,
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "is_active")
    # ### end Alembic commands ###
