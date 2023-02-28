from pysnmp.hlapi import *
import datetime
import sys 
import os
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/"))
from OOP_Switch import Switches

info_SW = "172.30.204.13"
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

snmp_get(UdpTransportTarget(('172.30.204.13', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_EPFL4SW197 = check_status_sw(info_SW[1])

while(status_EPFL4SW197 != 0):
    snmp_get(UdpTransportTarget(('172.30.204.13', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_EPFL4SW197=info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.204.13', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.4.20.1.1.172.30.204.13')))
    ip_EPFL4SW197=info_SW[1]    
    
    snmp_get(UdpTransportTarget(('172.30.204.13', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.1.57.0')))
    cpu_EPFL4SW197=info_SW[1]    

    snmp_get(UdpTransportTarget(('172.30.204.13', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portInbound_port_EPFL4SW197 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.204.13', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.6.10')))
    portInbound_packet_EPFL4SW197 = info_SW[1]
    portInbound_EPFL4SW197 = portInbound_port_EPFL4SW197+":"+portInbound_packet_EPFL4SW197

    snmp_get(UdpTransportTarget(('172.30.204.13', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portOutbound_port_EPFL4SW197 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.204.13', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.8.10')))
    portOutbound_packet_EPFL4SW197 = info_SW[1]
    portOutbound_EPFL4SW197 = portOutbound_port_EPFL4SW197+":"+portOutbound_packet_EPFL4SW197

    snmp_get(UdpTransportTarget(('172.30.204.13', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.3.0')))
    log_EPFL4SW197 = uptime(info_SW[1])  
 
    snmp_getnext(UdpTransportTarget(('172.30.204.13', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.9.23.1.2.1.1.6')))
    portStatus_EPFL4SW197 = MY_CONSTANT(implement(temp))
    temp.clear()

    break


while(status_EPFL4SW197 == 0):
    name_EPFL4SW197 = info_SW
    ip_EPFL4SW197 = info_SW
    cpu_EPFL4SW197 = info_SW
    portInbound_EPFL4SW197 = info_SW
    portOutbound_EPFL4SW197 = info_SW
    log_EPFL4SW197 = info_SW
    portStatus_EPFL4SW197 = info_SW

    break

EPFL4SW197 = Switches(name_EPFL4SW197,ip_EPFL4SW197,cpu_EPFL4SW197,portStatus_EPFL4SW197,portInbound_EPFL4SW197,portOutbound_EPFL4SW197,log_EPFL4SW197)
EPFL4SW197.insert_SW("EPFL4SW197",20.046534, 99.890843)# 3 arguments
UPDATE_EPFL4SW197 = [name_EPFL4SW197,ip_EPFL4SW197,cpu_EPFL4SW197,portStatus_EPFL4SW197,portInbound_EPFL4SW197,portOutbound_EPFL4SW197,log_EPFL4SW197,status_EPFL4SW197]# 7 arguments
EPFL4SW197.update_SW("EPFL4SW197",UPDATE_EPFL4SW197)# 2 arguments
EPFL4SW197.update_Location("EPFL4SW197",20.046534, 99.890843)# 3 arguments
#EPFL4SW197.delete_SW("EPFL4SW197")# 1 argument