from pysnmp.hlapi import *
import datetime
import sys 
import os
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/"))
from OOP_Switch import Switches

info_SW = "172.30.200.134"
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

snmp_get(UdpTransportTarget(('172.30.200.134', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_WNSC = check_status_sw(info_SW[1])

while(status_WNSC != 0):
    snmp_get(UdpTransportTarget(('172.30.200.134', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_WNSC=info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.200.134', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.4.20.1.1.172.30.200.134')))
    ip_WNSC=info_SW[1]    
    
    snmp_get(UdpTransportTarget(('172.30.200.134', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.1.57.0')))
    cpu_WNSC=info_SW[1]    

    snmp_get(UdpTransportTarget(('172.30.200.134', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portInbound_port_WNSC = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.200.134', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.6.10')))
    portInbound_packet_WNSC = info_SW[1]
    portInbound_WNSC = portInbound_port_WNSC+":"+portInbound_packet_WNSC

    snmp_get(UdpTransportTarget(('172.30.200.134', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portOutbound_port_WNSC = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.200.134', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.8.10')))
    portOutbound_packet_WNSC = info_SW[1]
    portOutbound_WNSC = portOutbound_port_WNSC+":"+portOutbound_packet_WNSC

    snmp_get(UdpTransportTarget(('172.30.200.134', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.3.0')))
    log_WNSC = uptime(info_SW[1])  
 
    snmp_getnext(UdpTransportTarget(('172.30.200.134', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.9.23.1.2.1.1.6')))
    portStatus_WNSC = MY_CONSTANT(implement(temp))
    temp.clear()

    break


while(status_WNSC == 0):
    name_WNSC = info_SW
    ip_WNSC = info_SW
    cpu_WNSC = info_SW
    portInbound_WNSC = info_SW
    portOutbound_WNSC = info_SW
    log_WNSC = info_SW
    portStatus_WNSC = info_SW

    break

WNSC = Switches(name_WNSC,ip_WNSC,cpu_WNSC,portStatus_WNSC,portInbound_WNSC,portOutbound_WNSC,log_WNSC)
WNSC.insert_SW("WNSC",20.054618, 99.911259)# 3 arguments
UPDATE_WNSC = [name_WNSC,ip_WNSC,cpu_WNSC,portStatus_WNSC,portInbound_WNSC,portOutbound_WNSC,log_WNSC,status_WNSC]# 7 arguments
WNSC.update_SW("WNSC",UPDATE_WNSC)# 2 arguments
WNSC.update_Location("WNSC",20.054618, 99.911259)# 3 arguments
#WNSC.delete_SW("WNSC")# 1 argument