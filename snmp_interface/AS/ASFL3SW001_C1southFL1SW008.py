from pysnmp.hlapi import *
import sys 
import os
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/"))
from OOP_Interface import Interfaces

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
                          CommunityData('mfunet'),
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


name_ASFL3SW001 = info_SW
interface_ASFL3SW001 = info_SW
name_C1SOUTHFL1SW008 = info_SW
interface_C1SOUTHFL1SW008 = info_SW
#-------------------------------------------------snmp_get Get Interfaces 12---------------------------------------------------------------------#
snmp_get(UdpTransportTarget(('172.31.255.255', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_ASFL3SW001 = check_status_sw(info_SW[1])

snmp_get(UdpTransportTarget(('172.31.255.16', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_C1SOUTHFL1SW008 = check_status_sw(info_SW[1])

INTERFACE_ASFL3SW001_C1SOUTHFL1SW008 = Interfaces(name_ASFL3SW001,interface_ASFL3SW001,name_C1SOUTHFL1SW008,interface_C1SOUTHFL1SW008)
while(status_ASFL3SW001 != 0 or status_C1SOUTHFL1SW008 != 0):
    snmp_get(UdpTransportTarget(('172.31.255.255', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_ASFL3SW001=info_SW[1]
    snmp_get(UdpTransportTarget(('172.31.255.255', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.9'))  )
    interfaceName_ASFL3SW001 = info_SW[1]
    snmp_get(UdpTransportTarget(('172.31.255.255', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.7.9'))  )
    interfaceStatus_ASFL3SW001 = info_SW[1]
    interface_ASFL3SW001 = state_name(interfaceName_ASFL3SW001) +":"+ state_port(interfaceStatus_ASFL3SW001)
    
    info_SW = "Down"

    snmp_get(UdpTransportTarget(('172.31.255.16', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_C1SOUTHFL1SW008=info_SW[1]
    snmp_get(UdpTransportTarget(('172.31.255.16', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.9'))  )
    interfaceName_C1SOUTHFL1SW008 = info_SW[1]
    snmp_get(UdpTransportTarget(('172.31.255.16', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.7.9'))  )
    interfaceStatus_C1SOUTHFL1SW008 = info_SW[1]
    interface_C1SOUTHFL1SW008 = state_name(interfaceName_C1SOUTHFL1SW008) +":"+ state_port(interfaceStatus_C1SOUTHFL1SW008)
    
    
    UPDATE_INT = [name_ASFL3SW001,interface_ASFL3SW001,name_C1SOUTHFL1SW008,interface_C1SOUTHFL1SW008]# 2 arguments
    INTERFACE_ASFL3SW001_C1SOUTHFL1SW008.insert_INT("ASFL3SW001_C1SOUTHFL1SW008",20.046154, 99.893680,20.044739, 99.895307)# 5 arguments
    INTERFACE_ASFL3SW001_C1SOUTHFL1SW008.update_Point("ASFL3SW001_C1SOUTHFL1SW008",20.046154, 99.893680,20.044739, 99.895307)# 5 arguments
    INTERFACE_ASFL3SW001_C1SOUTHFL1SW008.update_INT("ASFL3SW001_C1SOUTHFL1SW008",UPDATE_INT)# 2 arguments
    break
    

while(status_ASFL3SW001 == 0 or status_C1SOUTHFL1SW008 == 0):
    interface_ASFL3SW001 = info_SW
    interface_C1SOUTHFL1SW008 = info_SW
    INTERFACE_ASFL3SW001_C1SOUTHFL1SW008.delete_INT("ASFL3SW001_C1SOUTHFL1SW008")# 1 arguments
    break









