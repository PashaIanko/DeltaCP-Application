from pymodbus.exceptions import ParameterException
from Singleton import Singleton
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.constants import Defaults
Defaults.RetryOnEmpty = True
Defaults.Timeout = 5
Defaults.Retries = 5

@Singleton
class DeltaCPClient(ModbusClient):
    # Frequency Transducer Client
    def __init__(self):
        self.if_connected = False
        self.if_created = False
        self.Client = None

    def __repr__(self):
        if self.if_created == True:
            return f'method = {self.Client.method},' \
                   f'port = {self.Client.port},' \
                   f'stopbits = {self.Client.stopbits},' \
                   f'bytesize = {self.Client.bytesize},' \
                   f'parity = {self.Client.parity},' \
                   f'baudrate = {self.Client.baudrate},' \
                   f'timeout = {self.Client.timeout}'
        else:
            return 'Client is not created'

    def CreateClient(self,
            Protocol, COMPort, Timeout, StopBits, ByteSize, Parity, BaudRate ):

        print(
            Protocol, COMPort, Timeout, StopBits, ByteSize, Parity, BaudRate)
        try:
            self.Client = ModbusClient\
                (
                    method = Protocol,
                    port = COMPort,
                    timeout = Timeout,
                    stopbits = StopBits,
                    bytesize = ByteSize,
                    parity = Parity,
                    baudrate = BaudRate
                )
            self.if_created = True
        except ParameterException:
            print('parameter exception')
        except:
            print('exception')


    def Connect(self):
        if(self.Client is not None):
            try:
                self.if_connected = self.Client.connect()
            except ValueError:
                print('value error')
                self.if_connected = False
            return self.if_connected


    def SetFrequency(self, value):
        print(f'DeltaCP Client sends frequency = {value}')



# Source Code from video on Youtube:
#client = ModbusClient(
#    method = 'rtu',
#    port = 'COM4',
#    timeout = 2,
#    stopbits = 1,
#    bytesize = 8,
#    parity = 'N',
#    baudrate = 2400
#)

#while True:
   # hh = client.read_holding_registers(address = 245, count = 8, unit = 1)
   # h2 = hh.registers[7]/10

   # print(h2)