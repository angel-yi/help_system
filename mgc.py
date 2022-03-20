# coding: utf-8

import jieba

jieba.lcut_for_search('哈哈哈')


def mgc_jc(message):
    with open('keywords.txt', 'r', encoding='utf-8') as fp:
        mgc_list = fp.readlines()
    mgc_list = [i.replace('\n', '') for i in mgc_list]

    b = jieba.lcut_for_search(message)
    print(b)
    test_re = []
    for i in b:
        if i in mgc_list:
            print('检测到铭感词')
            print('find', i)
            test_re.append(i)
    for i in test_re:
        message = message.replace(i, '*')
    print(message)
    return message


mgc_jc('我想获取你的联系方式')
