from ibapi.common import TickerId, TickAttrib
from ibapi.contract import ContractDetails
from ibapi.ticktype import TickType
from ibapi.wrapper import EWrapper;
import queue;
class TestWrapper(EWrapper):
    def __init__(self):
        EWrapper.__init__(self)

    def historicalTicks(self, reqId: int, ticks, done:bool):
        for tick in ticks:
            print("HistoricalTick. ReqId:", reqId, tick)
        return super().historicalTicks(reqId, ticks, done)

    def historicalTicksBidAsk(self, reqId:int , ticks, done:bool):
        for tick in ticks:
            print("HistoricalTickBidAsk. ReqId:", reqId, tick)
        return super().historicalTicksBidAsk(reqId, ticks, done)

    def historicalTicksLast(self, reqId:int, ticks, done:bool):
        for tick in ticks:
            print("HistoricalTickLast. ReqId:", reqId, tick)
        return super().historicalTicksLast(reqId, ticks, done)

    def tickPrice(self, reqId: TickerId, tickType: TickType, price: float, attrib: TickAttrib):
        super().tickPrice(reqId, tickType, price, attrib)

    def fundamentalData(self, reqId: TickerId, data: str):
        super().fundamentalData(reqId, data)
        print("FundamentalData. ReqId:", reqId, "Data:",data)

    def error(self, reqId: TickerId, errorCode: int, errorString: str):
        super().error(reqId, errorCode, errorString)
        print("Error. Id:", reqId, "Code:", errorCode, "Msg:", errorString)

    def winError(self, text: str, lastError: int):
        super().winError(text, lastError)

    def connectionClosed(self):
        print("Connection closed")
        super().connectionClosed()

    def nextValidId(self, orderId: int):
        print("Next valid Id:",orderId)
        super().nextValidId(orderId)

    def connectAck(self):
        print("Connection ack!")
        super().connectAck()

    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        super().contractDetails(reqId, contractDetails)
        printinstance(contractDetails)



def printinstance(inst):
    attrs = vars(inst)
    print(', '.join("%s: %s" % item for item in attrs.items()))

