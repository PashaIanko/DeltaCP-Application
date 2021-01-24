from pymodbus.exceptions import ParameterException
from Singleton import Singleton
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.constants import Defaults
from DeltaCPRegisters import DeltaCPRegisters
import numpy as np
from LoggersConfig import loggers
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


    def CreateClient(self,
            Protocol, COMPort, Timeout, StopBits, ByteSize, Parity, BaudRate ):

        loggers['Debug'].debug(f'CreateClient: Client params:\n'
                               f'{Protocol}, '
                               f'Port = {COMPort}, '
                               f'Timeout = {Timeout},\n'
                               f'StopBits = {StopBits}, '
                               f'ByteSize = {ByteSize}, '
                               f'Parity = {Parity}, '
                               f'BaudRate = {BaudRate}')
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
            loggers['Debug'].debug('DeltaCPClient: CreateClient: Parameter Exception')
        except:
            loggers['Debug'].debug('DeltaCPClient: CreateClient: Exception')

    def Connect(self):
        if(self.Client is not None):
            try:
                self.if_connected = self.Client.connect()

                # If connected successfully - we need to preset some default settings. For example, there is a
                # Radio Button, predefined regime #1 for Acceleration Deceleration time. We need to preset it after
                # connection
                if self.if_connected:
                    self.preset_parameters()
            except:
                loggers['Debug'].debug(f'DeltaCPClient: Connect: Exception {sys.exc_info()}')
                self.if_connected = False
            return self.if_connected


    def WriteRegister(self, address, value):
        try:
            self.Client.write_register(address, value)
        except:
            loggers['Debug'].debug(f'DeltaCP Client: WriteRegister: {sys.exc_info()}')

    def ReadRegister(self, address):
        try:
            hh = self.Client.read_holding_registers(address, count=1, unit=1)
            loggers['Debug'].debug(f"Register value = {hh.registers[0]}")
            return hh.registers[0]
        except:
            loggers['Debug'].debug(f'DeltaCP Client: ReadRegister: {sys.exc_info()}')

    def AdjustRegister(self, mask_bit_AND, mask_bit_OR):
        try:
            value = self.ReadRegister(DeltaCPRegisters.StartStopRegister)
            # value - это 16 битное значение. Чтобы отправить Run (стр. 514/868)
            # необходимо 0-1 биты выставить как 10
            # Старший бит должен быть 1
            # Младший бит должен быть 0
            # Чтобы отправить Stop - должно быть наоборот
            value_16bit = np.uint16(value)
            value_16bit &= mask_bit_AND
            value_16bit |= mask_bit_OR
            self.WriteRegister(DeltaCPRegisters.StartStopRegister, value_16bit)
        except:
            loggers['Debug'].debug(f'DeltaCP Client: AdjustRegister: {sys.exc_info()}')

    def SendStart(self):
        mask_bit_AND = np.uint16(65534)  # 0x1111 1111 1111 1110
        mask_bit_OR = np.uint16(2)   # 0x0000 0000 0000 0010
        self.AdjustRegister(mask_bit_AND, mask_bit_OR)

    def SendStop(self):
        mask_bit_AND = np.uint16(65533)  # 0x1111 1111 1111 1101
        mask_bit_OR = np.uint16(1)  # 0x0000 0000 0000 0001
        self.AdjustRegister(mask_bit_AND, mask_bit_OR)

    def SetFrequency(self, value):
        self.WriteRegister(DeltaCPRegisters.FrequencyCommandRegister, value)

    def RequestCurrentFrequency(self):
        res = self.ReadRegister(DeltaCPRegisters.CurrentFrequencyRegister)
        if res is not None:
            return res / 100

    def RequestSetFrequency(self):
        res = self.ReadRegister(DeltaCPRegisters.SetFrequencyRegister)
        if res is not None:
            return res / 100

    def SetRegime1(self):
        # Set regime - Acceleration time1, DecelerationTime1
        mask_bit_and = np.uint16(65343)  # 0x1111 1111 0011 1111
        mask_bit_or = np.uint16(0)  # 0x0000 0000 0000 0000
        self.AdjustRegister(mask_bit_and, mask_bit_or)

    def SetRegime2(self):
        # Set regime - Acceleration time2, DecelerationTime2
        mask_bit_and = np.uint16(65407)  # 0x1111 1111 0111 1111
        mask_bit_or = np.uint16(64)  # 0x0000 0000 0100 0000
        self.AdjustRegister(mask_bit_and, mask_bit_or)

    def SetRegime3(self):
        # Set regime - Acceleration time3, DecelerationTime3
        mask_bit_and = np.uint16(65471)  # 0x1111 1111 1011 1111
        mask_bit_or = np.uint16(128)  # 0x0000 0000 1000 0000
        self.AdjustRegister(mask_bit_and, mask_bit_or)

    def SetRegime4(self):
        # Set regime - Acceleration time4, DecelerationTime4
        mask_bit_and = np.uint16(65535)  # 0x1111 1111 1111 1111
        mask_bit_or = np.uint16(192)  # 0x0000 0000 1100 0000
        self.AdjustRegister(mask_bit_and, mask_bit_or)

    def preset_parameters(self):
        loggers['Debug'].debug(f'DeltaCPClient: preset_parameters: Setting regime1')
        loggers['Application'].debug(f'Presetting initial parameters: Acceleration time #1, Deceleration time #1')
        self.SetRegime1()


# TODO: Переделать визуализацию (чтоб два графика в едином окошке)
# TODO: Исправить баг (когда закрываешь окошко с визуализацией, вылезает баг)