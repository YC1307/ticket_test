import json
import re


def json2data():
    file = open('./json/ticket.json', 'r+', encoding="utf-8")

    datas = json.load(file)

    dicts = datas['data']
    l_list = []
    for i in dicts:
        if i == "result":
            lists = dicts[i]
            for li in lists:
                li_real = re.search("无\|无\|无", li)
                if li_real:
                    print("票已售罄")
                    continue
                else:
                    li_one = li.split("|")
                    # print(li_one)
                    # le = len(li_one)
                    print(li_one[3], li_one[8], li_one[9], li_one[10], )
                    l_list.append(li_one)
            # print(l_list)
            return l_list


def data_hadle():
    l_list = json2data()
    # print(l_list)


# json2data()

data_hadle()
