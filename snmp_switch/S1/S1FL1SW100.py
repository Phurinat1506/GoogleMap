from pysnmp.hlapi import *
import datetime
import sys 
import os
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/"))
from OOP_Switch import Switches

info_SW = "172.30.203.14"
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

snmp_get(UdpTransportTarget(('172.30.203.14', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_S1FL1SW100 = check_status_sw(info_SW[1])

while(status_S1FL1SW100 != 0):
    snmp_get(UdpTransportTarget(('172.30.203.14', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_S1FL1SW100=info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.203.14', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.4.20.1.1.172.30.203.14')))
    ip_S1FL1SW100=info_SW[1]    
    
    snmp_get(UdpTransportTarget(('172.30.203.14', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.1.57.0')))
    cpu_S1FL1SW100=info_SW[1]    

    snmp_get(UdpTransportTarget(('172.30.203.14', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portInbound_port_S1FL1SW100 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.203.14', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.6.10')))
    portInbound_packet_S1FL1SW100 = info_SW[1]
    portInbound_S1FL1SW100 = portInbound_port_S1FL1SW100+":"+portInbound_packet_S1FL1SW100

    snmp_get(UdpTransportTarget(('172.30.203.14', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portOutbound_port_S1FL1SW100 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.203.14', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.8.10')))
    portOutbound_packet_S1FL1SW100 = info_SW[1]
    portOutbound_S1FL1SW100 = portOutbound_port_S1FL1SW100+":"+portOutbound_packet_S1FL1SW100

    snmp_get(UdpTransportTarget(('172.30.203.14', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.3.0')))
    log_S1FL1SW100 = uptime(info_SW[1])  
 
    snmp_getnext(UdpTransportTarget(('172.30.203.14', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.9.23.1.2.1.1.6')))
    portStatus_S1FL1SW100 = MY_CONSTANT(implement(temp))
    temp.clear()

    break


while(status_S1FL1SW100 == 0):
    name_S1FL1SW100 = info_SW
    ip_S1FL1SW100 = info_SW
    cpu_S1FL1SW100 = info_SW
    portInbound_S1FL1SW100 = info_SW
    portOutbound_S1FL1SW100 = info_SW
    log_S1FL1SW100 = info_SW
    portStatus_S1FL1SW100 = info_SW

    break

S1FL1SW100 = Switches(name_S1FL1SW100,ip_S1FL1SW100,cpu_S1FL1SW100,portStatus_S1FL1SW100,portInbound_S1FL1SW100,portOutbound_S1FL1SW100,log_S1FL1SW100)
S1FL1SW100.insert_SW("S1FL1SW100",20.046023, 99.894179)# 3 arguments
UPDATE_S1FL1SW100 = [name_S1FL1SW100,ip_S1FL1SW100,cpu_S1FL1SW100,portStatus_S1FL1SW100,portInbound_S1FL1SW100,portOutbound_S1FL1SW100,log_S1FL1SW100,status_S1FL1SW100]# 7 arguments
S1FL1SW100.update_SW("S1FL1SW100",UPDATE_S1FL1SW100)# 2 arguments
S1FL1SW100.update_Location("S1FL1SW100",20.046023, 99.894179)# 3 arguments
#S1FL1SW100.delete_SW("S1FL1SW100")# 1 argument