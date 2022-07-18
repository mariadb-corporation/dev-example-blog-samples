import wmi

wmidata = wmi.WMI()

for os in wmidata.Win32_OperatingSystem():
    print(os.caption, "Build:", os.buildnumber)


for d in wmidata.Win32_Product():
    print(d)