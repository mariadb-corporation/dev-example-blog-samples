from typing import List

from ms_active_directory import ADDomain
from ms_active_directory.core.ad_objects import ADComputer
import wmi

domain = ADDomain('wca.local')
session = domain.create_session_as_user('awinterl@wca.local', 'DjWindy1971')


computers: list[ADComputer] = session.find_computers_by_attribute(attribute_name='objectclass', attribute_value='computer')
for computer in computers:
    print(computer.name, computer.class_name)
    test = wmi.WMI(computer=computer.name)
    print(test)
