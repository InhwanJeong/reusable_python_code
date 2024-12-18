class User(
    Base,
    UUIDMixin,
    TimestampMixin,
):
    __tablename__ = "prompt_metadata"

    email: Mapped[str] = mapped_column(
        unique=True,
    )
    password: Mapped[str] = mapped_column(
        String(length=128),
    )
    name: Mapped[str] = mapped_column(
        String(length=20),
    )
    role: Mapped[str] = mapped_column(
        String(length=20),
    )
    last_login: Mapped[datetime.datetime | None] = mapped_column(
        DateTime(timezone=True),
    )