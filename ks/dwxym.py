import random
import json
import os
import sys
import logging
import time
import re
import requests
logging.basicConfig(level=logging.INFO,format='%(message)s')
logger=logging.getLogger(__name__)
token='wo_5_2022_07_26_06_13_1873f9df72596*00b27a9d59d975d5296f6a9432dc1*82fe437ab2e339'
sleep_time=random.randint(2,6)
ksjsbtask='no'
web_list=['47.243.248.136:3334','8.210.215.40:3334','183.57.37.247:3334','124.220.48.76:3334','101.33.252.145:3334']
def radom_web():
 return random.choice(web_list)
radom_web=radom_web()
def get_web_task(want_id,token,cookie_list,change_value,type_name=None,which_on=None):
 try:
  url='http://'+radom_web+'/api_list'
  data={"want_id":want_id,"token":token,"cookie_list":cookie_list,"change_value":change_value,"type_name":type_name,"which_one":which_on}
  re=requests.post(url=url,json=data).text
  re=json.loads(re)['data']
  return re
 except ConnectionResetError:
  logger.info(f"��������,��������ж�,���½ű����Ժ�����,��ʱ30s")
  time.sleep(30)
def get_time():
 return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
def is_today(t1,t2,tz_count=28800):
 if int((int(t1)+int(tz_count))/86400)==int((int(t2)+int(tz_count))/86400):
  return True
 else:
  return False
def get_nama_cash(cookie,did):
 url='https://nebula.kuaishou.com/rest/n/nebula/activity/earn/overview/basicInfo'
 headers={'Accept-Encoding':'gzip, deflate','Cookie':'kpn=NEBULA; kpf=ANDROID_PHONE;c=XIAOMI; ver=10.5; appver=10.5.31.3825; client_key=2ac2a76d; language=zh-cn; countryCode=CN; sys=ANDROID_9; mod=Xiaomi%28MI+6%29; net=WIFI; deviceName=Xiaomi%28MI+6%29; isp=; did_tag=7;kcv=1458; app=0; bottom_navigation=true; android_os=0; boardPlatform=msm8998; androidApiLevel=28; newOc=XIAOMI; slh=0; country_code=cn; nbh=0; hotfix_ver=; did_gt=1652302313321; keyconfig_state=2; max_memory=256; oc=XIAOMI; sh=1920; app_status=3; ddpi=480; deviceBit=0; browseType=3; power_mode=0; socName=Qualcomm+MSM8998; sw=1080; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; totalMemory=5724; grant_browse_type=AUTHORIZED; iuid=; rdid=${$.didi}; sbh=72; darkMode=false; kuaishou.api_st='+cookie+'; kuaishou.h5_st='+cookie+'; is_background=0; is_background=0; did='+did+'; oDid=TEST_'+did+'','Connection':'keep-alive','Accept':'*/*','Accept-Language':'en-us',"User-Agent":'Kwai-android aegon/3.4.0',}
 try:
  redata=requests.get(url=url,headers=headers).text
  re=json.loads(redata)['data']
  player_data={'totalCash':re['totalCash'],'totalCoin':re['totalCoin'],'nickname':re['userData']['nickname'],'api_st':cookie}
 except Exception as e:
  logger.info("��ȡ�û���Ϣ����")
  logger.info(e)
  player_data={'totalCash':"",'totalCoin':"",'nickname':"",'api_st':cookie}
 return player_data
def choujiang(headers):
 while True:
  url_choujing='https://activity.e.kuaishou.com/rest/r/game/lottery?wheelVersion=1'
  re_choujiang=requests.post(url=url_choujing,headers=headers).text
  re_choujiang=json.loads(re_choujiang)
  if re_choujiang["message"]=="6001":
   logger.info("����6001,CKʧЧ")
  data_choujiang=re_choujiang.get('data')
  if re_choujiang['result']==1112:
   return False
  if data_choujiang:
   if data_choujiang['code']==2:
    data=data_choujiang['diamondCount']
    logger.info(f'--�鵽{data}��ʯ--')
    pass
   else:
    return False
  else:
   return False
