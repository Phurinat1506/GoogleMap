from pysnmp.hlapi import *
import datetime
import sys 
import os
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/"))
from OOP_Switch import Switches

info_SW = "172.30.201.101"
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

snmp_get(UdpTransportTarget(('172.30.201.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.1')))
status_CHINAFL1SW046 = check_status_sw(info_SW[1])

while(status_CHINAFL1SW046 != 0):
    snmp_get(UdpTransportTarget(('172.30.201.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0'))) 
    name_CHINAFL1SW046=info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.201.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.4.20.1.1.172.30.201.101')))
    ip_CHINAFL1SW046=info_SW[1]    
    
    snmp_get(UdpTransportTarget(('172.30.201.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.1.57.0')))
    cpu_CHINAFL1SW046=info_SW[1]    

    snmp_get(UdpTransportTarget(('172.30.201.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portInbound_port_CHINAFL1SW046 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.201.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.6.10')))
    portInbound_packet_CHINAFL1SW046 = info_SW[1]
    portInbound_CHINAFL1SW046 = portInbound_port_CHINAFL1SW046+":"+portInbound_packet_CHINAFL1SW046

    snmp_get(UdpTransportTarget(('172.30.201.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2.10')))
    portOutbound_port_CHINAFL1SW046 = info_SW[1]

    snmp_get(UdpTransportTarget(('172.30.201.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.2.2.1.1.8.10')))
    portOutbound_packet_CHINAFL1SW046 = info_SW[1]
    portOutbound_CHINAFL1SW046 = portOutbound_port_CHINAFL1SW046+":"+portOutbound_packet_CHINAFL1SW046

    snmp_get(UdpTransportTarget(('172.30.201.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.3.0')))
    log_CHINAFL1SW046 = uptime(info_SW[1])  
 
    snmp_getnext(UdpTransportTarget(('172.30.201.101', 161)),ObjectType(ObjectIdentity('.1.3.6.1.4.1.9.9.23.1.2.1.1.6')))
    portStatus_CHINAFL1SW046 = MY_CONSTANT(implement(temp))
    temp.clear()

    break


while(status_CHINAFL1SW046 == 0):
    name_CHINAFL1SW046 = info_SW
    ip_CHINAFL1SW046 = info_SW
    cpu_CHINAFL1SW046 = info_SW
    portInbound_CHINAFL1SW046 = info_SW
    portOutbound_CHINAFL1SW046 = info_SW
    log_CHINAFL1SW046 = info_SW
    portStatus_CHINAFL1SW046 = info_SW

    break

CHINAFL1SW046 = Switches(name_CHINAFL1SW046,ip_CHINAFL1SW046,cpu_CHINAFL1SW046,portStatus_CHINAFL1SW046,portInbound_CHINAFL1SW046,portOutbound_CHINAFL1SW046,log_CHINAFL1SW046)
CHINAFL1SW046.insert_SW("CHINAFL1SW046",20.049323, 99.891887)# 3 arguments
UPDATE_CHINAFL1SW046 = [name_CHINAFL1SW046,ip_CHINAFL1SW046,cpu_CHINAFL1SW046,portStatus_CHINAFL1SW046,portInbound_CHINAFL1SW046,portOutbound_CHINAFL1SW046,log_CHINAFL1SW046,status_CHINAFL1SW046]# 7 arguments
CHINAFL1SW046.update_SW("CHINAFL1SW046",UPDATE_CHINAFL1SW046)# 2 arguments
CHINAFL1SW046.update_Location("CHINAFL1SW046",20.049323, 99.891887)# 3 arguments
#CHINAFL1SW046.delete_SW("CHINAFL1SW046")# 1 argument
