from pysnmp.hlapi import *
import datetime
import sys 
import os
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/"))
from OOP_Switch import Switches

info_SW = "172.30.200.148"
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

snmp_get(UdpTransportTarget(('172.30.200.148', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_A13 = check_status_sw(info_SW[1])

while(status_A13 != 0):
    snmp_get(UdpTransportTarget(('172.30.200.148', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_A13=info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.200.148', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.4.20.1.1.172.30.200.148')))
    ip_A13=info_SW[1]    
    
    snmp_get(UdpTransportTarget(('172.30.200.148', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.1.57.0')))
    cpu_A13=info_SW[1]    

    snmp_get(UdpTransportTarget(('172.30.200.148', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portInbound_port_A13 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.200.148', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.6.10')))
    portInbound_packet_A13 = info_SW[1]
    portInbound_A13 = portInbound_port_A13+":"+portInbound_packet_A13

    snmp_get(UdpTransportTarget(('172.30.200.148', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portOutbound_port_A13 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.200.148', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.8.10')))
    portOutbound_packet_A13 = info_SW[1]
    portOutbound_A13 = portOutbound_port_A13+":"+portOutbound_packet_A13

    snmp_get(UdpTransportTarget(('172.30.200.148', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.3.0')))
    log_A13 = uptime(info_SW[1])  
 
    snmp_getnext(UdpTransportTarget(('172.30.200.148', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.9.23.1.2.1.1.6')))
    portStatus_A13 = MY_CONSTANT(implement(temp))
    temp.clear()

    break


while(status_A13 == 0):
    name_A13 = info_SW
    ip_A13 = info_SW
    cpu_A13 = info_SW
    portInbound_A13 = info_SW
    portOutbound_A13 = info_SW
    log_A13 = info_SW
    portStatus_A13 = info_SW

    break

A13 = Switches(name_A13,ip_A13,cpu_A13,portStatus_A13,portInbound_A13,portOutbound_A13,log_A13)
A13.insert_SW("A13",20.053262, 99.894850)# 3 arguments
UPDATE_A13 = [name_A13,ip_A13,cpu_A13,portStatus_A13,portInbound_A13,portOutbound_A13,log_A13,status_A13]# 7 arguments
A13.update_SW("A13",UPDATE_A13)# 2 arguments
A13.update_Location("A13",A13.lat, A13.lng)# 3 arguments
# A13.delete_SW("A13")# 1 argument

