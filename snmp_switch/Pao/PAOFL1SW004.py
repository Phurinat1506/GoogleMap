from pysnmp.hlapi import *
import datetime
import sys 
import os
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/"))
from OOP_Switch import Switches

info_SW = "172.31.255.12"
def check_status_sw(state):
    while(True):
        state=str(state)
        if state == "No Such Instance currently exists at this OID":
            state = 1
        else:
            state = 0
        return state

def uptime(state):
    global timestamp
    try:
        state=int(state)
        timestamp = datetime.timedelta( seconds = state )
        return timestamp   
    except:
        print("No SNMP response received before timeout")
 
def snmp_get(ip,oid):
    try:
        for (errorIndication,
            errorStatus,
            errorIndex,
            get_SW) in getCmd(SnmpEngine(),
                            CommunityData('mfunet'),
                            ip,
                            ContextData(),
                            oid,
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
    except:
        pass
temp = []

def implement(var):
    try:
        var = var[0:count]
        return var
    except:
        pass 
def MY_CONSTANT(var):
    return var
def snmp_getnext(ip,value):
    try:
        for (errorIndication,
            errorStatus,
            errorIndex,
            get_SW) in nextCmd(SnmpEngine(),
                            CommunityData('mfunet'),
                            ip,
                            ContextData(),
                            value,    
                            maxRows=50,
                            ignoreNonIncreasingOid=True,               
                            lookupMib=False):
                                 
            if errorIndication:
                print(errorIndication)
                break
            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and  get_SW[int(errorIndex) - 1][0] or '?'))
                break
            else:
            
                for varBind in get_SW:
                    #print(type(varBind))
                    #print(Get_SW)
                    #print(' = '.join([x.prettyPrint() for x in varBind]))
                    global info_SW
                    global count
                    global oidsplit
                    info_SW=[x.prettyPrint() for x in varBind]
                    oidsplit=info_SW[0].split(".")
                    #print(oidsplit)
                    lastoidsplit = int(oidsplit[-3])
                    
                    if lastoidsplit == 6: 
                        print(info_SW[1])
                        temp.append(info_SW[1])
                        count = len(temp)

                    
                    #return info_SW[0]
    except:
        pass

snmp_get(UdpTransportTarget(('172.31.255.12', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_PAOFL1SW004 = check_status_sw(info_SW[1])

while(status_PAOFL1SW004 != 0):
    snmp_get(UdpTransportTarget(('172.31.255.12', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_PAOFL1SW004=info_SW[1]

    snmp_get(UdpTransportTarget(('172.31.255.12', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.4.20.1.1.172.31.255.12')))
    ip_PAOFL1SW004=info_SW[1]    
    
    snmp_get(UdpTransportTarget(('172.31.255.12', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.1.57.0')))
    cpu_PAOFL1SW004=info_SW[1]    

    snmp_get(UdpTransportTarget(('172.31.255.12', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portInbound_port_PAOFL1SW004 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.31.255.12', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.6.10')))
    portInbound_packet_PAOFL1SW004 = info_SW[1]
    portInbound_PAOFL1SW004 = portInbound_port_PAOFL1SW004+":"+portInbound_packet_PAOFL1SW004

    snmp_get(UdpTransportTarget(('172.31.255.12', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portOutbound_port_PAOFL1SW004 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.31.255.12', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.8.10')))
    portOutbound_packet_PAOFL1SW004 = info_SW[1]
    portOutbound_PAOFL1SW004 = portOutbound_port_PAOFL1SW004+":"+portOutbound_packet_PAOFL1SW004

    snmp_get(UdpTransportTarget(('172.31.255.12', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.3.0')))
    log_PAOFL1SW004 = uptime(info_SW[1])  
 
    snmp_getnext(UdpTransportTarget(('172.31.255.12', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.9.23.1.2.1.1.6')))
    portStatus_PAOFL1SW004 = MY_CONSTANT(implement(temp))
    temp.clear()

    break


while(status_PAOFL1SW004 == 0):
    name_PAOFL1SW004 = info_SW
    ip_PAOFL1SW004 = info_SW
    cpu_PAOFL1SW004 = info_SW
    portInbound_PAOFL1SW004 = info_SW
    portOutbound_PAOFL1SW004 = info_SW
    log_PAOFL1SW004 = info_SW
    portStatus_PAOFL1SW004 = info_SW

    break

PAOFL1SW004 = Switches(name_PAOFL1SW004,ip_PAOFL1SW004,cpu_PAOFL1SW004,portStatus_PAOFL1SW004,portInbound_PAOFL1SW004,portOutbound_PAOFL1SW004,log_PAOFL1SW004)
PAOFL1SW004.insert_SW("PAOFL1SW004",20.042796, 99.894924)# 3 arguments
UPDATE_PAOFL1SW004 = [name_PAOFL1SW004,ip_PAOFL1SW004,cpu_PAOFL1SW004,portStatus_PAOFL1SW004,portInbound_PAOFL1SW004,portOutbound_PAOFL1SW004,log_PAOFL1SW004,status_PAOFL1SW004]# 7 arguments
PAOFL1SW004.update_SW("PAOFL1SW004",UPDATE_PAOFL1SW004)# 2 arguments
PAOFL1SW004.update_Location("PAOFL1SW004",20.042796, 99.894924)# 3 arguments
#PAOFL1SW004.delete_SW("PAOFL1SW004")# 1 argument