def one_cash(cookie,did):
 url='https://nebula.kuaishou.com/rest/n/nebula/activity/earn/overview/tasks?addressBookAccessStatus=true&pushNotificationStatus=false'
 headers={'Accept-Encoding':'gzip, deflate','Cookie':'kpn=NEBULA; kpf=ANDROID_PHONE;c=XIAOMI; ver=10.5; appver=10.5.31.3825; client_key=2ac2a76d; language=zh-cn; countryCode=CN; sys=ANDROID_9; mod=Xiaomi%28MI+6%29; net=WIFI; deviceName=Xiaomi%28MI+6%29; isp=; did_tag=7;kcv=1458; app=0; bottom_navigation=true; android_os=0; boardPlatform=msm8998; androidApiLevel=28; newOc=XIAOMI; slh=0; country_code=cn; nbh=0; hotfix_ver=; did_gt=1652302313321; keyconfig_state=2; max_memory=256; oc=XIAOMI; sh=1920; app_status=3; ddpi=480; deviceBit=0; browseType=3; power_mode=0; socName=Qualcomm+MSM8998; sw=1080; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; totalMemory=5724; grant_browse_type=AUTHORIZED; iuid=; rdid=${$.didi}; sbh=72; darkMode=false; kuaishou.api_st='+cookie+'; kuaishou.h5_st='+cookie+'; is_background=0; did='+did+'; oDid=TEST_'+did+'','Connection':'keep-alive','Accept':'*/*','Accept-Language':'en-us',"User-Agent":'Kwai-android aegon/3.4.0',}
 re=requests.get(url=url,headers=headers).text
 re=json.loads(re)
 try:
  nebulaGoldenAreaTask=re['data']['nebulaGoldenAreaTask']
 except Exception as e:
  print('1Ԫ���ֽ����ж�',e)
def sign_today(cookie,did):
 url='https://nebula.kuaishou.com/rest/n/nebula/sign/sign?source=activity'
 headers={'Accept-Encoding':'gzip, deflate','Cookie':'kpn=NEBULA; kpf=ANDROID_PHONE;c=XIAOMI; ver=10.5; appver=10.5.31.3825; client_key=2ac2a76d; language=zh-cn; countryCode=CN; sys=ANDROID_9; mod=Xiaomi%28MI+6%29; net=WIFI; deviceName=Xiaomi%28MI+6%29; isp=; did_tag=7;kcv=1458; app=0; bottom_navigation=true; android_os=0; boardPlatform=msm8998; androidApiLevel=28; newOc=XIAOMI; slh=0; country_code=cn; nbh=0; hotfix_ver=; did_gt=1652302313321; keyconfig_state=2; max_memory=256; oc=XIAOMI; sh=1920; app_status=3; ddpi=480; deviceBit=0; browseType=3; power_mode=0; socName=Qualcomm+MSM8998; sw=1080; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; totalMemory=5724; grant_browse_type=AUTHORIZED; iuid=; rdid=${$.didi}; sbh=72; darkMode=false; kuaishou.api_st='+cookie+'; kuaishou.h5_st='+cookie+'; is_background=0; did='+did+'; oDid=TEST_'+did+'','Connection':'keep-alive','Accept':'*/*','Accept-Language':'en-us',"User-Agent":'Kwai-android aegon/3.4.0',}
 re=json.loads(requests.get(url=url,headers=headers).text)
 choujiang(headers)
 result=re['result']
 if result==1:
  logger.info(re['data']['toast'])
  get_web_task('set_one_value',token,cookie,change_value=False,type_name='sign',which_on='is_run')
  get_web_task('set_one_value',token,cookie,change_value=int(time.time()),type_name='sign',which_on='last_time')
 elif result==10901:
  logger.info(re['error_msg'])
  get_web_task('set_one_value',token,cookie,change_value=False,type_name='sign',which_on='is_run')
  get_web_task('set_one_value',token,cookie,change_value=int(time.time()),type_name='sign',which_on='last_time')
 else:
  logger.info('ǩ�������쳣')
  logger.info(re)
  get_web_task('set_one_value',token,cookie,change_value=False,type_name='sign',which_on='is_run')
  get_web_task('set_one_value',token,cookie,change_value=int(time.time()),type_name='sign',which_on='last_time')
  logger.info('���ռ�¼��ǩ��')
