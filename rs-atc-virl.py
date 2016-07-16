import os
import codecs

locations = {
    'R1': '53,35',
    'R2': '53,94',
    'R3': '53,150',
    'R4': '53,202',  
    'R5': '53,258',
    'R6': '53,312',
    'R7': '53,364',
    'R8': '53,424',
    'R9': '53,486',
    'R10': '53,552',
}

header = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<topology xmlns="http://www.cisco.com/VIRL" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="0.9" xsi:schemaLocation="http://www.cisco.com/VIRL https://raw.github.com/CiscoVIRL/schema/v0.9/virl.xsd">
'''

footer = '''
    <connection dst="/virl:topology/virl:node[11]/virl:interface[1]" src="/virl:topology/virl:node[9]/virl:interface[1]"/>
    <connection dst="/virl:topology/virl:node[11]/virl:interface[2]" src="/virl:topology/virl:node[10]/virl:interface[1]"/>
    <connection dst="/virl:topology/virl:node[11]/virl:interface[3]" src="/virl:topology/virl:node[1]/virl:interface[1]"/>
    <connection dst="/virl:topology/virl:node[11]/virl:interface[4]" src="/virl:topology/virl:node[2]/virl:interface[1]"/>
    <connection dst="/virl:topology/virl:node[11]/virl:interface[5]" src="/virl:topology/virl:node[3]/virl:interface[1]"/>
    <connection dst="/virl:topology/virl:node[11]/virl:interface[6]" src="/virl:topology/virl:node[4]/virl:interface[1]"/>
    <connection dst="/virl:topology/virl:node[11]/virl:interface[7]" src="/virl:topology/virl:node[5]/virl:interface[1]"/>
    <connection dst="/virl:topology/virl:node[11]/virl:interface[8]" src="/virl:topology/virl:node[6]/virl:interface[1]"/>
    <connection dst="/virl:topology/virl:node[11]/virl:interface[9]" src="/virl:topology/virl:node[7]/virl:interface[1]"/>
    <connection dst="/virl:topology/virl:node[11]/virl:interface[10]" src="/virl:topology/virl:node[8]/virl:interface[1]"/>
</topology>'''

def build_router_config(router_name, router_location, router_config):
    router_config = '''
    <node name="{0}" type="SIMPLE" subtype="IOSv" location="{1}" vmImage="IOSv [5340a778-440a-45b0-b8de-2271612732ba]" vmFlavor="IOSv [3d253112-e8b6-4db9-b133-67621bf58eb2]">
            <extensions>
                <entry key="Auto-generate config" type="Boolean">false</entry>
                <entry key="config" type="String">{2}</entry>
            </extensions>
            <interface id="0" name="GigabitEthernet0/1"/>
            <interface id="1" name="GigabitEthernet0/2"/>
            <interface id="2" name="GigabitEthernet0/3"/>
    </node>'''.format(router_name, router_location, router_config)
    return router_config

switch_config = '''
<node name="SW5" type="SIMPLE" subtype="IOSvL2" location="450,295" vmImage="IOSvL2 [a69a29a3-8446-4f66-beea-cf1cfe1772fe]" vmFlavor="IOSvL2 [4b19f77e-ad8e-4b09-b08d-4e11e792fc19]">
        <extensions>
            <entry key="Auto-generate config" type="Boolean">false</entry>
            <entry key="config" type="String">service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname SW5
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
!
!
!
!
!         
!
!
!
ip cef
no ipv6 cef
!
!
spanning-tree mode rapid-pvst
spanning-tree extend system-id
!
vlan internal allocation policy ascending
!
! 
!
!
!
!
vlan 5
!
vlan 7
!
vlan 8
!
vlan 9
!
vlan 10
!
vlan 13
!
vlan 23
!
vlan 37
!
vlan 45
!
vlan 58
!
vlan 67
!
vlan 79
!
vlan 100
!
vlan 108
!
vlan 146
!
!
!
!
!
!
!         
!
interface GigabitEthernet0/0
 media-type rj45
 negotiation auto
!
interface GigabitEthernet0/1
 desc to R1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,13,100,146
 media-type rj45
 negotiation auto
 spanning-tree portfast
!
interface GigabitEthernet0/2
 desc to R2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,23,100
 media-type rj45
 negotiation auto
 spanning-tree portfast
!
interface GigabitEthernet0/3
 desc to R3
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,13,23,37,100
 media-type rj45
 negotiation auto
 spanning-tree portfast
!
interface GigabitEthernet1/0
 desc to R4
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,45,100,146
 media-type rj45
 negotiation auto
 spanning-tree portfast
!
interface GigabitEthernet1/1
 desc to R5
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,5,45,58,100
 media-type rj45
 negotiation auto
 spanning-tree portfast
!
interface GigabitEthernet1/2
 desc to R6
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,67,146
 media-type rj45
 negotiation auto
 spanning-tree portfast
!
interface GigabitEthernet1/3
 desc to R7
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,7,37,67,79
 media-type rj45
 negotiation auto
 spanning-tree portfast
