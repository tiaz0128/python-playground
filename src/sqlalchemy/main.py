from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from model.base import Base
from model.user import User
from model.address import Address


if __name__ == "__main__":
    # 메로리 DB
    engine = create_engine("sqlite:///src/sqlalchemy/test.sqlite3", echo=True)

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        spongebob = User(
            name="spongebob",
            fullname="Spongebob Squarepants",
            addresses=[Address(email_address="spongebob@sqlalchemy.org")],
        )
        sandy = User(
            name="sandy",
            fullname="Sandy Cheeks",
            addresses=[
                Address(email_address="sandy@sqlalchemy.org"),
                Address(email_address="sandy@squirrelpower.org"),
            ],
        )
        patrick = User(name="patrick", fullname="Patrick Star")
        session.add_all([spongebob, sandy, patrick])
        session.commit()
