import json
import re

output = []

with open("show fulltech E5520-TMC-GF-SW01.txt","r", encoding='latin-1') as file :
    data= file.read()
    lines = data.split('\n')
    
for line in lines : 
    match = re.match(r"^(\d+\/\d+)\s+(\w+\(\d+\))\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)", line)
    if match :
        result = {"PortID":match.groups()[0],"PktType":match.groups()[1],"RxPkts":match.groups()[2],"RxDiff":match.groups()[3],"RxPps":match.groups()[4],"TxPkts":match.groups()[5],"TxDiff":match.groups()[6],"TxPps":match.groups()[7]}
        output.append(result)

sorted_output = sorted(output, key = (lambda x : x['TxDiff']), reverse = True) 

with open("sort_by_TxDiff_result.json","w") as file :
    file.write(json.dumps(sorted_output, indent = 4)) 
