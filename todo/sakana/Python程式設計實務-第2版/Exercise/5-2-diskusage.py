import os
disk = os.statvfs("/")
print( disk )
freespace = disk.f_bsize * disk.f_blocks
print(freespace)