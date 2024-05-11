# FakeNETSTAT
## When a tech support scammer connects to your computer, they tend to use a program called netstat. This is a legitimate program, it can be found in %windir% (Windows Directory)\System32\NETSTAT.EXE. However a scammer will use this and say the connections are hackers even though they are likely to be normal.

# Download FakeNETSTAT Versions:
## - https://github.com/bazthedev/FakeNETSTAT/releases/tag/1.0
# Setup
## Either use the backup (REAL_NETSTAT.exe or copy the NETSTAT.exe from C:\Windows\System32\ to a safe location)
## Using the backup from REAL_NETSTAT.exe:
### - Open a command window as administrator by pressing the windows key and typing cmd then right click and press run as administrator
### - Say yes to UAC
### - If you cannot see C:\Windows\System32, then type `c: && cd C:\Windows\System32`
### - Type `del NETSTAT.EXE`
### - Now copy your fake netstat to the same path (C:\Windows\System32)

## Creating a backup:
### - Press the windows key and type `explorer C:\Windows\System32`
### - Find NETSTAT.EXE
### - Copy it to a location you will remember
### - Now copy this NETSTAT to the same path

#### Please note this repository will continue to receive updates
