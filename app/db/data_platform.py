class DataPlatform(object):
    @staticmethod
    def getSalesDataForFiscalYear():
        return [
            [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ],
            [1400000, 1600000, 922000, 1150000, 1720000, 2030000, 1933000, 2280000, 1770000, 1702000, 1800000, 1930000]
        ]

    @staticmethod
    def getQuarterlyProductionQuotaForFiscalYear():
        return [
            [ "Jan. - Mar.", "Apr. - Jun.", "Jul. - Sep.", "Oct. - Dec."],
            [ 220, 335, 300, 285 ]
        ]