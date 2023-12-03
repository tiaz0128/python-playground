import pytest
import logging

# from main import DatabaseTest
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


@pytest.fixture(scope="function", name="session")
def setup_database():
    # 데이터베이스 연결 설정
    logging.info("DB connection")

    try:
        engine = create_engine(
            "mysql+mysqlconnector://root:1234qwer!@127.0.0.1/dclo",
            echo=False,
        )
        session = Session(engine)

        yield session

        session.rollback()
        session.close()

    except Exception as e:
        logging.error(e)

    # 데이터베이스 연결 종료
    logging.info("DB closed")
