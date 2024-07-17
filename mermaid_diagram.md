---
title: Airbus Aerostructures PoV 2024
---
flowchart LR
281474976770201(<b>NCP_Gateway_A</b><br>Target: 185.187.245.25:443)
4844(["Munich, Germany"]):::teAgent --> 281474976770201
4904(["Dusseldorf, Germany"]):::teAgent --> 281474976770201
42311(["Hamburg, Germany"]):::teAgent --> 281474976770201
315431(["Frankfurt, Germany"]):::teAgent --> 281474976770201
281474976770202(<b>NCP_Gateway_B</b><br>Target: 88.217.236.204:443)
4844(["Munich, Germany"]):::teAgent --> 281474976770202
4904(["Dusseldorf, Germany"]):::teAgent --> 281474976770202
42311(["Hamburg, Germany"]):::teAgent --> 281474976770202
315431(["Frankfurt, Germany"]):::teAgent --> 281474976770202
281474976771482(<b>Netskope - PoP - IAD2</b><br>Target: 163.116.146.38)
4844(["Munich, Germany"]):::teAgent --> 281474976771482
315431(["Frankfurt, Germany"]):::teAgent --> 281474976771482
4113(["Frankfurt, Germany (Cogent)"]):::teAgent --> 281474976771482
5616(["Bucharest, Romania"]):::teAgent --> 281474976771482
387266(["Marseille, France (Orange)"]):::teAgent --> 281474976771482
42311(["Hamburg, Germany"]):::teAgent --> 281474976771482
721036(["Paris, France (Orange)"]):::teAgent --> 281474976771482
1193906(["Munich, Germany (Vodafone - AWS Wavelength)"]):::teAgent --> 281474976771482
1325202(["Frankfurt, Germany (Vodafone)"]):::teAgent --> 281474976771482
281474976771472(<b>Netskope - PoP - MRS1</b><br>Target: 163.116.174.36)
4844(["Munich, Germany"]):::teAgent --> 281474976771472
4113(["Frankfurt, Germany (Cogent)"]):::teAgent --> 281474976771472
315431(["Frankfurt, Germany"]):::teAgent --> 281474976771472
5616(["Bucharest, Romania"]):::teAgent --> 281474976771472
387266(["Marseille, France (Orange)"]):::teAgent --> 281474976771472
42311(["Hamburg, Germany"]):::teAgent --> 281474976771472
721036(["Paris, France (Orange)"]):::teAgent --> 281474976771472
1193906(["Munich, Germany (Vodafone - AWS Wavelength)"]):::teAgent --> 281474976771472
1325202(["Frankfurt, Germany (Vodafone)"]):::teAgent --> 281474976771472
281474976771479(<b>Netskope - PoP - ORD1</b><br>Target: 163.116.133.38)
4844(["Munich, Germany"]):::teAgent --> 281474976771479
315431(["Frankfurt, Germany"]):::teAgent --> 281474976771479
4113(["Frankfurt, Germany (Cogent)"]):::teAgent --> 281474976771479
5616(["Bucharest, Romania"]):::teAgent --> 281474976771479
387266(["Marseille, France (Orange)"]):::teAgent --> 281474976771479
42311(["Hamburg, Germany"]):::teAgent --> 281474976771479
721036(["Paris, France (Orange)"]):::teAgent --> 281474976771479
1193906(["Munich, Germany (Vodafone - AWS Wavelength)"]):::teAgent --> 281474976771479
1325202(["Frankfurt, Germany (Vodafone)"]):::teAgent --> 281474976771479
281474976768994(<b>ASA_ServiceNow - airbus.service-now.com - DNS</b><br>Target: airbus.service-now.com)
4844(["Munich, Germany"]):::teAgent --> 281474976768994
315431(["Frankfurt, Germany"]):::teAgent --> 281474976768994
5616(["Bucharest, Romania"]):::teAgent --> 281474976768994
1193896(["Berlin, Germany (Vodafone - AWS Wavelength)"]):::teAgent --> 281474976768994
1325202(["Frankfurt, Germany (Vodafone)"]):::teAgent --> 281474976768994
281474976724308(["AUGTEA001"]):::teAgent --> 281474976768994
281474976768994 --> 281474976716909([eur6.akam.net.])
281474976768994 --> 281474976716910([usw1.akam.net.])
281474976768994 --> 281474976716912([usc4.akam.net.])
281474976768994 --> 281474976716916([aus1.akam.net.])
281474976768994 --> 281474976716919([use1.akam.net.])
281474976768994 --> 281474976724540([edns140.ultradns.net.])
281474976768994 --> 281474976724541([edns140.ultradns.org.])
281474976768994 --> 281474976724542([ns1-234.akam.net.])
281474976768994 --> 281474976724543([use3.akam.net.])
281474976768994 --> 281474976724544([edns140.ultradns.com.])
281474976768994 --> 281474976724545([edns140.ultradns.biz.])
281474976768994 --> 281474976724546([ns1-98.akam.net.])
281474976764520(<b>GMail Mail DNS</b><br>Target: mail.google.com)
84213(["Bangalore, India (Reliance)"]):::teAgent --> 281474976764520
315431(["Frankfurt, Germany"]):::teAgent --> 281474976764520
387266(["Marseille, France (Orange)"]):::teAgent --> 281474976764520
42311(["Hamburg, Germany"]):::teAgent --> 281474976764520
656576(["Bangalore, India (Bharti Airtel)"]):::teAgent --> 281474976764520
721036(["Paris, France (Orange)"]):::teAgent --> 281474976764520
281474976764520 --> 281474976710661([ns3.google.com.])
281474976764520 --> 281474976710662([ns4.google.com.])
281474976764520 --> 281474976710663([ns2.google.com.])
281474976764520 --> 281474976710664([ns1.google.com.])
281474976764518(<b>Goolgle Meet - DNS</b><br>Target: meet.google.com)
84213(["Bangalore, India (Reliance)"]):::teAgent --> 281474976764518
315431(["Frankfurt, Germany"]):::teAgent --> 281474976764518
387266(["Marseille, France (Orange)"]):::teAgent --> 281474976764518
42311(["Hamburg, Germany"]):::teAgent --> 281474976764518
656576(["Bangalore, India (Bharti Airtel)"]):::teAgent --> 281474976764518
721036(["Paris, France (Orange)"]):::teAgent --> 281474976764518
281474976764518 --> 281474976710661([ns3.google.com.])
281474976764518 --> 281474976710662([ns4.google.com.])
281474976764518 --> 281474976710663([ns2.google.com.])
281474976764518 --> 281474976710664([ns1.google.com.])
281474976742591(<b>Airbus Aerostructures Website</b><br>Target: https://www.airbus.com/en/airbus-aerostructures)
42311(["Hamburg, Germany"]):::teAgent --> 281474976742591
84213(["Bangalore, India (Reliance)"]):::teAgent --> 281474976742591
315431(["Frankfurt, Germany"]):::teAgent --> 281474976742591
387266(["Marseille, France (Orange)"]):::teAgent --> 281474976742591
656576(["Bangalore, India (Bharti Airtel)"]):::teAgent --> 281474976742591
721036(["Paris, France (Orange)"]):::teAgent --> 281474976742591
281474976716062(["NORTEA001"]):::teAgent --> 281474976742591
281474976724308(["AUGTEA001"]):::teAgent --> 281474976742591
281474976752274(<b>Airbus Proxy</b><br>Target: http://10.45.24.157:8080)
281474976716062(["NORTEA001"]):::teAgent --> 281474976752274
281474976724308(["AUGTEA001"]):::teAgent --> 281474976752274
281474976769548(<b>ASA_DEX_internal</b><br>Target: https://10.45.12.12)
281474976716062(["NORTEA001"]):::teAgent --> 281474976769548
281474976724308(["AUGTEA001"]):::teAgent --> 281474976769548
281474976742594(<b>https://supplier.premium-aerotec.com</b><br>Target: https://supplier.premium-aerotec.com)
42311(["Hamburg, Germany"]):::teAgent --> 281474976742594
84213(["Bangalore, India (Reliance)"]):::teAgent --> 281474976742594
315431(["Frankfurt, Germany"]):::teAgent --> 281474976742594
387266(["Marseille, France (Orange)"]):::teAgent --> 281474976742594
656576(["Bangalore, India (Bharti Airtel)"]):::teAgent --> 281474976742594
721036(["Paris, France (Orange)"]):::teAgent --> 281474976742594
281474976716062(["NORTEA001"]):::teAgent --> 281474976742594
281474976724308(["AUGTEA001"]):::teAgent --> 281474976742594
281474976742592(<b>Premium Aerotec</b><br>Target: https://www.premium-aerotec.com)
42311(["Hamburg, Germany"]):::teAgent --> 281474976742592
84213(["Bangalore, India (Reliance)"]):::teAgent --> 281474976742592
315431(["Frankfurt, Germany"]):::teAgent --> 281474976742592
387266(["Marseille, France (Orange)"]):::teAgent --> 281474976742592
656576(["Bangalore, India (Bharti Airtel)"]):::teAgent --> 281474976742592
721036(["Paris, France (Orange)"]):::teAgent --> 281474976742592
281474976716062(["NORTEA001"]):::teAgent --> 281474976742592
281474976724308(["AUGTEA001"]):::teAgent --> 281474976742592
281474976742593(<b>Premium Aerotec - Dataexchange</b><br>Target: https://dataexchange.premium-aerotec.com)
4844(["Munich, Germany"]):::teAgent --> 281474976742593
315431(["Frankfurt, Germany"]):::teAgent --> 281474976742593
5616(["Bucharest, Romania"]):::teAgent --> 281474976742593
387266(["Marseille, France (Orange)"]):::teAgent --> 281474976742593
42311(["Hamburg, Germany"]):::teAgent --> 281474976742593
721036(["Paris, France (Orange)"]):::teAgent --> 281474976742593
1325202(["Frankfurt, Germany (Vodafone)"]):::teAgent --> 281474976742593
281474976716062(["NORTEA001"]):::teAgent --> 281474976742593
281474976724308(["AUGTEA001"]):::teAgent --> 281474976742593
281474976768993(<b>ASA_ServiceNow - airbus.service-now.com - Web</b><br>Target: https://airbus.service-now.com)
4844(["Munich, Germany"]):::teAgent --> 281474976768993
315431(["Frankfurt, Germany"]):::teAgent --> 281474976768993
5616(["Bucharest, Romania"]):::teAgent --> 281474976768993
1193896(["Berlin, Germany (Vodafone - AWS Wavelength)"]):::teAgent --> 281474976768993
1325202(["Frankfurt, Germany (Vodafone)"]):::teAgent --> 281474976768993
281474976724308(["AUGTEA001"]):::teAgent --> 281474976768993
281474976764519(<b>GMail Mail</b><br>Target: https://mail.google.com)
84213(["Bangalore, India (Reliance)"]):::teAgent --> 281474976764519
315431(["Frankfurt, Germany"]):::teAgent --> 281474976764519
387266(["Marseille, France (Orange)"]):::teAgent --> 281474976764519
42311(["Hamburg, Germany"]):::teAgent --> 281474976764519
656576(["Bangalore, India (Bharti Airtel)"]):::teAgent --> 281474976764519
721036(["Paris, France (Orange)"]):::teAgent --> 281474976764519
281474976716062(["NORTEA001"]):::teAgent --> 281474976764519
281474976724219(["VARTEA001"]):::teAgent --> 281474976764519
281474976724308(["AUGTEA001"]):::teAgent --> 281474976764519
281474976764517(<b>Goolgle Meet - Web</b><br>Target: https://meet.google.com)
4844(["Munich, Germany"]):::teAgent --> 281474976764517
315431(["Frankfurt, Germany"]):::teAgent --> 281474976764517
5616(["Bucharest, Romania"]):::teAgent --> 281474976764517
387266(["Marseille, France (Orange)"]):::teAgent --> 281474976764517
42311(["Hamburg, Germany"]):::teAgent --> 281474976764517
721036(["Paris, France (Orange)"]):::teAgent --> 281474976764517
1325202(["Frankfurt, Germany (Vodafone)"]):::teAgent --> 281474976764517
281474976716062(["NORTEA001"]):::teAgent --> 281474976764517
281474976724219(["VARTEA001"]):::teAgent --> 281474976764517
281474976724308(["AUGTEA001"]):::teAgent --> 281474976764517
281474976769486(<b>PLM Prod</b><br>Target: https://plmprod.de.pa.corp/)
281474976716062(["NORTEA001"]):::teAgent --> 281474976769486
281474976724308(["AUGTEA001"]):::teAgent --> 281474976769486
281474976764525(<b>GMail Transaction</b><br>Target: server)
281474976716062(["NORTEA001"]):::teAgent --> 281474976764525
281474976724219(["VARTEA001"]):::teAgent --> 281474976764525
281474976724308(["AUGTEA001"]):::teAgent --> 281474976764525
cloud([Cloud Units<br>6316]) -..- total((Total Units<br>9000)) -..- ent([Enterprise Units<br>540])
classDef teAgent fill:#f96
##### START - Label: Use-Case_Home-Office - START #####
---
title: Use-Case_Home-Office
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770673("VPN GW C1 - tcp/113"<br>Type: agent-to-server, Interval: 120s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
281474976770673 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976770673_server([194.0.93.94:113])
281474976770677("VPN GW C2 - tcp/113"<br>Type: agent-to-server, Interval: 120s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
281474976770677 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976770677_server([194.0.93.95:113])
classDef teAgent fill:#f80

##### END - Label: Use-Case_Home-Office - END #####

##### START - Label: LRABB - Website - START #####
---
title: LRABB - Website
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770626("LRABB - Website - https://www.lrabb.de"<br>Type: page-load, Interval: 300s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976770626
281474976770626 --Trace: classic<br>Protocol: TCP --> 281474976770626_url([https://www.lrabb.de])
classDef teAgent fill:#f80

##### END - Label: LRABB - Website - END #####

##### START - Label: Webex Video Tests - START #####
---
title: Webex Video Tests
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770663("Webex - lrabb - EMEA - Video - 9000"<br>Type: agent-to-agent, Interval: 60s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
281474976770663 --Trace: classic<br>Protocol: UDP/9000<br>DSCP: 34 --> 281474976770663_agent(["Frankfurt, Germany (Webex)"])
classDef teAgent fill:#f80

##### END - Label: Webex Video Tests - END #####

##### START - Label: Use-Case_Apps-Services - START #####
---
title: Use-Case_Apps-Services
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976776744("ACS - Database"<br>Type: agent-to-server, Interval: 60s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976776744
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976776744
281474976776744 --Trace: classic<br>Protocol: TCP<br>DSCP: 0 --> 281474976776744_server([srvora01.lrabb.de:1521])
281474976776737("Stranger - Database"<br>Type: agent-to-server, Interval: 60s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976776737
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976776737
281474976776737 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976776737_server([srv047.lrabb.de:1433])
281474976776738("Stranger - Fileshare"<br>Type: agent-to-server, Interval: 120s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976776738
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976776738
281474976776738 --Trace: classic<br>Protocol: TCP<br>DSCP: 0 --> 281474976776738_server([w2k11.lrabb.de:445])
classDef teAgent fill:#f80

##### END - Label: Use-Case_Apps-Services - END #####

##### START - Label: Webex - START #####
---
title: Webex
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770663("Webex - lrabb - EMEA - Video - 9000"<br>Type: agent-to-agent, Interval: 60s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
281474976770663 --Trace: classic<br>Protocol: UDP/9000<br>DSCP: 34 --> 281474976770663_agent(["Frankfurt, Germany (Webex)"])
281474976770664("Webex - lrabb - DNS"<br>Type: dns-server, Interval: 900s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
281474976770664 --Trace: classic--> 281474976711397([ns1.as13445.net.])
281474976770664 --Trace: classic--> 281474976711398([ns2.as13445.net.])
281474976770662("Webex - lrabb - Server"<br>Type: http-server, Interval: 60s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
281474976770662 --Trace: classic<br>Protocol: ICMP --> 281474976770662_url([https://lrabb.webex.com])
classDef teAgent fill:#f80

##### END - Label: Webex - END #####

##### START - Label: Webex Voice Tests - START #####
---
title: Webex Voice Tests
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
classDef teAgent fill:#f80

##### END - Label: Webex Voice Tests - END #####

##### START - Label: LRABB Services - START #####
---
title: LRABB Services
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976771877("LRABB - REXX"<br>Type: http-server, Interval: 120s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976771877
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976771877
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976771877
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976771877
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976771877
281474976771877 --Trace: classic<br>Protocol: TCP --> 281474976771877_url([https://lrabb-er.rexx-systems.com])
281474976770751("LRABB Service Bürgerinfo"<br>Type: page-load, Interval: 300s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
281474976770751 --Trace: classic<br>Protocol: TCP --> 281474976770751_url([https://service.lrabb.de/bi])
281474976770752("LRABB Service Ratsinfo"<br>Type: page-load, Interval: 300s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
281474976770752 --Trace: classic<br>Protocol: TCP --> 281474976770752_url([https://service.lrabb.de/ri])
281474976770750("LRABB Service Teststellenmeldung"<br>Type: page-load, Interval: 300s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
281474976770750 --Trace: classic<br>Protocol: TCP --> 281474976770750_url([https://teststellenmeldung.lrabb.de:39000])
classDef teAgent fill:#f80

##### END - Label: LRABB Services - END #####

##### START - Label: Use-Case_Collaboration - START #####
---
title: Use-Case_Collaboration
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770663("Webex - lrabb - EMEA - Video - 9000"<br>Type: agent-to-agent, Interval: 60s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
281474976770663 --Trace: classic<br>Protocol: UDP/9000<br>DSCP: 34 --> 281474976770663_agent(["Frankfurt, Germany (Webex)"])
281474976771901("Skype Frontend TCP/5067"<br>Type: agent-to-server, Interval: 60s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976771901
281474976771901 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976771901_server([10.172.58.40:5067])
281474976776751("Skype Polycom - Telefon"<br>Type: agent-to-server, Interval: 60s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976776751
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976776751
281474976776751 --Trace: classic<br>Protocol: ICMP<br>DSCP: 46 --> 281474976776751_server([10.172.16.11])
281474976772940("Skype SBC - Audiocodes01 tcp/5066"<br>Type: agent-to-server, Interval: 60s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976772940
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976772940
281474976772940 --Trace: classic<br>Protocol: TCP<br>DSCP: 0 --> 281474976772940_server([10.175.168.34:5066])
281474976770664("Webex - lrabb - DNS"<br>Type: dns-server, Interval: 900s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
281474976770664 --Trace: classic--> 281474976711397([ns1.as13445.net.])
281474976770664 --Trace: classic--> 281474976711398([ns2.as13445.net.])
281474976774213("S4B Loadbalance"<br>Type: http-server, Interval: 120s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976774213
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976774213
281474976774213 --Trace: classic<br>Protocol: TCP --> 281474976774213_url([https://s4b19poolbblra.lrabb.de])
281474976774226("S4B Loadbalance Edge"<br>Type: http-server, Interval: 120s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976774226
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976774226
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976774226
281474976774226 --Trace: classic<br>Protocol: TCP --> 281474976774226_url([https://skype2019-ext.lrabb.de])
281474976771900("Skype Frontend - Srvsfb01"<br>Type: http-server, Interval: 120s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976771900
281474976771900 --Trace: classic<br>Protocol: TCP --> 281474976771900_url([https://10.172.58.40])
281474976771903("Skype Frontend - Srvsfb02"<br>Type: http-server, Interval: 120s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976771903
281474976771903 --Trace: classic<br>Protocol: TCP --> 281474976771903_url([https://10.172.58.41])
281474976774202("Skype Frontend - Srvsfb03"<br>Type: http-server, Interval: 120s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976774202
281474976774202 --Trace: classic<br>Protocol: TCP --> 281474976774202_url([https://10.172.58.42])
281474976774205("Skype Frontend - Srvsfb04"<br>Type: http-server, Interval: 120s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976774205
281474976774205 --Trace: classic<br>Protocol: TCP --> 281474976774205_url([https://10.172.58.43])
281474976774203("Skype Frontend - Srvsfb05"<br>Type: http-server, Interval: 120s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976774203
281474976774203 --Trace: classic<br>Protocol: TCP --> 281474976774203_url([https://10.172.58.44])
281474976771902("Skype SBC - Audiocodes01"<br>Type: http-server, Interval: 120s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976771902
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976771902
281474976771902 --Trace: classic<br>Protocol: TCP --> 281474976771902_url([https://10.175.168.34])
281474976770662("Webex - lrabb - Server"<br>Type: http-server, Interval: 60s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
281474976770662 --Trace: classic<br>Protocol: ICMP --> 281474976770662_url([https://lrabb.webex.com])
classDef teAgent fill:#f80

##### END - Label: Use-Case_Collaboration - END #####

##### START - Label: Network Health Overview - START #####
---
title: Network Health Overview
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770663("Webex - lrabb - EMEA - Video - 9000"<br>Type: agent-to-agent, Interval: 60s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
281474976770663 --Trace: classic<br>Protocol: UDP/9000<br>DSCP: 34 --> 281474976770663_agent(["Frankfurt, Germany (Webex)"])
281474976770673("VPN GW C1 - tcp/113"<br>Type: agent-to-server, Interval: 120s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
281474976770673 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976770673_server([194.0.93.94:113])
281474976770677("VPN GW C2 - tcp/113"<br>Type: agent-to-server, Interval: 120s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
281474976770677 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976770677_server([194.0.93.95:113])
281474976770667("LRABB - DNS"<br>Type: dns-server, Interval: 900s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770667
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770667
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770667
281474976770667 --Trace: inSession--> 281474976734036([k1z01s003.kivbf.de.])
281474976770667 --Trace: inSession--> 281474976734037([k1z01s004.kivbf.de.])
281474976770667 --Trace: inSession--> 281474976734038([ns.frei.net.])
281474976770664("Webex - lrabb - DNS"<br>Type: dns-server, Interval: 900s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
281474976770664 --Trace: classic--> 281474976711397([ns1.as13445.net.])
281474976770664 --Trace: classic--> 281474976711398([ns2.as13445.net.])
281474976770662("Webex - lrabb - Server"<br>Type: http-server, Interval: 60s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
281474976770662 --Trace: classic<br>Protocol: ICMP --> 281474976770662_url([https://lrabb.webex.com])
281474976770626("LRABB - Website - https://www.lrabb.de"<br>Type: page-load, Interval: 300s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976770626
281474976770626 --Trace: classic<br>Protocol: TCP --> 281474976770626_url([https://www.lrabb.de])
281474976770751("LRABB Service Bürgerinfo"<br>Type: page-load, Interval: 300s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
281474976770751 --Trace: classic<br>Protocol: TCP --> 281474976770751_url([https://service.lrabb.de/bi])
281474976770752("LRABB Service Ratsinfo"<br>Type: page-load, Interval: 300s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
281474976770752 --Trace: classic<br>Protocol: TCP --> 281474976770752_url([https://service.lrabb.de/ri])
281474976770750("LRABB Service Teststellenmeldung"<br>Type: page-load, Interval: 300s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
281474976770750 --Trace: classic<br>Protocol: TCP --> 281474976770750_url([https://teststellenmeldung.lrabb.de:39000])
classDef teAgent fill:#f80

##### END - Label: Network Health Overview - END #####

##### START - Label: Webex - START #####
---
title: Webex
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770663("Webex - lrabb - EMEA - Video - 9000"<br>Type: agent-to-agent, Interval: 60s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
281474976770663 --Trace: classic<br>Protocol: UDP/9000<br>DSCP: 34 --> 281474976770663_agent(["Frankfurt, Germany (Webex)"])
281474976770664("Webex - lrabb - DNS"<br>Type: dns-server, Interval: 900s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
281474976770664 --Trace: classic--> 281474976711397([ns1.as13445.net.])
281474976770664 --Trace: classic--> 281474976711398([ns2.as13445.net.])
281474976770662("Webex - lrabb - Server"<br>Type: http-server, Interval: 60s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
281474976770662 --Trace: classic<br>Protocol: ICMP --> 281474976770662_url([https://lrabb.webex.com])
classDef teAgent fill:#f80

##### END - Label: Webex - END #####

##### START - Label: LRABB Services - START #####
---
title: LRABB Services
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976771877("LRABB - REXX"<br>Type: http-server, Interval: 120s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976771877
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976771877
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976771877
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976771877
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976771877
281474976771877 --Trace: classic<br>Protocol: TCP --> 281474976771877_url([https://lrabb-er.rexx-systems.com])
281474976770751("LRABB Service Bürgerinfo"<br>Type: page-load, Interval: 300s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
281474976770751 --Trace: classic<br>Protocol: TCP --> 281474976770751_url([https://service.lrabb.de/bi])
281474976770752("LRABB Service Ratsinfo"<br>Type: page-load, Interval: 300s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
281474976770752 --Trace: classic<br>Protocol: TCP --> 281474976770752_url([https://service.lrabb.de/ri])
281474976770750("LRABB Service Teststellenmeldung"<br>Type: page-load, Interval: 300s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
281474976770750 --Trace: classic<br>Protocol: TCP --> 281474976770750_url([https://teststellenmeldung.lrabb.de:39000])
classDef teAgent fill:#f80

##### END - Label: LRABB Services - END #####

##### START - Label: Webex Voice Tests - START #####
---
title: Webex Voice Tests
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
classDef teAgent fill:#f80

##### END - Label: Webex Voice Tests - END #####

##### START - Label: Use-Case_Apps-Services - START #####
---
title: Use-Case_Apps-Services
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976776744("ACS - Database"<br>Type: agent-to-server, Interval: 60s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976776744
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976776744
281474976776744 --Trace: classic<br>Protocol: TCP<br>DSCP: 0 --> 281474976776744_server([srvora01.lrabb.de:1521])
281474976776737("Stranger - Database"<br>Type: agent-to-server, Interval: 60s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976776737
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976776737
281474976776737 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976776737_server([srv047.lrabb.de:1433])
281474976776738("Stranger - Fileshare"<br>Type: agent-to-server, Interval: 120s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976776738
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976776738
281474976776738 --Trace: classic<br>Protocol: TCP<br>DSCP: 0 --> 281474976776738_server([w2k11.lrabb.de:445])
classDef teAgent fill:#f80

##### END - Label: Use-Case_Apps-Services - END #####

##### START - Label: Use-Case_Collaboration - START #####
---
title: Use-Case_Collaboration
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770663("Webex - lrabb - EMEA - Video - 9000"<br>Type: agent-to-agent, Interval: 60s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
281474976770663 --Trace: classic<br>Protocol: UDP/9000<br>DSCP: 34 --> 281474976770663_agent(["Frankfurt, Germany (Webex)"])
281474976771901("Skype Frontend TCP/5067"<br>Type: agent-to-server, Interval: 60s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976771901
281474976771901 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976771901_server([10.172.58.40:5067])
281474976776751("Skype Polycom - Telefon"<br>Type: agent-to-server, Interval: 60s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976776751
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976776751
281474976776751 --Trace: classic<br>Protocol: ICMP<br>DSCP: 46 --> 281474976776751_server([10.172.16.11])
281474976772940("Skype SBC - Audiocodes01 tcp/5066"<br>Type: agent-to-server, Interval: 60s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976772940
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976772940
281474976772940 --Trace: classic<br>Protocol: TCP<br>DSCP: 0 --> 281474976772940_server([10.175.168.34:5066])
281474976770664("Webex - lrabb - DNS"<br>Type: dns-server, Interval: 900s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
281474976770664 --Trace: classic--> 281474976711397([ns1.as13445.net.])
281474976770664 --Trace: classic--> 281474976711398([ns2.as13445.net.])
281474976774213("S4B Loadbalance"<br>Type: http-server, Interval: 120s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976774213
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976774213
281474976774213 --Trace: classic<br>Protocol: TCP --> 281474976774213_url([https://s4b19poolbblra.lrabb.de])
281474976774226("S4B Loadbalance Edge"<br>Type: http-server, Interval: 120s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976774226
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976774226
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976774226
281474976774226 --Trace: classic<br>Protocol: TCP --> 281474976774226_url([https://skype2019-ext.lrabb.de])
281474976771900("Skype Frontend - Srvsfb01"<br>Type: http-server, Interval: 120s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976771900
281474976771900 --Trace: classic<br>Protocol: TCP --> 281474976771900_url([https://10.172.58.40])
281474976771903("Skype Frontend - Srvsfb02"<br>Type: http-server, Interval: 120s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976771903
281474976771903 --Trace: classic<br>Protocol: TCP --> 281474976771903_url([https://10.172.58.41])
281474976774202("Skype Frontend - Srvsfb03"<br>Type: http-server, Interval: 120s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976774202
281474976774202 --Trace: classic<br>Protocol: TCP --> 281474976774202_url([https://10.172.58.42])
281474976774205("Skype Frontend - Srvsfb04"<br>Type: http-server, Interval: 120s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976774205
281474976774205 --Trace: classic<br>Protocol: TCP --> 281474976774205_url([https://10.172.58.43])
281474976774203("Skype Frontend - Srvsfb05"<br>Type: http-server, Interval: 120s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976774203
281474976774203 --Trace: classic<br>Protocol: TCP --> 281474976774203_url([https://10.172.58.44])
281474976771902("Skype SBC - Audiocodes01"<br>Type: http-server, Interval: 120s)
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976771902
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976771902
281474976771902 --Trace: classic<br>Protocol: TCP --> 281474976771902_url([https://10.175.168.34])
281474976770662("Webex - lrabb - Server"<br>Type: http-server, Interval: 60s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
281474976770662 --Trace: classic<br>Protocol: ICMP --> 281474976770662_url([https://lrabb.webex.com])
classDef teAgent fill:#f80

##### END - Label: Use-Case_Collaboration - END #####

##### START - Label: LRABB - Website - START #####
---
title: LRABB - Website
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770626("LRABB - Website - https://www.lrabb.de"<br>Type: page-load, Interval: 300s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976770626
281474976770626 --Trace: classic<br>Protocol: TCP --> 281474976770626_url([https://www.lrabb.de])
classDef teAgent fill:#f80

##### END - Label: LRABB - Website - END #####

##### START - Label: Use-Case_Home-Office - START #####
---
title: Use-Case_Home-Office
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770673("VPN GW C1 - tcp/113"<br>Type: agent-to-server, Interval: 120s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
281474976770673 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976770673_server([194.0.93.94:113])
281474976770677("VPN GW C2 - tcp/113"<br>Type: agent-to-server, Interval: 120s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
281474976770677 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976770677_server([194.0.93.95:113])
classDef teAgent fill:#f80

##### END - Label: Use-Case_Home-Office - END #####

##### START - Label: Webex Video Tests - START #####
---
title: Webex Video Tests
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770663("Webex - lrabb - EMEA - Video - 9000"<br>Type: agent-to-agent, Interval: 60s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
281474976770663 --Trace: classic<br>Protocol: UDP/9000<br>DSCP: 34 --> 281474976770663_agent(["Frankfurt, Germany (Webex)"])
classDef teAgent fill:#f80

##### END - Label: Webex Video Tests - END #####

##### START - Label: Network Health Overview - START #####
---
title: Network Health Overview
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770663("Webex - lrabb - EMEA - Video - 9000"<br>Type: agent-to-agent, Interval: 60s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
281474976770663 --Trace: classic<br>Protocol: UDP/9000<br>DSCP: 34 --> 281474976770663_agent(["Frankfurt, Germany (Webex)"])
281474976770673("VPN GW C1 - tcp/113"<br>Type: agent-to-server, Interval: 120s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
281474976770673 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976770673_server([194.0.93.94:113])
281474976770677("VPN GW C2 - tcp/113"<br>Type: agent-to-server, Interval: 120s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
281474976770677 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976770677_server([194.0.93.95:113])
281474976770667("LRABB - DNS"<br>Type: dns-server, Interval: 900s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770667
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770667
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770667
281474976770667 --Trace: inSession--> 281474976734036([k1z01s003.kivbf.de.])
281474976770667 --Trace: inSession--> 281474976734037([k1z01s004.kivbf.de.])
281474976770667 --Trace: inSession--> 281474976734038([ns.frei.net.])
281474976770664("Webex - lrabb - DNS"<br>Type: dns-server, Interval: 900s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
281474976770664 --Trace: classic--> 281474976711397([ns1.as13445.net.])
281474976770664 --Trace: classic--> 281474976711398([ns2.as13445.net.])
281474976770662("Webex - lrabb - Server"<br>Type: http-server, Interval: 60s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
281474976770662 --Trace: classic<br>Protocol: ICMP --> 281474976770662_url([https://lrabb.webex.com])
281474976770626("LRABB - Website - https://www.lrabb.de"<br>Type: page-load, Interval: 300s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976770626
281474976770626 --Trace: classic<br>Protocol: TCP --> 281474976770626_url([https://www.lrabb.de])
281474976770751("LRABB Service Bürgerinfo"<br>Type: page-load, Interval: 300s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
281474976770751 --Trace: classic<br>Protocol: TCP --> 281474976770751_url([https://service.lrabb.de/bi])
281474976770752("LRABB Service Ratsinfo"<br>Type: page-load, Interval: 300s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
281474976770752 --Trace: classic<br>Protocol: TCP --> 281474976770752_url([https://service.lrabb.de/ri])
281474976770750("LRABB Service Teststellenmeldung"<br>Type: page-load, Interval: 300s)
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
281474976770750 --Trace: classic<br>Protocol: TCP --> 281474976770750_url([https://teststellenmeldung.lrabb.de:39000])
classDef teAgent fill:#f80

##### END - Label: Network Health Overview - END #####

##### START - Label: Use-Case_Home-Office - START #####
---
title: Use-Case_Home-Office
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770673("VPN GW C1 - tcp/113"<br>Type: agent-to-server, Interval: 120s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
281474976770673 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976770673_server([194.0.93.94:113])
281474976770677("VPN GW C2 - tcp/113"<br>Type: agent-to-server, Interval: 120s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
281474976770677 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976770677_server([194.0.93.95:113])
classDef teAgent fill:#f80
classDef teTest fill:#f100

##### END - Label: Use-Case_Home-Office - END #####

##### START - Label: LRABB - Website - START #####
---
title: LRABB - Website
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770626("LRABB - Website - https://www.lrabb.de"<br>Type: page-load, Interval: 300s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976770626
281474976770626 --Trace: classic<br>Protocol: TCP --> 281474976770626_url([https://www.lrabb.de])
classDef teAgent fill:#f80
classDef teTest fill:#f100

##### END - Label: LRABB - Website - END #####

##### START - Label: Webex Video Tests - START #####
---
title: Webex Video Tests
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770663("Webex - lrabb - EMEA - Video - 9000"<br>Type: agent-to-agent, Interval: 60s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
281474976770663 --Trace: classic<br>Protocol: UDP/9000<br>DSCP: 34 --> 281474976770663_agent(["Frankfurt, Germany (Webex)"])
classDef teAgent fill:#f80
classDef teTest fill:#f100

##### END - Label: Webex Video Tests - END #####

##### START - Label: Use-Case_Apps-Services - START #####
---
title: Use-Case_Apps-Services
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976776744("ACS - Database"<br>Type: agent-to-server, Interval: 60s):::teTest
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976776744
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976776744
281474976776744 --Trace: classic<br>Protocol: TCP<br>DSCP: 0 --> 281474976776744_server([srvora01.lrabb.de:1521])
281474976776737("Stranger - Database"<br>Type: agent-to-server, Interval: 60s):::teTest
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976776737
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976776737
281474976776737 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976776737_server([srv047.lrabb.de:1433])
281474976776738("Stranger - Fileshare"<br>Type: agent-to-server, Interval: 120s):::teTest
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976776738
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976776738
281474976776738 --Trace: classic<br>Protocol: TCP<br>DSCP: 0 --> 281474976776738_server([w2k11.lrabb.de:445])
classDef teAgent fill:#f80
classDef teTest fill:#f100

##### END - Label: Use-Case_Apps-Services - END #####

##### START - Label: Webex - START #####
---
title: Webex
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770663("Webex - lrabb - EMEA - Video - 9000"<br>Type: agent-to-agent, Interval: 60s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
281474976770663 --Trace: classic<br>Protocol: UDP/9000<br>DSCP: 34 --> 281474976770663_agent(["Frankfurt, Germany (Webex)"])
281474976770664("Webex - lrabb - DNS"<br>Type: dns-server, Interval: 900s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
281474976770664 --Trace: classic--> 281474976711397([ns1.as13445.net.])
281474976770664 --Trace: classic--> 281474976711398([ns2.as13445.net.])
281474976770662("Webex - lrabb - Server"<br>Type: http-server, Interval: 60s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
281474976770662 --Trace: classic<br>Protocol: ICMP --> 281474976770662_url([https://lrabb.webex.com])
classDef teAgent fill:#f80
classDef teTest fill:#f100

##### END - Label: Webex - END #####

##### START - Label: Webex Voice Tests - START #####
---
title: Webex Voice Tests
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
classDef teAgent fill:#f80
classDef teTest fill:#f100

##### END - Label: Webex Voice Tests - END #####

##### START - Label: LRABB Services - START #####
---
title: LRABB Services
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976771877("LRABB - REXX"<br>Type: http-server, Interval: 120s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976771877
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976771877
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976771877
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976771877
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976771877
281474976771877 --Trace: classic<br>Protocol: TCP --> 281474976771877_url([https://lrabb-er.rexx-systems.com])
281474976770751("LRABB Service Bürgerinfo"<br>Type: page-load, Interval: 300s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
281474976770751 --Trace: classic<br>Protocol: TCP --> 281474976770751_url([https://service.lrabb.de/bi])
281474976770752("LRABB Service Ratsinfo"<br>Type: page-load, Interval: 300s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
281474976770752 --Trace: classic<br>Protocol: TCP --> 281474976770752_url([https://service.lrabb.de/ri])
281474976770750("LRABB Service Teststellenmeldung"<br>Type: page-load, Interval: 300s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
281474976770750 --Trace: classic<br>Protocol: TCP --> 281474976770750_url([https://teststellenmeldung.lrabb.de:39000])
classDef teAgent fill:#f80
classDef teTest fill:#f100

##### END - Label: LRABB Services - END #####

##### START - Label: Use-Case_Collaboration - START #####
---
title: Use-Case_Collaboration
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770663("Webex - lrabb - EMEA - Video - 9000"<br>Type: agent-to-agent, Interval: 60s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
281474976770663 --Trace: classic<br>Protocol: UDP/9000<br>DSCP: 34 --> 281474976770663_agent(["Frankfurt, Germany (Webex)"])
281474976771901("Skype Frontend TCP/5067"<br>Type: agent-to-server, Interval: 60s):::teTest
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976771901
281474976771901 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976771901_server([10.172.58.40:5067])
281474976776751("Skype Polycom - Telefon"<br>Type: agent-to-server, Interval: 60s):::teTest
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976776751
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976776751
281474976776751 --Trace: classic<br>Protocol: ICMP<br>DSCP: 46 --> 281474976776751_server([10.172.16.11])
281474976772940("Skype SBC - Audiocodes01 tcp/5066"<br>Type: agent-to-server, Interval: 60s):::teTest
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976772940
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976772940
281474976772940 --Trace: classic<br>Protocol: TCP<br>DSCP: 0 --> 281474976772940_server([10.175.168.34:5066])
281474976770664("Webex - lrabb - DNS"<br>Type: dns-server, Interval: 900s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
281474976770664 --Trace: classic--> 281474976711397([ns1.as13445.net.])
281474976770664 --Trace: classic--> 281474976711398([ns2.as13445.net.])
281474976774213("S4B Loadbalance"<br>Type: http-server, Interval: 120s):::teTest
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976774213
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976774213
281474976774213 --Trace: classic<br>Protocol: TCP --> 281474976774213_url([https://s4b19poolbblra.lrabb.de])
281474976774226("S4B Loadbalance Edge"<br>Type: http-server, Interval: 120s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976774226
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976774226
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976774226
281474976774226 --Trace: classic<br>Protocol: TCP --> 281474976774226_url([https://skype2019-ext.lrabb.de])
281474976771900("Skype Frontend - Srvsfb01"<br>Type: http-server, Interval: 120s):::teTest
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976771900
281474976771900 --Trace: classic<br>Protocol: TCP --> 281474976771900_url([https://10.172.58.40])
281474976771903("Skype Frontend - Srvsfb02"<br>Type: http-server, Interval: 120s):::teTest
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976771903
281474976771903 --Trace: classic<br>Protocol: TCP --> 281474976771903_url([https://10.172.58.41])
281474976774202("Skype Frontend - Srvsfb03"<br>Type: http-server, Interval: 120s):::teTest
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976774202
281474976774202 --Trace: classic<br>Protocol: TCP --> 281474976774202_url([https://10.172.58.42])
281474976774205("Skype Frontend - Srvsfb04"<br>Type: http-server, Interval: 120s):::teTest
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976774205
281474976774205 --Trace: classic<br>Protocol: TCP --> 281474976774205_url([https://10.172.58.43])
281474976774203("Skype Frontend - Srvsfb05"<br>Type: http-server, Interval: 120s):::teTest
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976774203
281474976774203 --Trace: classic<br>Protocol: TCP --> 281474976774203_url([https://10.172.58.44])
281474976771902("Skype SBC - Audiocodes01"<br>Type: http-server, Interval: 120s):::teTest
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976771902
281474976728755(["thousandeyes-va02<br>IP: 10.175.168.114<br>(Enterprise Agent)"]):::teAgent --- 281474976771902
281474976771902 --Trace: classic<br>Protocol: TCP --> 281474976771902_url([https://10.175.168.34])
281474976770662("Webex - lrabb - Server"<br>Type: http-server, Interval: 60s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
281474976770662 --Trace: classic<br>Protocol: ICMP --> 281474976770662_url([https://lrabb.webex.com])
classDef teAgent fill:#f80
classDef teTest fill:#f100

##### END - Label: Use-Case_Collaboration - END #####

##### START - Label: Network Health Overview - START #####
---
title: Network Health Overview
config:
  theme: base
  themeVariables:
    primaryColor: '#00ff00'
---
flowchart LR
281474976770663("Webex - lrabb - EMEA - Video - 9000"<br>Type: agent-to-agent, Interval: 60s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770663
281474976770663 --Trace: classic<br>Protocol: UDP/9000<br>DSCP: 34 --> 281474976770663_agent(["Frankfurt, Germany (Webex)"])
281474976770673("VPN GW C1 - tcp/113"<br>Type: agent-to-server, Interval: 120s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770673
281474976770673 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976770673_server([194.0.93.94:113])
281474976770677("VPN GW C2 - tcp/113"<br>Type: agent-to-server, Interval: 120s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770677
281474976770677 --Trace: inSession<br>Protocol: TCP<br>DSCP: 0 --> 281474976770677_server([194.0.93.95:113])
281474976770667("LRABB - DNS"<br>Type: dns-server, Interval: 900s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770667
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770667
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770667
281474976770667 --Trace: inSession--> 281474976734036([k1z01s003.kivbf.de.])
281474976770667 --Trace: inSession--> 281474976734037([k1z01s004.kivbf.de.])
281474976770667 --Trace: inSession--> 281474976734038([ns.frei.net.])
281474976770664("Webex - lrabb - DNS"<br>Type: dns-server, Interval: 900s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770664
281474976770664 --Trace: classic--> 281474976711397([ns1.as13445.net.])
281474976770664 --Trace: classic--> 281474976711398([ns2.as13445.net.])
281474976770662("Webex - lrabb - Server"<br>Type: http-server, Interval: 60s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770662
281474976770662 --Trace: classic<br>Protocol: ICMP --> 281474976770662_url([https://lrabb.webex.com])
281474976770626("LRABB - Website - https://www.lrabb.de"<br>Type: page-load, Interval: 300s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770626
281474976728448(["thousandeyes-va<br>IP: 10.172.58.81<br>(Enterprise Agent)"]):::teAgent --- 281474976770626
281474976770626 --Trace: classic<br>Protocol: TCP --> 281474976770626_url([https://www.lrabb.de])
281474976770751("LRABB Service Bürgerinfo"<br>Type: page-load, Interval: 300s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770751
281474976770751 --Trace: classic<br>Protocol: TCP --> 281474976770751_url([https://service.lrabb.de/bi])
281474976770752("LRABB Service Ratsinfo"<br>Type: page-load, Interval: 300s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770752
281474976770752 --Trace: classic<br>Protocol: TCP --> 281474976770752_url([https://service.lrabb.de/ri])
281474976770750("LRABB Service Teststellenmeldung"<br>Type: page-load, Interval: 300s):::teTest
4844(["Munich, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
4904(["Dusseldorf, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
315431(["Frankfurt, Germany<br>(Cloud Agent)"]):::teAgent --- 281474976770750
281474976770750 --Trace: classic<br>Protocol: TCP --> 281474976770750_url([https://teststellenmeldung.lrabb.de:39000])
classDef teAgent fill:#f80
classDef teTest fill:#f100

##### END - Label: Network Health Overview - END #####
