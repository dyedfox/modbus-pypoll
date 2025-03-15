from pyModbusTCP.client import ModbusClient
import time
import sys
import ctypes

def data_process(regs, data_type):
    if data_type == -1:
        return ctypes.c_int32(regs[0]).value
    elif data_type == -2:
        combined_value = (regs[0] << 16) | regs[1]
        return ctypes.c_int32(combined_value).value
    elif data_type == 1:
        return regs[0]
    elif data_type == 2:
        return (regs[0] << 16) | regs[1]
    else:
        return None  # Changed from False to None for clarity

def main():
    success = 0
    errors = 0
    
    if len(sys.argv) < 6:
        print(">> ModbusChecker 0.3")
        print("Usage: modbus <IP address> <port> <device number> <data address> <data type/length>")
        print(" Data type/length: '-2' - I32, '2' - U32, '-1' - I16, '1' - U16")
        return
    
    host_ip = sys.argv[1]
    unit_port = sys.argv[2]
    device_id = sys.argv[3]
    register = sys.argv[4]
    data_type = int(sys.argv[5])
    
    try:
        c = ModbusClient(host=host_ip, port=int(unit_port), unit_id=int(device_id), auto_open=True)
        if not c.is_open:
            print("Error: Connection to the Modbus server failed.")
            return
            
        for i in range(100):
            try:
                regs = c.read_holding_registers(int(register), abs(data_type))
                if regs:
                    processed_data = data_process(regs, data_type)
                    print(f"[{i+1:03}] Read data: {processed_data}")
                    success += 1
                else:
                    print(f"[{i+1:03}] Warning: Empty response received.")
                    errors += 1
            except Exception as e:
                print(f"[{i+1:03}] Read error: {e}")
                errors += 1
            time.sleep(1)
            
    except Exception as e:
        print(f"Error: Connection failed - {e}")
    finally:
        if 'c' in locals() and c.is_open:
            c.close()
        
    print(f"\nSummary:\n  Success count: {success}\n  Failure count: {errors}")

if __name__ == "__main__":
    main()
