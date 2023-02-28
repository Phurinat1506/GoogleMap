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


name_S7AFL1SW009 = info_SW
interface_S7AFL1SW009 = info_SW
name_S7AFL2SW121 = info_SW
interface_S7AFL2SW121 = info_SW
#-------------------------------------------------snmp_get Get Interfaces 12---------------------------------------------------------------------#
snmp_get(UdpTransportTarget(('172.31.255.19', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_S7AFL1SW009 = check_status_sw(info_SW[1])

snmp_get(UdpTransportTarget(('172.30.208.21', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_S7AFL2SW121 = check_status_sw(info_SW[1])

INTERFACE_S7AFL1SW009_S7AFL2SW121 = Interfaces(name_S7AFL1SW009,interface_S7AFL1SW009,name_S7AFL2SW121,interface_S7AFL2SW121)
while(status_S7AFL1SW009 != 0 or status_S7AFL2SW121 != 0):
    snmp_get(UdpTransportTarget(('172.31.255.19', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_S7AFL1SW009=info_SW[1]
    snmp_get(UdpTransportTarget(('172.31.255.19', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.9'))  )
    interfaceName_S7AFL1SW009 = info_SW[1]
    snmp_get(UdpTransportTarget(('172.31.255.19', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.7.9'))  )
    interfaceStatus_S7AFL1SW009 = info_SW[1]
    interface_S7AFL1SW009 = state_name(interfaceName_S7AFL1SW009) +":"+ state_port(interfaceStatus_S7AFL1SW009)
    
    info_SW = "Down"

    snmp_get(UdpTransportTarget(('172.30.208.21', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_S7AFL2SW121=info_SW[1]
    snmp_get(UdpTransportTarget(('172.30.208.21', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.9'))  )
    interfaceName_S7AFL2SW121 = info_SW[1]
    snmp_get(UdpTransportTarget(('172.30.208.21', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.7.9'))  )
    interfaceStatus_S7AFL2SW121 = info_SW[1]
    interface_S7AFL2SW121 = state_name(interfaceName_S7AFL2SW121) +":"+ state_port(interfaceStatus_S7AFL2SW121)
    
    
    UPDATE_INT = [name_S7AFL1SW009,interface_S7AFL1SW009,name_S7AFL2SW121,interface_S7AFL2SW121]# 2 arguments
    INTERFACE_S7AFL1SW009_S7AFL2SW121.insert_INT("S7AFL1SW009_S7AFL2SW121",20.048081, 99.895151,20.048198, 99.895001)# 5 arguments
    INTERFACE_S7AFL1SW009_S7AFL2SW121.update_Point("S7AFL1SW009_S7AFL2SW121",20.048081, 99.895151,20.048198, 99.895001)# 5 arguments
    INTERFACE_S7AFL1SW009_S7AFL2SW121.update_INT("S7AFL1SW009_S7AFL2SW121",UPDATE_INT)# 2 arguments
    break
    

while(status_S7AFL1SW009 == 0 or status_S7AFL2SW121 == 0):
    interface_S7AFL1SW009 = info_SW
    interface_S7AFL2SW121 = info_SW
    INTERFACE_S7AFL1SW009_S7AFL2SW121.delete_INT("S7AFL1SW009_S7AFL2SW121")# 1 arguments
    break









