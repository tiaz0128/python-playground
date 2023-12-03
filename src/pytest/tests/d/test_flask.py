from sqlalchemy import text

from src.interface_sql import InterfaceSQL
from src.options_sql import MonthlyReportOptionsSQL


def test_db_connection(capsys, session):
    result = session.execute(text("select 'hello world'"))

    word = result.scalar_one()
    print(word)
    captured = capsys.readouterr()

    assert captured.out == "hello world\n"


def test_db_select(session):
    sql: InterfaceSQL = MonthlyReportOptionsSQL()

    stmt = sql.make_stmt("diagnosis_month_year", login_user="joo_test")
    results = session.execute(stmt).all()

    assert results
