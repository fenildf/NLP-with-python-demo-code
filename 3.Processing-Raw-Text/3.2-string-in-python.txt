
Sorry this part I write in Chinese. ><
这一节主要是基础知识，就分享一下我的笔记吧。


单引号：
包裹在双引号中，circus = “Monty Python’s Flying Circus"
使用\转义 circus = ‘Monty Python\’s Flying Circus'

跨行写字符串：
使用\表示字符串没有写完： str = “this is not”\
                                                                 “finished."
     2. 使用括号包裹： str = (“this is not"
                                                 “finished.” )

保留换行：
     将字符串写在三引号中，’’’ XXXXXXX’’’ 或者”””XXXXXXX”””  （相当于 web 中的 pre，会保留换行）

访问子字符串
     切片 [m:n] 包含的是从 m到 n-1 的字符串，包含头不包含尾。

list和字符串的差异：
     他们是不同的，不能不加操作的就连在一起。
     list是分词之后得到的结果，更方便处理。（因为可以很方便地组合成句子）一般来说处理 str 的第一件事就是分词成 list，而写入文件的时候，就要转换成字符串进行相应的操作。
     其中，字符串一旦创建不可更改，比如 tmp=“hello”;tmp[0]=’s’;是错误的，但是分词可以更改。（我猜，python 的字符串也是用指针指向字符串池来操作的吧！
