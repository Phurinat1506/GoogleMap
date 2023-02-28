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


name_E2FL2SW016 = info_SW
interface_E2FL2SW016 = info_SW
name_E2FL2SW073 = info_SW
interface_E2FL2SW073 = info_SW
#-------------------------------------------------snmp_get Get Interfaces 12---------------------------------------------------------------------#
snmp_get(UdpTransportTarget(('172.30.200.51', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_E2FL2SW016 = check_status_sw(info_SW[1])

snmp_get(UdpTransportTarget(('172.30.200.52', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_E2FL2SW073 = check_status_sw(info_SW[1])

INTERFACE_E2FL2SW016_E2FL2SW073 = Interfaces(name_E2FL2SW016,interface_E2FL2SW016,name_E2FL2SW073,interface_E2FL2SW073)
while(status_E2FL2SW016 != 0 or status_E2FL2SW073 != 0):
    snmp_get(UdpTransportTarget(('172.30.200.51', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_E2FL2SW016=info_SW[1]
    snmp_get(UdpTransportTarget(('172.30.200.51', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.9'))  )
    interfaceName_E2FL2SW016 = info_SW[1]
    snmp_get(UdpTransportTarget(('172.30.200.51', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.7.9'))  )
    interfaceStatus_E2FL2SW016 = info_SW[1]
    interface_E2FL2SW016 = state_name(interfaceName_E2FL2SW016) +":"+ state_port(interfaceStatus_E2FL2SW016)
    
    info_SW = "Down"

    snmp_get(UdpTransportTarget(('172.30.200.52', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_E2FL2SW073=info_SW[1]
    snmp_get(UdpTransportTarget(('172.30.200.52', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.9'))  )
    interfaceName_E2FL2SW073 = info_SW[1]
    snmp_get(UdpTransportTarget(('172.30.200.52', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.7.9'))  )
    interfaceStatus_E2FL2SW073 = info_SW[1]
    interface_E2FL2SW073 = state_name(interfaceName_E2FL2SW073) +":"+ state_port(interfaceStatus_E2FL2SW073)
    
    
    UPDATE_INT = [name_E2FL2SW016,interface_E2FL2SW016,name_E2FL2SW073,interface_E2FL2SW073]# 2 arguments
    INTERFACE_E2FL2SW016_E2FL2SW073.insert_INT("E2FL2SW016_E2FL2SW073",20.044349, 99.893669,20.044435, 99.893342)# 5 arguments
    INTERFACE_E2FL2SW016_E2FL2SW073.update_Point("E2FL2SW016_E2FL2SW073",20.044349, 99.893669,20.044435, 99.893342)# 5 arguments
    INTERFACE_E2FL2SW016_E2FL2SW073.update_INT("E2FL2SW016_E2FL2SW073",UPDATE_INT)# 2 arguments
    break
    

while(status_E2FL2SW016 == 0 or status_E2FL2SW073 == 0):
    interface_E2FL2SW016 = info_SW
    interface_E2FL2SW073 = info_SW
    INTERFACE_E2FL2SW016_E2FL2SW073.delete_INT("E2FL2SW016_E2FL2SW073")# 1 arguments
    break









