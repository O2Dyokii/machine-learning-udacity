用Python 统计高频字数

用 Python 统计字数
问题
用 Python 实现函数 count_words()，该函数输入字符串 s 和数字 n，返回 s 中 n 个出现频率最高的单词。返回值是一个元组列表，包含出现次数最高的 n 个单词及其次数,即 [(<单词1>, <次数1>), (<单词2>, <次数2>), ... ]，按出现次数降序排列。

您可以假设所有输入都是小写形式，并且不含标点符号或其他字符（只包含字母和单个空格）。如果出现次数相同，则按字母顺序排列。

例如：

print count_words("betty bought a bit of butter but the butter was bitter",3)
输出：

[('butter', 2), ('a', 1), ('betty', 1)]
