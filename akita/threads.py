from threading import Thread, Lock
import array as arr
import ctypes
import time

lock = Lock()

def dump_array(array_obj, bytes_per_line=16):
    with lock:
        base_addr, length = array_obj.buffer_info()
        itemsize = array_obj.itemsize
        total_bytes = length * itemsize
        
        raw = ctypes.string_at(base_addr, total_bytes)
        
        print(f"\n=== Dump array('{array_obj.typecode}') ===")
        print(f"Endereço base: {hex(base_addr)} | Itens: {length} | Itemsize: {itemsize} bytes")
        print(f"Valores      : {list(array_obj)}\n")
        
        # Mostra endereço de cada item
        print("Endereços individuais dos itens:")
        for i in range(length):
            item_addr = base_addr + (i * itemsize)
            value = array_obj[i]
            print(f"  numbers[{i}] = {value:<8} → endereço: {hex(item_addr)}")
        print()
        
        # Hex dump do buffer completo
        print("Hex dump do buffer:")
        for i in range(0, total_bytes, bytes_per_line):
            chunk = raw[i:i + bytes_per_line]
            hexs = ' '.join(f'{b:02x}' for b in chunk)
            text = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
            print(f"{hex(base_addr + i):<12}  {hexs:<48}  |{text}|")


numbers = arr.array('I')

print(f"Endereço do objeto Python: {hex(id(numbers))}\n")

def func1():
    for i in range(5):
        numbers.append(i * 10)
        time.sleep(0.05)
    dump_array(numbers)

def func2():
    for i in range(5, 10):
        numbers.append(i * 10)
        time.sleep(0.05)
    dump_array(numbers)


t1 = Thread(target=func1)
t2 = Thread(target=func2)
t1.start()
t2.start()


print("\n=== Dump FINAL ===")
dump_array(numbers)