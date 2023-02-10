from app.db.data_platform import DataPlatform
import pandas as pd

class FiscalYearSalesService(object):
    @staticmethod
    def getFiscalYearSales() -> pd.DataFrame:
        fiscal_year_sales = DataPlatform.getSalesDataForFiscalYear()
        months = fiscal_year_sales[0]
        salesPerMonth = fiscal_year_sales[1]
        return pd.DataFrame({
            "Month": months,
            "Sales": salesPerMonth
        })