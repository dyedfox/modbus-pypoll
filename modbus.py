from pyModbusTCP.client import ModbusClient
import time
import sys

success=0
errors=0

if len(sys.argv) < 6:
        print (">> ModbusChecker 0.2")
        print ("Формат даних: адреса порт номер_пристрою регістр довжина_даних")
else:
        host_ip = sys.argv[1]
        unit_port = sys.argv[2]
        device_id = sys.argv[3]
        register = sys.argv[4]
        datalen = sys.argv[5]

        try:
                c = ModbusClient(host=host_ip, port=int(unit_port), unit_id=int(device_id), auto_open=True)
        except:
                print ('Not opened')

        for i in range(0, 100, 1):
                try:
                        regs = c.read_holding_registers(int(register), int(datalen))
                        print (regs)
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