!
interface GigabitEthernet2/0
 desc to R8
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,8,58,108
 media-type rj45
 negotiation auto
 spanning-tree portfast
!
interface GigabitEthernet2/1
 desc to R9
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,9,79
 media-type rj45
 negotiation auto
 spanning-tree portfast
!
interface GigabitEthernet2/2
 desc to R10
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,10,108
 media-type rj45
 negotiation auto
 spanning-tree portfast
!
interface GigabitEthernet2/3
 media-type rj45
 negotiation auto
 sh
!
ip forward-protocol nd
!
no ip http server
no ip http secure-server
!
!
!
!
!
!
control-plane
!
banner exec ^C
**************************************************************************
* IOSv - Cisco Systems Confidential                                      *
*                                                                        *
* This software is provided as is without warranty for internal          *
* development and testing purposes only under the terms of the Cisco     *
* Early Field Trial agreement.  Under no circumstances may this software *
* be used for production purposes or deployed in a production            *
* environment.                                                           *
*                                                                        *
* By using the software, you agree to abide by the terms and conditions  *
* of the Cisco Early Field Trial Agreement as well as the terms and      *
* conditions of the Cisco End User License Agreement at                  *
* http://www.cisco.com/go/eula                                           *
*                                                                        *
* Unauthorized use or distribution of this software is expressly         *
* Prohibited.                                                            *
**************************************************************************^C
banner incoming ^C
**************************************************************************
* IOSv - Cisco Systems Confidential                                      *
*                                                                        *
* This software is provided as is without warranty for internal          *
* development and testing purposes only under the terms of the Cisco     *
* Early Field Trial agreement.  Under no circumstances may this software *
* be used for production purposes or deployed in a production            *
* environment.                                                           *
*                                                                        *
* By using the software, you agree to abide by the terms and conditions  *
* of the Cisco Early Field Trial Agreement as well as the terms and      *
* conditions of the Cisco End User License Agreement at                  *
* http://www.cisco.com/go/eula                                           *
*                                                                        *
* Unauthorized use or distribution of this software is expressly         *
* Prohibited.                                                            *
**************************************************************************^C
banner login ^C
**************************************************************************
* IOSv - Cisco Systems Confidential                                      *
*                                                                        *
* This software is provided as is without warranty for internal          *
* development and testing purposes only under the terms of the Cisco     *
* Early Field Trial agreement.  Under no circumstances may this software *
* be used for production purposes or deployed in a production            *
* environment.                                                           *
*                                                                        *
* By using the software, you agree to abide by the terms and conditions  *
* of the Cisco Early Field Trial Agreement as well as the terms and      *
* conditions of the Cisco End User License Agreement at                  *
* http://www.cisco.com/go/eula                                           *
*                                                                        *
* Unauthorized use or distribution of this software is expressly         *
* Prohibited.                                                            *
**************************************************************************^C
!
line con 0
 exec-timeout 0 0
 logging synchronous
 privilege level 15
 no login
line aux 0
line vty 0 4
!
!</entry>
        </extensions>
        <interface id="0" name="GigabitEthernet0/1"/>
        <interface id="1" name="GigabitEthernet0/2"/>
        <interface id="2" name="GigabitEthernet0/3"/>
        <interface id="3" name="GigabitEthernet1/0"/>
        <interface id="4" name="GigabitEthernet1/1"/>
        <interface id="5" name="GigabitEthernet1/2"/>
        <interface id="6" name="GigabitEthernet1/3"/>
        <interface id="7" name="GigabitEthernet2/0"/>
        <interface id="8" name="GigabitEthernet2/1"/>
        <interface id="9" name="GigabitEthernet2/2"/>
        <interface id="10" name="GigabitEthernet2/3"/>
</node>'''

root_dir = '/Users/brad/Dropbox/learning/cisco/Workbooks v5/Workbooks v5/VIRL/INE/INE.VIRL.initial.configs/advanced.technology.labs'

for sub_dir, dirs, files in os.walk(root_dir):
    virl_filename = '{0}.virl'.format(sub_dir.split('/')[-1].replace('.', '-'))
    print(sub_dir.split('/')[-1])
    print(virl_filename)
    with open(virl_filename, 'w') as f:
        f.write(header)
        for conf_file in files:
            print(conf_file)
            if conf_file.startswith('R') and conf_file.endswith('.txt'):
                device_name = conf_file.split('.')[0]
                #print(device_name, locations[device_name])
                with open('{0}/{1}'.format(sub_dir, conf_file), 'rb') as fl:
                    encoded_text = fl.read()
                    try:
                        f.write(build_router_config(device_name, locations[device_name], encoded_text.decode('UTF-8')))
                    except UnicodeDecodeError:
                        bom = codecs.BOM_UTF16_LE             
                        assert encoded_text.startswith(bom)   
                        encoded_text = encoded_text[len(bom):]
                        decoded_text = encoded_text.decode('utf-16le') 
                        f.write(build_router_config(device_name, locations[device_name], decoded_text))
        f.write(switch_config)
        f.write(footer)
