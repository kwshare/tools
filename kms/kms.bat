
# office 2013

cd 'C:\Program Files\Microsoft Office\Office15'
cscript ospp.vbs /sethst:192.168.7.1
cscript ospp.vbs /act
cscript ospp.vbs /dstatus



# Windows 10

slmgr.vbs /upk
slmgr.vbs /skms 192.168.7.1
slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX
slmgr.vbs /ato
slmgr.vbs /xpr

# Windows 7

slmgr.vbs /upk
slmgr.vbs /skms 192.168.7.1
slmgr.vbs /ipk FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4
slmgr.vbs /ato
slmgr.vbs /xpr