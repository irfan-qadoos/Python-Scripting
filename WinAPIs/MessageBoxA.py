import ctypes


user_handle = ctypes.WinDLL("User32.dll")
error_handle = ctypes.WinDLL("Kernel32.dll") # For error handling

hWnd = None
lpText = "Hello World!".encode("utf-8") # Or encode("ascii")
lpCaption = "Let's go...".encode("utf-8") # Or encode("ascii")
uType = 0x00000001

response = user_handle.MessageBoxA(hWnd, lpText, lpCaption, uType)

error = error_handle.GetLastError()
if error != 0:
    print(f"Error code: {error}")
    exit(1)

if response == 1:
    print("User pressed OK")
elif response == 2:
    print("User pressed Cancel/x")
