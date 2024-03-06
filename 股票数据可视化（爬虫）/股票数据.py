import requests
import jsonpath

import DBHeple

db = DBHeple.MyDBmySQL()
page = int(input("请输入爬取页数"))
for i in range(page):
    url = "https://stock.xueqiu.com/v5/stock/screener/quote/list.json?page={}&size=30&order=desc&orderby=percent&order_by=percent&market=CN&type=sh_sz".format(
        i + 1)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',
        'cookie': 'xq_a_token=bf4ca35131318f0118658f3f4790584a66d8bb83; xqat=bf4ca35131318f0118658f3f4790584a66d8bb83; xq_r_token=3374a327172eff6197f4933bdfe11278fc6234ee; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY4NTE0NzQzMywiY3RtIjoxNjgzNjEzOTM4ODMxLCJjaWQiOiJkOWQwbjRBWnVwIn0.IWCkBumLrr1997-y1txbFkNTTsu5w8iRqGOeGWJuviTWUDCRPYhrPoJnziyIYn0nS-CvWizxDGr3ox1QaWMBqzhb16xKixaRmbxIO-2tvHswcGq4TWfhByOaQs940PdeRoDc5amdeWa04dyOzaGp1LfEHhOI8aw39hNURw1SMNmQCH5YvFtVB_uYMEXjFGHdGsdE1HLnxjB1OxvN0e7TH4W4U-uaHPNngTs7uws5fvEJHDbTVqANiuroiW7wDRhTOvfxuZ42-7TMyQ77CH55NxtkdxC9QHYA8Fpfufqi1erYKuOsFWy1pm3OX-eZtM4LMwL4811Ha--oc5ozB_rjQA; u=211683613975567; Hm_lvt_1db88642e346389874251b5a1eded6e3=1683613978; device_id=1ecfd26edef9f127fc5580121ec15576; s=bl11qrgruk; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1683615694',
        'origin': 'https://xueqiu.com',
        'referer': 'https://xueqiu.com/hq'
    }
    json_data = requests.get(url=url, headers=headers).json()
    xueqiu_list = json_data['data']['list']
    for data in xueqiu_list:
        symbol = str(data['symbol'])
        name = data['name']
        current = data['current']
        chg = data['chg']
        percent = data['percent']
        if data['volume'] is None:
            volume = 0.0
        else:
            volume = data['volume']
        if data['amount'] is None:
            amount = 0.0
        else:
            amount = data['amount']
        if data['pe_ttm'] is None:
            pe_ttm = 0.0
        else:
            pe_ttm = data['pe_ttm']
        #         保存数据
        sql = "insert into tb_xueqiu(symbol,name,current,chg,percent,volume,amount,pe_ttm) values ('%s','%s','%s','%s','%s','%s','%s','%s')" % (
            symbol, name, current, chg, percent, volume, amount, pe_ttm)
        db.add(sql)
