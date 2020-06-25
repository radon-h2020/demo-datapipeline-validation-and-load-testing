import pandas as pd
pd.set_option('display.max_columns', None)
df = pd.read_csv('servers.txt', sep =",")

df.drop(df.columns[0],axis=1,inplace=True)

df.columns = df.columns.str.replace(' ', '')
cols = ['ID', 'Name', 'Status', 'TaskState', 'PowerState', 'Networks']
for i in cols:
    df[i] = df[i].str.strip()

df['Networks'] = df['Networks'].astype('str')
iplist =[]
df = df[df['Name'].str.contains("vm_centos_radon")]
for i in df['Networks']:
    network = i.split("=")
    ip = network[1]
    ip_port = ", '" + ip + ":9100'"
    iplist.append(ip_port)
  
target = " "
for i in range(len(iplist)):
    
    target = target + iplist[i]
    
    
#print(target)    
output_file=open('prometheus.yml', 'w')
output_file.write("global:\n")
output_file.write("  scrape_interval: 10s\n")
output_file.write("scrape_configs:\n")
output_file.write("    - job_name: 'prometheus'\n")
output_file.write("      scrape_interval: 5s\n")
output_file.write("      static_configs:\n")
output_file.write("        - targets: ['localhost:9090']\n")
output_file.write("    - job_name: 'node_exporter_metrics'\n")
output_file.write("      scrape_interval: 5s\n")
output_file.write("      static_configs:\n")
output_file.write("        - targets: ["+ target + "]")
