from collections import OrderedDict

vocabular = OrderedDict()

vocabular['dict'] = '字典'
vocabular['array'] = '数组'
vocabular['list'] = '列表'
vocabular['docker'] = '集装箱'

for word,meaning in vocabular.items():
    print(word.title() + "'s meaning is " + meaning.title() + '.')