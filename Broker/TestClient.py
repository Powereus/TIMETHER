import Broker
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from Broker.TestWrapper import TestWrapper
import queue
class TestClient(EClient):

    def __init__(self, wrapper: TestWrapper):
        EClient.__init__(self, wrapper)
    def get_data(self):
        contract = Contract()
        contract.symbol = "INGA"
        contract.secType= "STK"
        contract.currency = "EUR"
        contract.exchange = "AEB"
        #self.reqHistoricalTicks(106,contract,"20190307 21:39:33","",1,"TRADES",1,True,[])
        self.reqFundamentalData(1233,contract,"ReportsFinSummary", [])
        self.reqContractDetails(20,contract)

    def run(self):
        super().run()


