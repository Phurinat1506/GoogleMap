from pysnmp.hlapi import *
import datetime
import sys 
import os
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/"))
from OOP_Switch import Switches

info_SW = "172.30.202.101"
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

snmp_get(UdpTransportTarget(('172.30.202.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_WWFL2SW047 = check_status_sw(info_SW[1])

while(status_WWFL2SW047 != 0):
    snmp_get(UdpTransportTarget(('172.30.202.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_WWFL2SW047=info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.202.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.4.20.1.1.172.30.202.101')))
    ip_WWFL2SW047=info_SW[1]    
    
    snmp_get(UdpTransportTarget(('172.30.202.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.1.57.0')))
    cpu_WWFL2SW047=info_SW[1]    

    snmp_get(UdpTransportTarget(('172.30.202.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portInbound_port_WWFL2SW047 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.202.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.6.10')))
    portInbound_packet_WWFL2SW047 = info_SW[1]
    portInbound_WWFL2SW047 = portInbound_port_WWFL2SW047+":"+portInbound_packet_WWFL2SW047

    snmp_get(UdpTransportTarget(('172.30.202.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portOutbound_port_WWFL2SW047 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.202.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.8.10')))
    portOutbound_packet_WWFL2SW047 = info_SW[1]
    portOutbound_WWFL2SW047 = portOutbound_port_WWFL2SW047+":"+portOutbound_packet_WWFL2SW047

    snmp_get(UdpTransportTarget(('172.30.202.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.3.0')))
    log_WWFL2SW047 = uptime(info_SW[1])  
 
    snmp_getnext(UdpTransportTarget(('172.30.202.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.9.23.1.2.1.1.6')))
    portStatus_WWFL2SW047 = MY_CONSTANT(implement(temp))
    temp.clear()

    break


while(status_WWFL2SW047 == 0):
    name_WWFL2SW047 = info_SW
    ip_WWFL2SW047 = info_SW
    cpu_WWFL2SW047 = info_SW
    portInbound_WWFL2SW047 = info_SW
    portOutbound_WWFL2SW047 = info_SW
    log_WWFL2SW047 = info_SW
    portStatus_WWFL2SW047 = info_SW

    break

WWFL2SW047 = Switches(name_WWFL2SW047,ip_WWFL2SW047,cpu_WWFL2SW047,portStatus_WWFL2SW047,portInbound_WWFL2SW047,portOutbound_WWFL2SW047,log_WWFL2SW047)
WWFL2SW047.insert_SW("WWFL2SW047",20.055803, 99.898298)# 3 arguments
UPDATE_WWFL2SW047 = [name_WWFL2SW047,ip_WWFL2SW047,cpu_WWFL2SW047,portStatus_WWFL2SW047,portInbound_WWFL2SW047,portOutbound_WWFL2SW047,log_WWFL2SW047,status_WWFL2SW047]# 7 arguments
WWFL2SW047.update_SW("WWFL2SW047",UPDATE_WWFL2SW047)# 2 arguments
WWFL2SW047.update_Location("WWFL2SW047",20.055803, 99.898298)# 3 arguments
#WWFL2SW047.delete_SW("WWFL2SW047")# 1 argument