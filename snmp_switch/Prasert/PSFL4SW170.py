from pysnmp.hlapi import *
import datetime
import sys 
import os
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/"))
from OOP_Switch import Switches

info_SW = "172.30.201.24"
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

snmp_get(UdpTransportTarget(('172.30.201.24', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_PSFL4SW170 = check_status_sw(info_SW[1])

while(status_PSFL4SW170 != 0):
    snmp_get(UdpTransportTarget(('172.30.201.24', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_PSFL4SW170=info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.201.24', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.4.20.1.1.172.30.201.24')))
    ip_PSFL4SW170=info_SW[1]    
    
    snmp_get(UdpTransportTarget(('172.30.201.24', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.1.57.0')))
    cpu_PSFL4SW170=info_SW[1]    

    snmp_get(UdpTransportTarget(('172.30.201.24', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portInbound_port_PSFL4SW170 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.201.24', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.6.10')))
    portInbound_packet_PSFL4SW170 = info_SW[1]
    portInbound_PSFL4SW170 = portInbound_port_PSFL4SW170+":"+portInbound_packet_PSFL4SW170

    snmp_get(UdpTransportTarget(('172.30.201.24', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portOutbound_port_PSFL4SW170 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.201.24', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.8.10')))
    portOutbound_packet_PSFL4SW170 = info_SW[1]
    portOutbound_PSFL4SW170 = portOutbound_port_PSFL4SW170+":"+portOutbound_packet_PSFL4SW170

    snmp_get(UdpTransportTarget(('172.30.201.24', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.3.0')))
    log_PSFL4SW170 = uptime(info_SW[1])  
 
    snmp_getnext(UdpTransportTarget(('172.30.201.24', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.9.23.1.2.1.1.6')))
    portStatus_PSFL4SW170 = MY_CONSTANT(implement(temp))
    temp.clear()

    break


while(status_PSFL4SW170 == 0):
    name_PSFL4SW170 = info_SW
    ip_PSFL4SW170 = info_SW
    cpu_PSFL4SW170 = info_SW
    portInbound_PSFL4SW170 = info_SW
    portOutbound_PSFL4SW170 = info_SW
    log_PSFL4SW170 = info_SW
    portStatus_PSFL4SW170 = info_SW

    break

PSFL4SW170 = Switches(name_PSFL4SW170,ip_PSFL4SW170,cpu_PSFL4SW170,portStatus_PSFL4SW170,portInbound_PSFL4SW170,portOutbound_PSFL4SW170,log_PSFL4SW170)
PSFL4SW170.insert_SW("PSFL4SW170",20.051167, 99.892060)# 3 arguments
UPDATE_PSFL4SW170 = [name_PSFL4SW170,ip_PSFL4SW170,cpu_PSFL4SW170,portStatus_PSFL4SW170,portInbound_PSFL4SW170,portOutbound_PSFL4SW170,log_PSFL4SW170,status_PSFL4SW170]# 7 arguments
PSFL4SW170.update_SW("PSFL4SW170",UPDATE_PSFL4SW170)# 2 arguments
PSFL4SW170.update_Location("PSFL4SW170",20.051167, 99.892060)# 3 arguments
#PSFL4SW170.delete_SW("PSFL4SW170")# 1 argument
