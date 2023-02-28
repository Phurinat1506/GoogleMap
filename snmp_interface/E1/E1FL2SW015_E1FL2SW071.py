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


name_E1FL2SW015 = info_SW
interface_E1FL2SW015 = info_SW
name_E1FL2SW071 = info_SW
interface_E1FL2SW071 = info_SW
#-------------------------------------------------snmp_get Get Interfaces 12---------------------------------------------------------------------#
snmp_get(UdpTransportTarget(('172.30.200.41', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_E1FL2SW015 = check_status_sw(info_SW[1])

snmp_get(UdpTransportTarget(('172.30.200.46', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_E1FL2SW071 = check_status_sw(info_SW[1])

INTERFACE_E1FL2SW015_E1FL2SW071 = Interfaces(name_E1FL2SW015,interface_E1FL2SW015,name_E1FL2SW071,interface_E1FL2SW071)
while(status_E1FL2SW015 != 0 or status_E1FL2SW071 != 0):
    snmp_get(UdpTransportTarget(('172.30.200.41', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_E1FL2SW015=info_SW[1]
    snmp_get(UdpTransportTarget(('172.30.200.41', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.9'))  )
    interfaceName_E1FL2SW015 = info_SW[1]
    snmp_get(UdpTransportTarget(('172.30.200.41', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.7.9'))  )
    interfaceStatus_E1FL2SW015 = info_SW[1]
    interface_E1FL2SW015 = state_name(interfaceName_E1FL2SW015) +":"+ state_port(interfaceStatus_E1FL2SW015)
    
    info_SW = "Down"

    snmp_get(UdpTransportTarget(('172.30.200.46', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_E1FL2SW071=info_SW[1]
    snmp_get(UdpTransportTarget(('172.30.200.46', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.9'))  )
    interfaceName_E1FL2SW071 = info_SW[1]
    snmp_get(UdpTransportTarget(('172.30.200.46', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.7.9'))  )
    interfaceStatus_E1FL2SW071 = info_SW[1]
    interface_E1FL2SW071 = state_name(interfaceName_E1FL2SW071) +":"+ state_port(interfaceStatus_E1FL2SW071)
    
    
    UPDATE_INT = [name_E1FL2SW015,interface_E1FL2SW015,name_E1FL2SW071,interface_E1FL2SW071]# 2 arguments
    INTERFACE_E1FL2SW015_E1FL2SW071.insert_INT("E1FL2SW015_E1FL2SW071",20.045594, 99.893632,20.045415, 99.893898)# 5 arguments
    INTERFACE_E1FL2SW015_E1FL2SW071.update_Point("E1FL2SW015_E1FL2SW071",20.045594, 99.893632,20.045415, 99.893898)# 5 arguments
    INTERFACE_E1FL2SW015_E1FL2SW071.update_INT("E1FL2SW015_E1FL2SW071",UPDATE_INT)# 2 arguments
    break
    

while(status_E1FL2SW015 == 0 or status_E1FL2SW071 == 0):
    interface_E1FL2SW015 = info_SW
    interface_E1FL2SW071 = info_SW
    INTERFACE_E1FL2SW015_E1FL2SW071.delete_INT("E1FL2SW015_E1FL2SW071")# 1 arguments
    break









