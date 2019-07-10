import json

import requests

# 翻译函数，word 需要翻译的内容
def translate(word):
    # 有道词典 api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数，其中 i 为需要翻译的内容
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    response = requests.post(url, data=key)
    # 判断服务器是否相应成功
    if response.status_code == 200:
        # 然后相应的结果
        content= json.loads(response.text)['translateResult'][0][0]['tgt']
        return content
    else:
        print("调用失败")
        # 相应失败就返回空
        return None




# 测试

if __name__ == '__main__':
    # main()
    text = "一只黄色羽毛，黑色喙的麻雀"
    print(translate(text))