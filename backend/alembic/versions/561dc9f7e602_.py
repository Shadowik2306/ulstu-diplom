"""empty message

Revision ID: 561dc9f7e602
Revises: 01e0211a669f
Create Date: 2025-02-27 22:17:06.718927

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "561dc9f7e602"
down_revision: Union[str, None] = "01e0211a669f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
