from pysnmp.hlapi import *
import datetime
import sys 
import os
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/"))
from OOP_Switch import Switches

info_SW = "172.30.200.121"
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

snmp_get(UdpTransportTarget(('172.30.200.121', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_FOOTBALLFL1SW236 = check_status_sw(info_SW[1])

while(status_FOOTBALLFL1SW236 != 0):
    snmp_get(UdpTransportTarget(('172.30.200.121', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_FOOTBALLFL1SW236=info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.200.121', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.4.20.1.1.172.30.200.121')))
    ip_FOOTBALLFL1SW236=info_SW[1]    
    
    snmp_get(UdpTransportTarget(('172.30.200.121', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.1.57.0')))
    cpu_FOOTBALLFL1SW236=info_SW[1]    

    snmp_get(UdpTransportTarget(('172.30.200.121', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portInbound_port_FOOTBALLFL1SW236 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.200.121', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.6.10')))
    portInbound_packet_FOOTBALLFL1SW236 = info_SW[1]
    portInbound_FOOTBALLFL1SW236 = portInbound_port_FOOTBALLFL1SW236+":"+portInbound_packet_FOOTBALLFL1SW236

    snmp_get(UdpTransportTarget(('172.30.200.121', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portOutbound_port_FOOTBALLFL1SW236 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.200.121', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.8.10')))
    portOutbound_packet_FOOTBALLFL1SW236 = info_SW[1]
    portOutbound_FOOTBALLFL1SW236 = portOutbound_port_FOOTBALLFL1SW236+":"+portOutbound_packet_FOOTBALLFL1SW236

    snmp_get(UdpTransportTarget(('172.30.200.121', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.3.0')))
    log_FOOTBALLFL1SW236 = uptime(info_SW[1])  
 
    snmp_getnext(UdpTransportTarget(('172.30.200.121', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.9.23.1.2.1.1.6')))
    portStatus_FOOTBALLFL1SW236 = MY_CONSTANT(implement(temp))
    temp.clear()

    break


while(status_FOOTBALLFL1SW236 == 0):
    name_FOOTBALLFL1SW236 = info_SW
    ip_FOOTBALLFL1SW236 = info_SW
    cpu_FOOTBALLFL1SW236 = info_SW
    portInbound_FOOTBALLFL1SW236 = info_SW
    portOutbound_FOOTBALLFL1SW236 = info_SW
    log_FOOTBALLFL1SW236 = info_SW
    portStatus_FOOTBALLFL1SW236 = info_SW

    break

FOOTBALLFL1SW236 = Switches(name_FOOTBALLFL1SW236,ip_FOOTBALLFL1SW236,cpu_FOOTBALLFL1SW236,portStatus_FOOTBALLFL1SW236,portInbound_FOOTBALLFL1SW236,portOutbound_FOOTBALLFL1SW236,log_FOOTBALLFL1SW236)
FOOTBALLFL1SW236.insert_SW("FOOTBALLFL1SW236",20.058028, 99.895531)# 3 arguments
UPDATE_FOOTBALLFL1SW236 = [name_FOOTBALLFL1SW236,ip_FOOTBALLFL1SW236,cpu_FOOTBALLFL1SW236,portStatus_FOOTBALLFL1SW236,portInbound_FOOTBALLFL1SW236,portOutbound_FOOTBALLFL1SW236,log_FOOTBALLFL1SW236,status_FOOTBALLFL1SW236]# 7 arguments
FOOTBALLFL1SW236.update_SW("FOOTBALLFL1SW236",UPDATE_FOOTBALLFL1SW236)# 2 arguments
FOOTBALLFL1SW236.update_Location("FOOTBALLFL1SW236",FOOTBALLFL1SW236.lat,FOOTBALLFL1SW236.lng)# 3 arguments
#FOOTBALLFL1SW236.delete_SW("FOOTBALLFL1SW236")# 1 argument