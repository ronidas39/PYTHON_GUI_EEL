import eel
from datetime import datetime
import platform
import psutil

system=platform.uname()
#print(system)
partition_info=psutil.disk_partitions()

memory_info=psutil.virtual_memory()
print(memory_info)
eel.init("HTMLS")
@eel.expose
def generate_data():
    def size_utility(size,initials="B"):
        factor=1024
        for memory_unit in ["","k","M","G","T","P"]:
         if size<factor:
            return(f"{size:.2f}{memory_unit}{initials}")
         size/=factor
    system=platform.uname()
    data={}
    data.update({"Operating System Type":system.system})
    data.update({"System Name":system.node})
    data.update({"Os Release":system.release})
    data.update({"Os Version":system.version})
    data.update({"Processor Type":system.machine})
    data.update({"Processor Category":system.processor})
    memory_info=psutil.virtual_memory()
    data.update({"Total Ram":size_utility(memory_info.total)})
    data.update({"Available Ram":size_utility(memory_info.available)})
    data.update({"Used Ram":size_utility(memory_info.used)})
    data.update({"Percentage Used":str(memory_info.percent)+"%"})
    partition_info=psutil.disk_partitions()
    for partition in partition_info:
        try:
         drive_size=psutil.disk_usage(partition.mountpoint)
         data.update({"Drive Name":partition.mountpoint})
         data.update({"Drive Size":size_utility(drive_size.total)})
         data.update({"Drive Used":size_utility(drive_size.used)})
         data.update({"Drive Free Space":size_utility(drive_size.free)})
         data.update({"Drive Used Percentage":str(drive_size.percent)+"%"})
        except:
            pass
        
    return data
eel.start("systeminfo.html",size=(1024,900))