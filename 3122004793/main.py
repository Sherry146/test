
import jieba
from collections import Counter
import math

#使用余弦相似度来计算文本相似度
# 分词并去除停用词
def tokenize(text):
    words = [word for word in jieba.cut(text) if word.strip()]
    return words

# 构建词袋模型
def build_bag_of_words(text):
    words = tokenize(text)
    word_counts = Counter(words)
    return word_counts

# 计算余弦相似度
def cosine_similarity(vector1, vector2):
    intersection = set(vector1.keys()) & set(vector2.keys())
    numerator = sum(vector1[x] * vector2[x] for x in intersection)

    sum1 = sum(vector1[x] ** 2 for x in vector1.keys())
    sum2 = sum(vector2[x] ** 2 for x in vector2.keys())
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def calculate_cosine_similarity(text1, text2):
    vector1 = build_bag_of_words(text1)
    vector2 = build_bag_of_words(text2)

    similarity = cosine_similarity(vector1, vector2)
    return similarity

#获取文件路径
file_name = input("请输入文件的绝对路径:")
file_sample = open(file="orig.txt",mode="r",encoding="utf-8")
file1 = open(file=file_name,mode="r",encoding="utf-8")

original = file_sample.read()
text1 = file1.read()

#计算相似度
similarity = calculate_cosine_similarity(original, text1)
similarity1 =round(similarity,4)
similarity1 *= 100

"""
print("文本1:", original)
print("文本2:", text1)
"""
#保存到文件 anser.txt
file_ans = open(file="anser.txt",mode="a",encoding="utf-8")
file_ans.write(str(file_name)+"相似度："+str(similarity1)+"%"+"\n")
print(file_name,"相似度：", similarity1,"%")

file_sample.close()
file1.close()
file_ans.close()

