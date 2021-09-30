# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys

sys.path.append('..')
from pytextclassifier import TextClassifier

if __name__ == '__main__':
    m = TextClassifier()
    data = [
        ('education', '名师指导托福语法技巧：名词的复数形式'),
        ('education', '中国高考成绩海外认可 是“狼来了”吗？'),
        ('sports', '图文：法网孟菲尔斯苦战进16强 孟菲尔斯怒吼'),
        ('sports', '四川丹棱举行全国长距登山挑战赛 近万人参与'),
        ('sports', '米兰客场8战不败国米10年连胜')
    ]
    m.train(data)

    r = m.predict(['福建春季公务员考试报名18日截止 2月6日考试',
                   '意甲首轮补赛交战记录:米兰客场8战不败国米10年连胜'])
    print(r)
    print(m)
    del m

    new_m = TextClassifier()
    new_m.load_model()
    predict_label, predict_proba = new_m.predict(['福建春季公务员考试报名18日截止 2月6日考试',
                                   '意甲首轮补赛交战记录:米兰客场8战不败国米10年连胜'])
    print(predict_label)  # ['education', 'sports']
    print(predict_proba)

    test_data = [
        ('education', '福建春季公务员考试报名18日截止 2月6日考试'),
        ('sports', '意甲首轮补赛交战记录:米兰客场8战不败国米10年连胜'),
    ]
    acc_score = new_m.evaluate(test_data)
    print(acc_score)  # 1.0
