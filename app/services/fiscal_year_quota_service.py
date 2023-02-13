from app.db.data_platform import DataPlatform
import pandas as pd

class FiscalYearQuotaService(object):
    @staticmethod
    def getQuarterlyFiscalYearProductionQuotas() -> pd.DataFrame:
        fiscal_year_prod_quotas = DataPlatform.getQuarterlyProductionQuotaForFiscalYear()
        quarters = fiscal_year_prod_quotas[0]
        quotas = fiscal_year_prod_quotas[1]
        return pd.DataFrame({
            "Quarters": quarters,
            "Quotas": quotas
        })