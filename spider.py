import requests
import re
import json
import csv
import pandas as pd

url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
    'cookie': 'BIDUPSID=570D09A1FD5745661BA2B5AD670679BA; PSTM=1625101885; BAIDUID=570D09A1FD5745662871F782C73D5034:FG=1; BAIDUID_BFESS=356D069EA813A557B35A95EF3E7F8661:FG=1; ZFY=KvEnCJORolbWSiMbmbUDkZqHXswB:ANUOVwvwOW2KZQ0:C; BDUSS_BFESS=FBjZElQdHhIdGItVVJtRDZten5iY3NiNGxMelFvQVRlRElaQ3UtamY3UEY1TFZpRUFBQUFBJCQAAAAAAAAAAAEAAABOH8J-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMVXjmLFV45ie; lscaptain=srcactivitycaptainindexcss_91e010cf-srccommonlibsesljs_e3d2f596-srcactivitycaptainindexjs_a2e9c712; Hm_lvt_68bd357b1731c0f15d8dbfef8c216d15=1654839616; Hm_lpvt_68bd357b1731c0f15d8dbfef8c216d15=1654839616'
}
response=requests.get(url=url,headers=headers)
data_html=response.text

json_str=re.findall('"component":\[(.*)\],',data_html)[0]  #解析数据
json_dict=json.loads(json_str)
caseList=json_dict['caseList']

fdata = open('./data.csv',mode='a',encoding='utf-8',newline='')
csv_writer=csv.writer(fdata)
for i in caseList:
    area=i['area']
    confirmed=i['confirmed']
    curConfirm=i['curConfirm']
    asymptomatic=i['asymptomatic']
    cured=i['crued']
    died=i['died']
    confirmedRelative=i['confirmedRelative']
    diedRelative=i['diedRelative']
    curedRelative=i['curedRelative']
    asymptomaticRelative=i['asymptomaticRelative']
    nativeRelative=i['nativeRelative']
    overseasInputRelative=i['overseasInputRelative']
    csv_writer.writerow([area,confirmed,curConfirm,confirmedRelative,nativeRelative,overseasInputRelative,asymptomatic,asymptomaticRelative,cured,curedRelative,died,diedRelative])
df = pd.read_csv('data.csv',header=None,names=['省份','累计确诊','确诊','新增确诊','本土新增','境外输入','无症状','新增无症状','累计治愈','新增治愈','累计死亡','新增死亡'])
df.to_csv('data.csv',index=False)
