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


name_D1FL1SW014 = info_SW
interface_D1FL1SW014 = info_SW
name_D1FL1SW066 = info_SW
interface_D1FL1SW066 = info_SW
#-------------------------------------------------snmp_get Get Interfaces 12---------------------------------------------------------------------#
snmp_get(UdpTransportTarget(('172.30.200.31', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_D1FL1SW014 = check_status_sw(info_SW[1])

snmp_get(UdpTransportTarget(('172.30.200.32', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_D1FL1SW066 = check_status_sw(info_SW[1])

INTERFACE_D1FL1SW014_D1FL1SW066 = Interfaces(name_D1FL1SW014,interface_D1FL1SW014,name_D1FL1SW066,interface_D1FL1SW066)
while(status_D1FL1SW014 != 0 or status_D1FL1SW066 != 0):
    snmp_get(UdpTransportTarget(('172.30.200.31', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_D1FL1SW014=info_SW[1]
    snmp_get(UdpTransportTarget(('172.30.200.31', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.9'))  )
    interfaceName_D1FL1SW014 = info_SW[1]
    snmp_get(UdpTransportTarget(('172.30.200.31', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.7.9'))  )
    interfaceStatus_D1FL1SW014 = info_SW[1]
    interface_D1FL1SW014 = state_name(interfaceName_D1FL1SW014) +":"+ state_port(interfaceStatus_D1FL1SW014)
    
    info_SW = "Down"

    snmp_get(UdpTransportTarget(('172.30.200.32', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_D1FL1SW066=info_SW[1]
    snmp_get(UdpTransportTarget(('172.30.200.32', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.9'))  )
    interfaceName_D1FL1SW066 = info_SW[1]
    snmp_get(UdpTransportTarget(('172.30.200.32', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.7.9'))  )
    interfaceStatus_D1FL1SW066 = info_SW[1]
    interface_D1FL1SW066 = state_name(interfaceName_D1FL1SW066) +":"+ state_port(interfaceStatus_D1FL1SW066)
    
    
    UPDATE_INT = [name_D1FL1SW014,interface_D1FL1SW014,name_D1FL1SW066,interface_D1FL1SW066]# 2 arguments
    INTERFACE_D1FL1SW014_D1FL1SW066.insert_INT("D1FL1SW014_D1FL1SW066",20.047653, 99.893832,20.047434, 99.893743)# 5 arguments
    INTERFACE_D1FL1SW014_D1FL1SW066.update_Point("D1FL1SW014_D1FL1SW066",20.047653, 99.893832,20.047434, 99.893743)# 5 arguments
    INTERFACE_D1FL1SW014_D1FL1SW066.update_INT("D1FL1SW014_D1FL1SW066",UPDATE_INT)# 2 arguments
    break
    

while(status_D1FL1SW014 == 0 or status_D1FL1SW066 == 0):
    interface_D1FL1SW014 = info_SW
    interface_D1FL1SW066 = info_SW
    INTERFACE_D1FL1SW014_D1FL1SW066.delete_INT("D1FL1SW014_D1FL1SW066")# 1 arguments
    break









