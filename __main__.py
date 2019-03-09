from Broker.TestWrapper import TestWrapper
from Broker.TestClient import TestClient

if __name__ == '__main__':
    wrapper = TestWrapper()
    client = TestClient(wrapper)
    client.connect("127.0.0.1", 7496, 10)
    ticker = client.get_data()
    client.run()



