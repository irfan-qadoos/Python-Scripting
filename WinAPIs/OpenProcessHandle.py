import ctypes


k_handle = ctypes.WinDLL("Kernel32.dll")

PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFFF)

dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False

try:
    get_pid = int(input("Enter PID: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

dwProcessId = get_pid

print(f"Process ID: {dwProcessId}")

response = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)

if response <= 0:
    error = k_handle.GetLastError()
    print(f"There is an error with status code: {error}")
else:
    print(f"Handler created: {response}")