def get_box(cookie,did):
 url='https://nebula.kuaishou.com/rest/n/nebula/box/explore?isOpen=true&isReadyOfAdPlay=true'
 headers={'Accept-Encoding':'gzip, deflate','Cookie':'kpn=NEBULA; kpf=ANDROID_PHONE;c=XIAOMI; ver=10.5; appver=10.5.31.3825; client_key=2ac2a76d; language=zh-cn; countryCode=CN; sys=ANDROID_9; mod=Xiaomi%28MI+6%29; net=WIFI; deviceName=Xiaomi%28MI+6%29; isp=; did_tag=7;kcv=1458; app=0; bottom_navigation=true; android_os=0; boardPlatform=msm8998; androidApiLevel=28; newOc=XIAOMI; slh=0; country_code=cn; nbh=0; hotfix_ver=; did_gt=1652302313321; keyconfig_state=2; max_memory=256; oc=XIAOMI; sh=1920; app_status=3; ddpi=480; deviceBit=0; browseType=3; power_mode=0; socName=Qualcomm+MSM8998; sw=1080; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; totalMemory=5724; grant_browse_type=AUTHORIZED; iuid=; rdid=${$.didi}; sbh=72; darkMode=false; kuaishou.api_st='+cookie+'; kuaishou.h5_st='+cookie+'; is_background=0; is_background=0; did='+did+'; oDid=TEST_'+did+'','Connection':'keep-alive','Accept':'*/*','Accept-Language':'en-us',"User-Agent":'Kwai-android aegon/3.4.0',}
 re=json.loads(requests.get(url=url,headers=headers).text)
 result=re.get('result')
 data=re.get('data')
 if result==1:
  if data:
   commonAwardPopup=data.get('commonAwardPopup')
   treasureBoxOpenTimestamp=data.get('treasureBoxOpenTimestamp')
   if treasureBoxOpenTimestamp==-1:
    get_web_task('set_one_value',token,cookie,change_value=False,type_name='box',which_on='is_run')
    get_web_task('set_one_value',token,cookie,change_value=int(time.time()),type_name='box',which_on='last_time')
    get_web_task('set_one_value',token,cookie,change_value=False,type_name='77',which_on='is_run')
    get_web_task('set_one_value',token,cookie,change_value=int(time.time()),type_name='77',which_on='last_time')
    get_web_task('set_one_value',token,cookie,change_value=False,type_name='0',which_on='is_run')
    get_web_task('set_one_value',token,cookie,change_value=int(time.time()),type_name='0',which_on='last_time')
    logger.info(f"==�������޴���(�������䷭���������Ƶ����),�Զ�����,���첻����=====")
   if commonAwardPopup!=None:
    jinbi=data['commonAwardPopup']['awardAmount']
    logger.info(f"---��������{jinbi}���---")
   else:
    logger.info(f"������ʱ��δ�����޴���")
  else:
   logger.info(f"==��data����=={re}=====")
 else:
  logger.info(f"==������1����=={re}=====")
def get_ck():
 global token
 global ksjsbtask
 if "ksjsbtoken" in os.environ:
  token=os.environ['ksjsbtoken']
 if "ksjsbtask" in os.environ:
  ksjsbtask=os.environ['ksjsbtask']
 if "ksjsbcookie" in os.environ:
  cklist=[]
  wskey_list=os.environ['ksjsbcookie'].replace('http',"@")
  wskey_list=wskey_list.split('@')
  for item in wskey_list:
   if item!='':
    cklist.append(item)
  if len(cklist)>0:
   return cklist
  else:
   logger.info("ksjsbcookie����δ����")
   sys.exit(1)
 else:
  try:
   with open('kscklist.txt','r')as f:
    wskey_list=f.read().split('\n')
   if len(wskey_list)>=1:
    return wskey_list
   else:
    logger.info("δ���ksjsbcookie����,��δ��kscklist.txt�ļ�")
    sys.exit(0)
  except BaseException:
   logger.info("δ���ksjsbcookie����,��δ��kscklist.txt�ļ�")
   sys.exit(0)
def check_ck(cks):
 switch=True
 check_list=['did','rdid','kuaishou.api_st','client_salt']
 cookie_list=[]
 count=0
 for i in cks:
  count+=1
  try:
   for c in check_list:
    if c not in i:
     logger.info(f'ȱ��{c}')
     sys.exit(0)
   cookie=re.search(r'(?<=kuaishou\.api_st=)[A-Za-z0-9_\-]*',i).group()
   did=re.search(r'(?<=&did=)[A-Za-z0-9_\-]*',i).group()
   data=get_nama_cash(cookie,did)
   logger.info(f'--�˺�{data["nickname"]}--�ֽ�{data["totalCash"]}--���{data["totalCoin"]}')
   cookie_list.append([cookie,did,data["nickname"],i])
  except BaseException:
   logger.info(f'��{count}��CK����!����')
   logger.info(f'cookie��{cookie}')
   sys.exit(0)
 if not switch:
  logger.info('��鲻ͨ��,�˳��ű�')
  sys.exit(0)
 return cookie_list
