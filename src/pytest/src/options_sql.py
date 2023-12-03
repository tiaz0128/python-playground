from sqlalchemy import select

from interface_sql import InterfaceSQL
from history import HistoryMst


class MonthlyReportOptionsSQL(InterfaceSQL):
    def lookup_query(self, sql_name: str):
        if sql_name == "diagnosis_month_year":
            return self.select_diagnosis_month_year

        raise Exception(f"Query for {sql_name} is not implemented.")

    def select_diagnosis_month_year(self, login_user, **filter):
        stmt = select(
            HistoryMst,
        ).select_from(HistoryMst)

        return stmt
