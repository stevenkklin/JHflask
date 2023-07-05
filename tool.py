import re
import cn2an

def data_process(message):
    statistics_dict={}
    message = cn2an.transform(message)
    # 去除空格、换行符和逗号
    message = message.replace(" ", "").replace("\n", "").replace(",", "").replace("，", "")


    # 使用正则表达式在数字和文字之间插入"-"
    output_string = re.sub(r'(\d+)', r'-\1-', message)

    # print(output_string)
    # 分割字符串成列表
    output_list = output_string.split("-")

    # 去除列表中的最后一个空字符串
    if output_list[-1] == '':
        output_list.pop()
    
    output_list = process_duplicate_key(output_list)


    # 对列表进行统计
    for i in range(0, len(output_list), 2):
        key = output_list[i]
        value = output_list[i+1]

        if key in statistics_dict:
            statistics_dict[key] += int(value)
        else:
            statistics_dict[key] = int(value)


    return statistics_dict

def process_duplicate_key(list):

    for index, value in enumerate(list):

        if value == '微':
            list[index] = "微信"

        if value == '数币激活' or value == '数币'  or value == '数活':
            list[index] = "数币活跃"

        if value == '手':
            list[index] = "手机银行"

        if value == '短':
            list[index] = "短信"   


    return list