def go_web_requsetion(a,b):
 try:
  url='http://'+radom_web+'/0705api'
  data={"a":a,"b":b,"c":token}
  if b=='Query_token':
   re=requests.post(url=url,data=json.dumps(data)).text
   re=json.loads(re)
   return re
  re=requests.post(url=url,data=json.dumps(data)).text
  re=json.loads(re)
  if not re.get('url'):
   logger.info("û�л�ȡ���������ӣ�30���������")
   time.sleep(30)
   re=requests.post(url=url,data=json.dumps(data)).text
   re=json.loads(re)
  x_requestid=str(int(time.time())*1000)+str(random.randint(00000,99999))
  header={"Host":"api.e.kuaishou.com","Connection":"keep-alive","Content-Length":str(len(re['body'])),"User-Agent":"kwai-android aegon/3.10.0","Accept-Language":"zh-cn","X-REQUESTID":x_requestid,"Content-Type":"application/x-www-form-urlencoded","Accept-Encoding":"gzip, deflate","X-Client-Info":"model=MI 10;os=Android;nqe-score=38;network=WIFI;signal-strength=4;",}
  rere=requests.post(url=re['url'],headers=header,data=re['body'])
  return json.loads(rere.text)
 except Exception as e:
  logger.info(f"��������,��������ж�,���½ű����Ժ�����,��ʱ30s")
  time.sleep(30)
def process_return_value(retrun,key,value,cookie):
 task_dict=['173-500','-1','259','0','253','box']
 task_104=['161-1','11-1']
 message=retrun.get('message')
 if message=='6001':
  return logger.info(f"----�˺�ʧЧ���»�ȡck���߻���did����----")
 if isinstance(retrun['data'],dict)and message=='�ɹ�':
  neoAmount=retrun['data'].get('neoAmount')
  awardAmount=retrun['data'].get('awardAmount')
  if neoAmount is not None:
   if neoAmount<21 and key in task_dict:
    get_web_task('set_one_value',token,cookie,change_value=False,type_name=key,which_on='is_run')
    get_web_task('set_one_value',token,cookie,change_value=int(time.time()),type_name=key,which_on='last_time')
    logger.info(f"---{value}----���{neoAmount}���,���������ڽ��ղ������д�����")
    return 0
   elif neoAmount<21 and key in task_104:
    get_web_task('set_one_value',token,cookie,change_value=False,type_name=key,which_on='is_run')
    get_web_task('set_one_value',token,cookie,change_value=int(time.time()),type_name=key,which_on='last_time')
    logger.info(f"---{value}----���{neoAmount}���,1047���������ڻ����Ѿ���,���ղ������д�����")
    return 0
   else:
    logger.info(f"---{value}----���{neoAmount}���")
    return 1
  if awardAmount is not None:
   if awardAmount<21 and key in task_dict:
    get_web_task('set_one_value',token,cookie,change_value=False,type_name=key,which_on='is_run')
    get_web_task('set_one_value',token,cookie,change_value=int(time.time()),type_name=key,which_on='last_time')
    logger.info(f"---{value}----���{awardAmount}���,����������,���ղ������д�����")
    return 0
   else:
    logger.info(f"---{value}----���{awardAmount}���")
    return 1
 elif '��������' in message:
  get_web_task('set_one_value',token,cookie,change_value=False,type_name=key,which_on='is_run')
  get_web_task('set_one_value',token,cookie,change_value=int(time.time()),type_name=key,which_on='last_time')
  logger.info(f"---{value}---{message}---,���������ڽ��ղ������д�����")
  return 0
 else:
  logger.info(f"---{value}----{message}")
  return 1
