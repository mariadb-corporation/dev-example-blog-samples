import wmi

wmidata = wmi.WMI()

for os in wmidata.Win32_OperatingSystem():
    print(os.caption, "Build:", os.buildnumber)

p: list = wmidata.Win32_NetworkAdapter()


for card in p:

    if card.NetEnabled:
        print(card.caption, '|', card.NetEnabled, '|', card.MacAddress)
