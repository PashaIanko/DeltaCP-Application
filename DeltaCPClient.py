from pymodbus.exceptions import ParameterException
from Singleton import Singleton
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.constants import Defaults
from DeltaCPRegisters import DeltaCPRegisters
import numpy as np
import sys

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


    def WriteRegister(self, address, value):
        print(f'DeltaCPClient: writing {value} in register {address}')
        try:
            self.Client.write_register(address, value)
        except:
            print(sys.exc_info())

    def ReadRegister(self, address):
        hh = self.Client.read_holding_registers(address, count=1, unit=1)
        print('Результат считывания = ', hh.registers[0])
        return hh.registers[0]

    def AdjustRegister(self, mask_bit_AND, mask_bit_OR):
        try:
            value = self.ReadRegister(DeltaCPRegisters.StartStopRegister)
            # value - это 16 битное значение. Чтобы отправить Run (стр. 514/868)
            # необходимо 0-1 биты выставить как 10
            # Старший бит должен быть 1
            # Младший бит должен быть 0
            # Чтобы отправить Stop - должно быть наоборот
            print(f'type is {type(value)}, value is {value}')
            value_16bit = np.uint16(value)
            value_16bit &= mask_bit_AND
            value_16bit |= mask_bit_OR
            self.WriteRegister(DeltaCPRegisters.StartStopRegister, value_16bit)
        except:
            print(sys.exc_info())

    def SendStart(self):
        print(f'sending start command')
        mask_bit_AND = np.uint16(65534)  # 0x1111 1111 1111 1110
        mask_bit_OR = np.uint16(2)   # 0x0000 0000 0000 0010
        self.AdjustRegister(mask_bit_AND, mask_bit_OR)


    def SendStop(self):
        print(f'sending stop command')
        mask_bit_AND = np.uint16(65533)  # 0x1111 1111 1111 1101
        mask_bit_OR = np.uint16(1)  # 0x0000 0000 0000 0001
        self.AdjustRegister(mask_bit_AND, mask_bit_OR)

    def SetFrequency(self, value):
        self.WriteRegister(DeltaCPRegisters.FrequencyCommandRegister, value)

    def RequestCurrentFrequency(self):
        return self.ReadRegister(DeltaCPRegisters.CurrentFrequencyRegister) / 100

    def RequestSetFrequency(self):
        return self.ReadRegister(DeltaCPRegisters.SetFrequencyRegister) / 100







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