import jieba
import wordcloud

f = open("journalism.txt", 'r', encoding='utf-8')
txt = f.read()
f.close()
words = jieba.lcut(txt)
counts = {}

for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0)+1

items = list(counts.items())    # 将字典转为列表
items.sort(key=lambda x: x[1], reverse=True)  # 排序
word2 = []

for i in range(len(items)-1):
    word, count = items[i]
#    print("{0:<10}{1:>5}".format(word,count))
    word2.append(word)
newWord = ' '.join(word2)    # 格拼接
wd = wordcloud.WordCloud(font_path='msyh.ttc').generate(newWord)
wd.to_file('结果图片.png')
