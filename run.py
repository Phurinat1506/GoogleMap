import sys 
import os
from OOP_Switch import mycol

sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/S1"))
from S1FL1SW100 import *
from S1FL1SW101 import *
from S1FL1SW208 import *
from S1FL1SW209 import *
from S1FL2SW002 import *
from S1FL2SW102 import *
from S1FL2SW103 import *
from S1FL2SW104 import *
from S1FL2SW105 import *
from S1FL2SW210 import *
from S1FL2SW211 import *
from S1FL2SW212 import *
from S1FL2SW213 import *
from S1FL3SW106 import *
from S1FL3SW107 import *
from S1FL3SW108 import *
from S1FL3SW109 import *
from S1FL3SW110 import *
from S1FL3SW111 import *
from S1FL3SW112 import *
from S1FL3SW214 import *
from S1FL3SW215 import *
from S1FL3SW216 import *
from S1FL4SW113 import *
from S1FL4SW217 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/S2"))
from S2FL2SW022 import *
from S2FL2SW114 import *
from S2FL2SW218 import *
from S2FL4SW115 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/S3"))
from S3FL3SW023 import *
from S3FL3SW116 import *
from S3FL3SW117 import *
from S3FL3SW219 import *
from S3FL3SW220 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/S4"))
from S4FL1R117 import *
from S4FL1SW118 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/S5"))
from S5FL1SW221 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/S6"))
from S6FL1SW222 import *
from S6FL2 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/S7"))
from SWITCH1 import *
from SWITCH2 import *
from S7AFL1SW009 import *
from S7AFL1SW044 import *
from S7AFL2SW119 import *
from S7AFL2SW120 import *
from S7AFL2SW121 import *
from S7AFL2SW122 import *
from S7AFL3SW223 import *
from S7AFL4SW045 import * 
from S7BFL2SW123 import * 
from S7BFL3SW124 import * 
from S7BFL4SW125 import * 
from S7BFL5SW126 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/A1"))
from A11 import *
from A12 import *
from A12TEMP import *
from A13 import *
from A14 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/A2"))
from A21FL1SW228 import *
from A22FL1SW229 import *
from A23FL1SW230 import *
from A24FL1SW231 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/AD1"))
from AD1FL1SW010 import *
from AD1FL1SW053 import *
from AD1FL2SW054 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/AD2"))
from AD2FL1SW011 import *
from AD2FL1SW055 import *
from AD2FL1SW056 import *
from AD2FL2SW057 import *
from AD2FL2SW200 import *
from AD2FL3SW058 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/AS"))
from ASFL1SW201 import *
from ASFL1SW202 import *
from ASFL3SW001 import *
from ASFL3SW005 import *
from ASFL3SW012 import *
from ASFL3SW060 import *
from ASFL3SW061 import *
from ASFL3SW062 import *
from ASFL3SW059 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/AV"))
from AVFL3SW013 import *
from AVFL2SW063 import *
from AVFL3SW203 import *
from AVFL4SW064 import *
from AVFL5SW065 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/C1"))
from C1SOUTHFL1SW008 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/C2"))
from C2NORTHFL3SW018 import *
from C2SOUTHFL3SW042 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/C3"))
from C3FL1SW043 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/C4"))
from C4FL1SW019 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/C5"))
from C5FL3SW020 import *
from C5FL3SW095 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/Chinese Center"))
from CHINAFL1SW046 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/Confucius"))
from CONFUCIUSFL1SW224 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/D1"))
from D1FL1SW014 import *
from D1FL1SW066 import *
from D1FL3 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/D2"))
from D2FL1SW040 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/E1"))
from E1FL2SW015 import *
from E1FL2SW067 import *
from E1FL2SW068 import *
from E1FL2SW069 import *
from E1FL2SW070 import *
from E1FL2SW071 import *
from E1FL2SW072 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/E2"))
from E2FL2SW016 import *
from E2FL2SW073 import *
from E2FL2SW074 import *
from E2FL2SW075 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/E3"))
from E3AFL2SW076 import *
from E3AFL3SW077 import *
from E3AFL3SW078 import *
from E3AFL4SW079 import *
from E3AFL4SW080 import *
from E3AFL5SW081 import *
from E3AFL5SW082 import *
from E3BFL1 import *
from E3BFL1SW006 import *
from E3BFL2SW204 import *
from E3BFL3SW083 import *
from E3BFL3SW084 import *
from E3BFL4SW085 import *
from E3BFL4SW086 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/E4"))
from E4AFL1SW087 import *
from E4AFL2SW088 import *
from E4AFL3SW089 import *
from E4AFL4 import *
from E4AFL4SW007 import *
from E4AFL4SW090 import *
from E4AFL5SW091 import *
from E4AFL6SW092 import *
from E4AFL7SW093 import *
from E4AFL8SW205 import *
from E4BFL5 import *
from E4BFL5SW206 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/EPark"))
from EPFL2SW000 import *
from EPFL2SW195 import *
from EPFL3SW196 import *
from EPFL4SW197 import *
from EPFL5SW198 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/F1"))
from F1FL1SW024 import *
from F1FL1SW127 import *
from F1FL2SW128 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/F2"))
from F2FL1SW025 import *
from F2FL1SW129 import *
from F2FL2SW130 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/F3"))
from F3FL1SW026 import *
from F3FL1SW131 import *
from F3FL2SW132 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/F4"))
from F4FL1SW027 import *
from F4FL1SW133 import *
from F4FL2SW134 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/F5"))
from F5FL1SW028 import *
from F5FL1SW135 import *
from F5FL2SW136 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/F6"))
from F6FL1SW029 import *
from F6FL1SW137 import *
from F6FL2SW138 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/Fitness"))
from FITNESSFL1SW051 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/Football"))
from FOOTBALLFL1SW236 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/GYM"))
from GYMFL1 import *
from GYMFL1SW039 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/HOSPITAL"))
from HOSFL1SW038 import *
from HOSFL2 import *
from HOSFL3SW194 import *
from HOSFLB1 import *
from INPFL1SW232 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/IPark"))
from IPFL2SW199 import *
from IPFL3SW233 import *
from IPFL4SW234 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/L1"))
from L1FL1SW030 import *
from L1FL1SW139 import *
from L1FL3SW140 import *
from L1FL3SW141 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/L2"))
from L2FL1SW031 import *
from L2FL1SW142 import *
from L2FL3SW143 import *
from L2FL3SW144 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/L3"))
from L3FL1SW032 import *
from L3FL1SW145 import *
from L3FL3SW146 import *
from L3FL3SW147 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/L4"))
from L4FL1SW033 import *
from L4FL1SW148 import *
from L4FL3SW149 import *
from L4FL3SW150 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/L5"))
from L5FL1SW034 import *
from L5FL1SW151 import *
from L5FL3SW152 import *
from L5FL3SW153 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/L6"))
from L6FL1SW035 import *
from L6FL1SW154 import *
from L6FL3SW155 import *
from L6FL3SW156 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/L7"))
from L7FL1SW036 import *
from L7FL1SW157 import *
from L7FL3SW158 import *
from L7FL3SW159 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/L8"))
from L8FL3SW227 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/LPark"))
from LPFL2SW235 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/Makampom"))
from MKPFL1SW050 import *
from MKPFL2SW191 import *
from MKPFL3SW192 import *
from MKPFL4SW193 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/Pool"))
from POOLFL1SW237 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/Wanawes"))
from WWFL1SW226 import *
from WWFL2SW047 import *
from WWFL2SW160 import *
from WWFL3SW161 import *
from WWFL4SW162 import *
from WWFL5SW163 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/Wanasom"))
from WNSA import *
from WNSB import *
from WNSC import *
from WNSD import *
from WNSE import *
from WNSF import *
from WNSFL1SW052 import *
from WNSSPA import *
from WNSWANASAWAN import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/Pao"))
from PAOFL1SW004 import *
from PAOFL1SW175 import *
from PAOFL2SW176 import *
from PAOFL3SW177 import *
from PAOFL4SW178 import *
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/M3"))
from M3FL2SW021 import *
from M3FL3SW096 import *
from M3FL4SW097 import *
from M3FL4SW098 import *
from M3FL5SW099 import *
from M3FL6SW207 import *

sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/Botanic"))
from BOTANICFL1SW238 import *

sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/Boonsong"))
from BSFL1SW171 import *
from BSFL2SW172 import *
from BSFL3SW173 import *
from BSFL4SW174 import *

sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/Prasert"))
from PSFL1SW037 import *
from PSFL2SW168 import *
from PSFL3SW169 import *
from PSFL4SW170 import *

sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/snmp_switch/L8"))
from L8FL3SW227 import *
from L8FL4SW164 import *
from L8FL5SW165 import *
from L8FL6SW166 import *
from L8FL7SW167 import *

for x in mycol.find():#find all document
    print(x)

