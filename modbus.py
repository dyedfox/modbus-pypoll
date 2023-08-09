from pyModbusTCP.client import ModbusClient
import time
import sys
import ctypes

success=0
errors=0

def data_process(regs, type):
        if type == -1:
                return ctypes.c_int32(regs[0]).value
        elif type == -2:
                combined_value = (regs[0] << 16) | regs[1]
                # Interpret the 32-bit value as a signed integer
                # You can use the 'ctypes' library to handle signed integer conversion
                return ctypes.c_int32(combined_value).value
        elif type == 1:
                return regs[0]
        elif type == 2:
                return (regs[0] << 16) | regs[1]
        else:
                return False

if len(sys.argv) < 6:
        print (">> ModbusChecker 0.2")
        print ("Формат даних: адреса порт номер_пристрою регістр тип_даних")
        print ("     Тип даних: '-2' - I32, '2' - U32, '-1' - I16, '1' - U16")
else:
        host_ip = sys.argv[1]
        unit_port = sys.argv[2]
        device_id = sys.argv[3]
        register = sys.argv[4]
        datalen = int(sys.argv[5])

        try:
                c = ModbusClient(host=host_ip, port=int(unit_port), unit_id=int(device_id), auto_open=True)
        except:
                print ('Not opened')

        for i in range(0, 100, 1):
                try:
                        regs = c.read_holding_registers(int(register), abs(datalen))
                        print(data_process(regs, int(datalen)))
                        if regs != "None":
                                success+=1
                        else:
                                errors+=1
                except:
                        print("Помилка читання!")
                        errors+=1
                time.sleep(1)

        print(f"Успішних з'єднань - {str(success)}")
        print(f"Невдач - {str(errors)}")