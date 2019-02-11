from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)
domainIDs=conn.listDomainsID()
print(domainIDs)
domains=conn.listAllDomains(0)
print(domains)
conn.close()

