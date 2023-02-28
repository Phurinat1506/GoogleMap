from pysnmp.hlapi import *
import datetime
import sys 
import os
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/"))
from OOP_Switch import Switches

info_SW = "172.30.200.91"
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

snmp_get(UdpTransportTarget(('172.30.200.91', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_HOSFL1SW038 = check_status_sw(info_SW[1])

while(status_HOSFL1SW038 != 0):
    snmp_get(UdpTransportTarget(('172.30.200.91', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_HOSFL1SW038=info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.200.91', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.4.20.1.1.172.30.200.91')))
    ip_HOSFL1SW038=info_SW[1]    
    
    snmp_get(UdpTransportTarget(('172.30.200.91', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.1.57.0')))
    cpu_HOSFL1SW038=info_SW[1]    

    snmp_get(UdpTransportTarget(('172.30.200.91', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portInbound_port_HOSFL1SW038 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.200.91', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.6.10')))
    portInbound_packet_HOSFL1SW038 = info_SW[1]
    portInbound_HOSFL1SW038 = portInbound_port_HOSFL1SW038+":"+portInbound_packet_HOSFL1SW038

    snmp_get(UdpTransportTarget(('172.30.200.91', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portOutbound_port_HOSFL1SW038 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.200.91', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.8.10')))
    portOutbound_packet_HOSFL1SW038 = info_SW[1]
    portOutbound_HOSFL1SW038 = portOutbound_port_HOSFL1SW038+":"+portOutbound_packet_HOSFL1SW038

    snmp_get(UdpTransportTarget(('172.30.200.91', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.3.0')))
    log_HOSFL1SW038 = uptime(info_SW[1])  
 
    snmp_getnext(UdpTransportTarget(('172.30.200.91', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.9.23.1.2.1.1.6')))
    portStatus_HOSFL1SW038 = MY_CONSTANT(implement(temp))
    temp.clear()

    break


while(status_HOSFL1SW038 == 0):
    name_HOSFL1SW038 = info_SW
    ip_HOSFL1SW038 = info_SW
    cpu_HOSFL1SW038 = info_SW
    portInbound_HOSFL1SW038 = info_SW
    portOutbound_HOSFL1SW038 = info_SW
    log_HOSFL1SW038 = info_SW
    portStatus_HOSFL1SW038 = info_SW

    break

HOSFL1SW038 = Switches(name_HOSFL1SW038,ip_HOSFL1SW038,cpu_HOSFL1SW038,portStatus_HOSFL1SW038,portInbound_HOSFL1SW038,portOutbound_HOSFL1SW038,log_HOSFL1SW038)
HOSFL1SW038.insert_SW("HOSFL1SW038",20.041196, 99.894032)# 3 arguments
UPDATE_HOSFL1SW038 = [name_HOSFL1SW038,ip_HOSFL1SW038,cpu_HOSFL1SW038,portStatus_HOSFL1SW038,portInbound_HOSFL1SW038,portOutbound_HOSFL1SW038,log_HOSFL1SW038,status_HOSFL1SW038]# 7 arguments
HOSFL1SW038.update_SW("HOSFL1SW038",UPDATE_HOSFL1SW038)# 2 arguments
HOSFL1SW038.update_Location("HOSFL1SW038",20.041196, 99.894032)# 3 arguments
#HOSFL1SW038.delete_SW("HOSFL1SW038")# 1 argument