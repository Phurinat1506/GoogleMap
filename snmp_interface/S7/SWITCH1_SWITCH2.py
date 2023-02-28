from pysnmp.hlapi import *
import sys 
import os
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/"))
from OOP_Interface import Interfaces
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/S7/"))
from SWITCH1 import SWITCH1
from SWITCH2 import SWITCH2


info_SW = ""
def check_status_sw(state):
    while(True):
        state=str(state)
        if state == "No Such Instance currently exists at this OID":
            state = 1
        else:
            state = 0
        return state
def state_port(state):
    while(True):
        state=str(state)
        if state == "1":
            state = "Up"
        elif state == "2":
            state = "Down"
        elif state == "3":
            state = "testing"
        elif state == "4":
            state = "unknown"
        elif state == "5":
            state = "dormant"
        elif state == "6":
            state = "notPresent"
        elif state == "7":
            state = "lowerLayerDown"
        else :
            state = "Down"
        return state 
def state_name(state):
    if state == "2":
        return "Not Connected"
    else:
        return state
def snmp_get(ip,value_oid):
    for (errorIndication,
        errorStatus,
        errorIndex,
        get_SW) in getCmd(SnmpEngine(),
                          CommunityData('public'),
                          ip,
                          ContextData(),
                          value_oid,
                          lookupMib=False):

        if errorIndication:
            print(errorIndication)
            
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and get_SW[int(errorIndex) - 1][0] or '?'))
            break
        else:
            for varBind in get_SW:
                global info_SW
                info_SW=[x.prettyPrint() for x in varBind]
                print(info_SW[1])


name_SWITCH1 = info_SW
interface_SWITCH1 = info_SW
name_SWITCH2 = info_SW
interface_SWITCH2 = info_SW
#-------------------------------------------------snmp_get Get Interfaces 12---------------------------------------------------------------------#
snmp_get(UdpTransportTarget(('10.1.199.200', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_SWITCH1 = check_status_sw(info_SW[1])

snmp_get(UdpTransportTarget(('10.1.199.201', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_SWITCH2 = check_status_sw(info_SW[1])

INTERFACE_SWITCH1_SWITCH2 = Interfaces(name_SWITCH1,interface_SWITCH1,name_SWITCH2,interface_SWITCH2)
while(status_SWITCH1 != 0 or status_SWITCH2 != 0):
    snmp_get(UdpTransportTarget(('10.1.199.200', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_SWITCH1=info_SW[1]
    snmp_get(UdpTransportTarget(('10.1.199.200', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.9'))  )
    interfaceName_SWITCH1 = info_SW[1]
    snmp_get(UdpTransportTarget(('10.1.199.200', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.7.9'))  )
    interfaceStatus_SWITCH1 = info_SW[1]
    interface_SWITCH1 = state_name(interfaceName_SWITCH1) +":"+ state_port(interfaceStatus_SWITCH1)

    info_SW = "Down"
    
    snmp_get(UdpTransportTarget(('10.1.199.201', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_SWITCH2=info_SW[1]
    snmp_get(UdpTransportTarget(('10.1.199.201', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.9'))  )
    interfaceName_SWITCH2 = info_SW[1]
    snmp_get(UdpTransportTarget(('10.1.199.201', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.7.9'))  )
    interfaceStatus_SWITCH2 = info_SW[1]
    interface_SWITCH2 = state_name(interfaceName_SWITCH2) +":"+ state_port(interfaceStatus_SWITCH2)
    
    
    UPDATE_INT = [name_SWITCH1,interface_SWITCH1,name_SWITCH2,interface_SWITCH2]# 2 arguments
    INTERFACE_SWITCH1_SWITCH2.insert_INT("SWITCH1_SWITCH2",SWITCH1.lat, SWITCH1.lng,SWITCH2.lat,SWITCH2.lng)# 5 arguments
    INTERFACE_SWITCH1_SWITCH2.update_Point("SWITCH1_SWITCH2",SWITCH1.lat, SWITCH1.lng,SWITCH2.lat,SWITCH2.lng)# 5 arguments
    INTERFACE_SWITCH1_SWITCH2.update_INT("SWITCH1_SWITCH2",UPDATE_INT)# 2 arguments
    break
    

while(status_SWITCH1 == 0 or status_SWITCH2 == 0):
    interface_SWITCH1 = info_SW
    interface_SWITCH2 = info_SW
    INTERFACE_SWITCH1_SWITCH2.delete_INT("SWITCH1_SWITCH2")# 1 arguments
    break









