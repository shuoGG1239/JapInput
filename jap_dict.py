import re

jp_dict = {}
hira_kake_dict = {}
kake_hira_dict = {}


def init_dict():
    with open('./tool/jp.data', 'rb') as f:
        text = f.read().decode('utf8')
    lines = text.splitlines()
    for line in lines:
        r = re.match(r'([^\s]+)\s+=\s+(\w+)', line.strip())
        jp_dict[r.group(2)] = r.group(1)
    with open('./tool/hira_kake.data', 'rb') as f:
        text = f.read().decode('utf8')
    lines = text.splitlines()
    for line in lines:
        hira_kake_dict[line[0]] = line[2]
        kake_hira_dict[line[2]] = line[0]


def isJP_word(char):
    """
    Unicode:
        中文：[\u4e00-\u9fa5]
        日文：[\u0800-\u4e00]
    """
    unicode_val = ord(char)
    return (unicode_val >= 0x0800 and unicode_val <= 0x4e00)
