from pysnmp.hlapi import *
import datetime
import sys 
import os
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/"))
from OOP_Switch import Switches

info_SW = "172.30.205.71"
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

snmp_get(UdpTransportTarget(('172.30.205.71', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_BOTANICFL1SW238 = check_status_sw(info_SW[1])

while(status_BOTANICFL1SW238 != 0):
    snmp_get(UdpTransportTarget(('172.30.205.71', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_BOTANICFL1SW238=info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.205.71', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.4.20.1.1.172.30.205.71')))
    ip_BOTANICFL1SW238=info_SW[1]    
    
    snmp_get(UdpTransportTarget(('172.30.205.71', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.1.57.0')))
    cpu_BOTANICFL1SW238=info_SW[1]    

    snmp_get(UdpTransportTarget(('172.30.205.71', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portInbound_port_BOTANICFL1SW238 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.205.71', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.6.10')))
    portInbound_packet_BOTANICFL1SW238 = info_SW[1]
    portInbound_BOTANICFL1SW238 = portInbound_port_BOTANICFL1SW238+":"+portInbound_packet_BOTANICFL1SW238

    snmp_get(UdpTransportTarget(('172.30.205.71', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portOutbound_port_BOTANICFL1SW238 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.205.71', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.8.10')))
    portOutbound_packet_BOTANICFL1SW238 = info_SW[1]
    portOutbound_BOTANICFL1SW238 = portOutbound_port_BOTANICFL1SW238+":"+portOutbound_packet_BOTANICFL1SW238

    snmp_get(UdpTransportTarget(('172.30.205.71', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.3.0')))
    log_BOTANICFL1SW238 = uptime(info_SW[1])  
 
    snmp_getnext(UdpTransportTarget(('172.30.205.71', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.9.23.1.2.1.1.6')))
    portStatus_BOTANICFL1SW238 = MY_CONSTANT(implement(temp))
    temp.clear()

    break


while(status_BOTANICFL1SW238 == 0):
    name_BOTANICFL1SW238 = info_SW
    ip_BOTANICFL1SW238 = info_SW
    cpu_BOTANICFL1SW238 = info_SW
    portInbound_BOTANICFL1SW238 = info_SW
    portOutbound_BOTANICFL1SW238 = info_SW
    log_BOTANICFL1SW238 = info_SW
    portStatus_BOTANICFL1SW238 = info_SW

    break

BOTANICFL1SW238 = Switches(name_BOTANICFL1SW238,ip_BOTANICFL1SW238,cpu_BOTANICFL1SW238,portStatus_BOTANICFL1SW238,portInbound_BOTANICFL1SW238,portOutbound_BOTANICFL1SW238,log_BOTANICFL1SW238)
BOTANICFL1SW238.insert_SW("BOTANICFL1SW238",20.037868, 99.895541)# 3 arguments
UPDATE_BOTANICFL1SW238 = [name_BOTANICFL1SW238,ip_BOTANICFL1SW238,cpu_BOTANICFL1SW238,portStatus_BOTANICFL1SW238,portInbound_BOTANICFL1SW238,portOutbound_BOTANICFL1SW238,log_BOTANICFL1SW238,status_BOTANICFL1SW238]# 7 arguments
BOTANICFL1SW238.update_SW("BOTANICFL1SW238",UPDATE_BOTANICFL1SW238)# 2 arguments
BOTANICFL1SW238.update_Location("BOTANICFL1SW238",20.037868, 99.895541)# 3 arguments
#BOTANICFL1SW238.delete_SW("BOTANICFL1SW238")# 1 argument
