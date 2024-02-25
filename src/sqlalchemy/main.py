from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import Session

from model import Base, Test, Test2

engine = create_engine(
    "mariadb+mariadbconnector://root:1234qwer!@127.0.0.1:3306/test3",
)
Base.metadata.create_all(engine)

session = Session(bind=engine)

stmt = select(
    Test.id,
    Test.desc,
    Test2.desc,
).join(Test2, Test2.id == Test.id)

r = session.execute(stmt).all()

for rw in r:
    print(rw)
