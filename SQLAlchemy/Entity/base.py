import uuid
import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """
        모든 엔터티의 기반이 되는 파일
        모든 엔터티에 적용되어야 하는 설정은 이곳에서 하도록 함.
    """
    pass


class IntegerIDMixin:
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )


class UUIDMixin:
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )


class TimestampMixin:
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    updated_at: Mapped[datetime.datetime | None] = mapped_column(
        DateTime(timezone=True),
        server_onupdate=func.now(),
    )
    deleted_at: Mapped[datetime.datetime | None] = mapped_column(
        DateTime(timezone=True)
    )
