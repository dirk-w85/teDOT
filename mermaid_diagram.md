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