def go_task_id(task_id_dict,web_ck_list):
 onece_task=['-1']
 pass_task_id=[]
 for key,value in task_id_dict.items():
  try:
   if key=='sign':
    sign_today(web_ck_list[0],web_ck_list[1])
   elif key in pass_task_id:
    pass
   elif key=='box':
    get_box(web_ck_list[0],web_ck_list[1])
   elif key in onece_task:
    result=go_web_requsetion(web_ck_list[3],key)
    if result['result']==1:
     re=result['data'].get('awardAmount')
     logger.info(f"---{value}----���{re}���,���콱���������ý��ղ������д�����")
     get_web_task('set_one_value',token,web_ck_list[0],change_value=False,type_name=key,which_on='is_run')
     get_web_task('set_one_value',token,web_ck_list[0],change_value=int(time.time()),type_name=key,which_on='last_time')
   else:
    three_onecs=['173-500','80']
    two_onecs=['161-1','11-1']
    if key in three_onecs:
     for i in range(0,8):
      result=go_web_requsetion(web_ck_list[3],key)
      re_process=process_return_value(result,key,value,web_ck_list[0])
      if re_process==0:
       break
      time.sleep(sleep_time)
    elif key in two_onecs:
     for i in range(0,10):
      result=go_web_requsetion(web_ck_list[3],key)
      re_process=process_return_value(result,key,value,web_ck_list[0])
      if re_process==0:
       break
      time.sleep(sleep_time)
    else:
     result=go_web_requsetion(web_ck_list[3],key)
     re_process=process_return_value(result,key,value,web_ck_list[0])
     time.sleep(sleep_time)
  except Exception as e:
   logger.info(f"{key}���������ж�{e}")
def check_net():
 import urllib3
 try:
  http=urllib3.PoolManager()
  http.request('GET','https://baidu.com')
  return True
 except Exception as e:
  logger.info(e)
  logger.info("���л�������ͨ")
  sys.exit(0)
def main():
 logger.info(f'========�ű�ִ��- ����ʱ��(UTC+8)��{get_time()}===========')
 logger.info(f'====�˰汾Ϊ22��7��21�ո���==========')
 logger.info(f'==�Ż�:1������ȸ������绷������==')
 logger.info(f'======2���ж��˱���,��Ƶ,���⽱��С��20��Һ��������ٴ�������==')
 logger.info(f'==(�ָ�����,����ksjsbtaskΪyes,��ȵڶ����Զ��ָ�,�����did���ɻָ�ȫ������)==')
 logger.info(f'==(3,ÿ����1047��Ҽ��Ķ����ӵ���8�κ�10��,Ϊ0���Զ�����)==')
 logger.info(f'==(4,�����ֱ��,�޸�ǩ��,����1Ԫ�������׺ڲ������)==')
 logger.info(f'==================��ʼ���ck==================')
 initial_cks=get_ck()
 cookie_list=check_ck(initial_cks)
 logger.info(f'=============��ʼ��������������Ϣ===========')
 add_play=['']
 check_play=[]
 for web_ck_list in cookie_list:
  re_add=get_web_task('check_web_player',token,web_ck_list,change_value=False)
  add_play.append(re_add)
  re_check=get_web_task('check_web',token,web_ck_list,change_value=False)
  check_play.append(re_check)
 check_play=list(set(check_play))
 add_play=list(set(add_play))
 logger.info(add_play)
 logger.info(check_play)
 if 'token����' in add_play or 'token����' in check_play:
  sys.exit(0)
 logger.info(f'===========����:{len(initial_cks)}ck=============')
 token_num=go_web_requsetion("chaxun","Query_token")
 logger.info(f'========tokenʣ�����{token_num}=============')
 try:
  for web_ck_list in cookie_list:
   logger.info(f'===========�˺ţ�{web_ck_list[2]}����ʼ����============')
   logger.info(f'================���������ȴ�10-30��===================')
   if ksjsbtask=='yes':
    task_id_dict=get_web_task('go_all_task',token,web_ck_list,change_value=False)
    logger.info(f'===ǿ�ƿ�����������,����ر�,�Ա����˷Ѵ�������ֹ�ں�=====')
    logger.info(f'==�˺ţ�{web_ck_list[2]}�������б�:{list(task_id_dict.values())}=====')
   else:
    task_id_dict=get_web_task('go_task',token,web_ck_list,change_value=False)
    logger.info(f'==�˺ţ�{web_ck_list[2]}�������б�:{list(task_id_dict.values())}==')
   go_task_id(task_id_dict,web_ck_list)
  logger.info(f'=============================')
  check_ck(initial_cks)
  logger.info(f'=============================')
  token_num=go_web_requsetion("chaxun","Query_token")
  logger.info(f'==========tokenʣ�����{token_num}=======================')
  logger.info(f'=====================�ű�����==========================')
 except Exception as e:
  logger.info(e)
if __name__=="__main__":
 main()
