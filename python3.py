{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 三、第三部分\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1.编码变换"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b'\\xce\\xd2\\xb0\\xae\\xb1\\xb1\\xbe\\xa9\\xcc\\xec\\xb0\\xb2\\xc3\\xc5'\n"
     ]
    }
   ],
   "source": [
    "# utf-8与gbk互相转化需要通过Unicode作为中介\n",
    "s=\"我爱北京天安门\"  # 默认编码为Unicode\n",
    "print(s.encode(\"gbk\")) # Unicode可直接转化为gbk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b'\\xe6\\x88\\x91\\xe7\\x88\\xb1\\xe5\\x8c\\x97\\xe4\\xba\\xac\\xe5\\xa4\\xa9\\xe5\\xae\\x89\\xe9\\x97\\xa8'\n"
     ]
    }
   ],
   "source": [
    "print(s.encode(\"utf-8\")) # Unicode可直接转化为utf-8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b'\\xce\\xd2\\xb0\\xae\\xb1\\xb1\\xbe\\xa9\\xcc\\xec\\xb0\\xb2\\xc3\\xc5'\n"
     ]
    }
   ],
   "source": [
    "print(s.encode(\"utf-8\").decode(\"utf-8\").encode(\"gb2312\"))\n",
    "# 此时s.encode(\"utf-8\")即转为utf-8了，然后转为gb2312，则需要先告诉Unicode你原先的编码是什么，即s.encode(\"utf-8\").decode(\"utf-8\"),再对其进行编码为gb2312，即最终为s.encode(\"utf-8\").decode(\"utf-8\").encode(\"gb2312\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2.文件"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "我是郎大鹏我爱中华\n"
     ]
    }
   ],
   "source": [
    "f=open('ly.txt','r',encoding='utf-8') # 文件句柄 'w'为创建文件，之前的数据就没了\n",
    "data=f.read()\n",
    "print(data)\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "f=open('test','a',encoding='utf-8') # 文件句柄 'a'为追加文件 append\n",
    "f.write(\"\\n阿斯达所，\\n天安门上太阳升\")\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "f = open('ly.txt', 'r', encoding='utf-8')  # 文件句柄"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000我爱中华\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "0\n",
      "\u0000\u0000\u0000\u0000\u0000\n",
      "5\n",
      "\u0000\u0000\u0000\u0000\u0000\n",
      "utf-8\n",
      "<_io.BufferedReader name='ly.txt'>\n",
      "5\n",
      "None\n",
      "##################################################\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\n",
      "\n",
      "\n",
      "\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000我爱中华\n"
     ]
    }
   ],
   "source": [
    "for i in range(5):\n",
    "    print(f.readline().strip())  # strip()去掉空格和回车\n",
    "\n",
    "for line in f.readlines():\n",
    "    print(line.strip())\n",
    "\n",
    "# 到第十行不打印\n",
    "\n",
    "for index, line in enumerate(f.readlines()):\n",
    "    if index == 9:\n",
    "        print('----我是分隔符-----')\n",
    "        continue\n",
    "    print(line.strip())\n",
    "# 到第十行不打印\n",
    "count = 0\n",
    "for line in f:\n",
    "\n",
    "    if count == 9:\n",
    "        print('----我是分隔符-----')\n",
    "        count += 1\n",
    "        continue\n",
    "    print(line.strip())\n",
    "    count += 1\n",
    "f = open('ly.txt', 'r', encoding='utf-8')  # 文件句柄\n",
    "print(f.tell())\n",
    "print(f.readline(5))\n",
    "print(f.tell())\n",
    "f.seek(0)\n",
    "print(f.readline(5))\n",
    "print(f.encoding)\n",
    "print(f.buffer)\n",
    "print(f.fileno())\n",
    "print(f.flush())  # 刷新缓冲区\n",
    "# 进度条\n",
    "import sys, time\n",
    "for i in range(50):\n",
    "    sys.stdout.write('#')\n",
    "    sys.stdout.flush()\n",
    "    time.sleep(0.5)\n",
    "f = open('ly.txt', 'a', encoding='utf-8')  # 文件句柄\n",
    "f.seek(10)\n",
    "f.truncate(20)  # 指定10到20个字符，10个字符前面留着，后面20字符清除\n",
    "f = open('ly.txt', 'r+', encoding='utf-8')  # 文件句柄\n",
    "print(f.readline().strip())\n",
    "print(f.readline().strip())\n",
    "print(f.readline().strip())\n",
    "f.write(\"我爱中华\")\n",
    "f.close()\n",
    "\n",
    "# 实现简单的shell sed替换功能\n",
    "\n",
    "f = open(\"ly.txt\", \"r\", encoding=\"utf-8\")\n",
    "f_new = open(\"ly2.txt\", \"w\", encoding=\"utf-8\")\n",
    "\n",
    "for line in f:\n",
    "    if \"肆意的快乐\" in line:\n",
    "        line = line.replace(\"肆意的快乐\", \"肆意的happy\")\n",
    "    f_new.write(line)\n",
    "\n",
    "f.close()\n",
    "f_new.close()\n",
    "\n",
    "import sys\n",
    "f = open(\"ly.txt\", \"r\", encoding=\"utf-8\")\n",
    "f_new = open(\"ly2.txt\", \"w\", encoding=\"utf-8\")\n",
    "find_str = sys.argv[1]\n",
    "replace_str = sys.argv[2]\n",
    "for line in f:\n",
    "    if find_str in line:\n",
    "        line = line.replace(find_str, replace_str)\n",
    "    f_new.write(line)\n",
    "f.close()\n",
    "f_new.close()\n",
    "\n",
    "# with语句---为了避免打开文件后忘记关闭，可以通过管理上下文\n",
    "with open('ly.txt', 'r', encoding='utf-8') as f:\n",
    "    for line in f:\n",
    "        print(line.strip())\n",
    "# python2.7后，with又支持同时对多个文件的上下文进行管理，即:\n",
    "with open('ly.txt', 'r', encoding='utf-8') as f1, open('ly2.txt',\n",
    "                                                       'r',\n",
    "                                                       encoding='utf-8'):\n",
    "    pass"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3.全局变量"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "inside func ['金角大王', 'Jack', 'Rain']\n",
      "['金角大王', 'Jack', 'Rain']\n"
     ]
    }
   ],
   "source": [
    "names = [\"Alex\", \"Jack\", \"Rain\"]\n",
    "\n",
    "\n",
    "# 除了整数和字符串在函数内不能改，列表，字典这些可以改\n",
    "def change_name():\n",
    "    names[0] = \"金角大王\"\n",
    "    print(\"inside func\", names)\n",
    "\n",
    "\n",
    "change_name()\n",
    "print(names)\n",
    "\n",
    "# 当全局变量与局部变量同名时，在定义局部变量的子程序内，局部变量起作用，在其它地方全局变量起作用。"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4.list操作"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "__author__=\"Alex Li\"\n",
    "names=\"zhang Gu Xiang Xu\"\n",
    "names=[\"zhang\",\"Gu\",\"Xiang\",\"Xu\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "zhang Gu Xiang\n"
     ]
    }
   ],
   "source": [
    "# 1.切片\n",
    "print(names[0],names[1],names[2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Gu', 'Xiang']\n"
     ]
    }
   ],
   "source": [
    "print(names[1:3])  # 顾头不顾尾，切片"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Xu\n"
     ]
    }
   ],
   "source": [
    "print(names[-1]) # 在不知道多长情况下，取最后一个位置"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "print(names[-1:-3]) # 切片是从左往右，此时不输出"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Gu', 'Xiang']\n"
     ]
    }
   ],
   "source": [
    "print(names[-3:-1]) # 顾头顾尾，取最后三个"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Xiang', 'Xu']\n"
     ]
    }
   ],
   "source": [
    "print(names[-2:])  # 取最后两个"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['zhang', 'Gu', 'Xiang']\n"
     ]
    }
   ],
   "source": [
    "print(names[0:3]) # 切片 等价于 print(names[:3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['zhang', 'Gu', 'Xiang', 'Xu', 'Lei']\n"
     ]
    }
   ],
   "source": [
    "# 2.追加\n",
    "names.append(\"Lei\")\n",
    "print(names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['zhang', 'Chen', 'Gu', 'Xiang', 'Xu', 'Lei']\n"
     ]
    }
   ],
   "source": [
    "# 3.指定位置插入\n",
    "names.insert(1,\"Chen\") # Gu前面插入\n",
    "print(names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['zhang', 'Chen', 'Xie', 'Xiang', 'Xu', 'Lei']\n"
     ]
    }
   ],
   "source": [
    "# 4.修改\n",
    "names[2]=\"Xie\"\n",
    "print(names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['zhang', 'Xie', 'Xiang', 'Xu', 'Lei']\n"
     ]
    }
   ],
   "source": [
    "# 5.删除\n",
    "# 第一种删除方法\n",
    "names.remove(\"Chen\")\n",
    "print(names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['zhang', 'Xiang', 'Xu', 'Lei']\n"
     ]
    }
   ],
   "source": [
    "# 第二种删除方法\n",
    "del names[1]\n",
    "print(names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['zhang', 'Xiang', 'Xu']\n"
     ]
    }
   ],
   "source": [
    "# 第三种删除方法\n",
    "names.pop() # 默认删除最后一个\n",
    "print(names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['zhang', 'Xu']\n"
     ]
    }
   ],
   "source": [
    "names.pop(1) #删除第二个元素\n",
    "print(names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "print(names.index(\"Xu\")) # 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Xu\n"
     ]
    }
   ],
   "source": [
    "print(names[names.index(\"Xu\")]) #打印出找出的元素值3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "# 6.统计\n",
    "names.append(\"zhang\") #再加一个用于学习统计\"zhang\"的个数\n",
    "print(names.count(\"zhang\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Xu', 'zhang', 'zhang']\n"
     ]
    }
   ],
   "source": [
    "# 7.排序\n",
    "names.sort() #按照ASCII码排序\n",
    "print(names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['zhang', 'zhang', 'Xu']\n"
     ]
    }
   ],
   "source": [
    "names.reverse() # 逆序\n",
    "print(names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['zhang', 'zhang', 'Xu', 1, 2, 3, 4] [1, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "# 8.合并\n",
    "names2=[1,2,3,4]\n",
    "names.extend(names2)\n",
    "print(names,names2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "# 9.删掉names2\n",
    "'''del names2'''\n",
    "print(names2) # NameError: name 'names2' is not defined,表示已删除"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['zhang', 'zhang', 'Xu', 1, 2, 3, 4] ['zhang', 'zhang', 'Xu', 1, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "# 10.浅copy\n",
    "names2=names.copy()\n",
    "print(names,names2) # 此时names2与names指向相同"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['zhang', 'zhang', '大张', 1, 2, 3, 4] ['zhang', 'zhang', 'Xu', 1, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "names[2]=\"大张\"\n",
    "print(names,names2) # 此时names改变，names2不变"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, ['zhang', 'Gu'], 5]\n"
     ]
    }
   ],
   "source": [
    "# 11.浅copy在列表嵌套应用\n",
    "names=[1,2,3,4,[\"zhang\",\"Gu\"],5]\n",
    "print(names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, '斯', ['张改', 'Gu'], 5] [1, 2, 3, 4, ['张改', 'Gu'], 5]\n"
     ]
    }
   ],
   "source": [
    "names2=names.copy()\n",
    "names[3]=\"斯\"\n",
    "names[4][0]=\"张改\"\n",
    "print(names,names2) # copy为浅copy,第一层copy不变，后面的嵌套全部都变,修改names2与names都一样\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, '斯', ['张改', 'Gu'], 5] [1, 2, 3, 4, ['zhang', 'Gu'], 5]\n"
     ]
    }
   ],
   "source": [
    "# 12.完整克隆\n",
    "import copy\n",
    "# 浅copy与深copy\n",
    "'''浅copy与深copy区别就是浅copy只copy一层，而深copy就是完全克隆'''\n",
    "names = [1, 2, 3, 4, [\"zhang\", \"Gu\"], 5]\n",
    "# names2=copy.copy(names) # 这个跟列表的浅copy一样\n",
    "names2 = copy.deepcopy(names)  #深copy\n",
    "names[3] = \"斯\"\n",
    "names[4][0] = \"张改\"\n",
    "print(names, names2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "斯\n",
      "['张改', 'Gu']\n",
      "5\n",
      "[1, 3, ['张改', 'Gu']]\n"
     ]
    }
   ],
   "source": [
    "# 13.列表循环\n",
    "for i in names:\n",
    "    print(i)\n",
    "print(names[0:-1:2]) # 步长为2进行切片"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5.Tuple操作"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "names=('alex','jack','alex')\n",
    "\n",
    "print(names.count('alex'))\n",
    "print(names.index('jack'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input your salary:8000\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n",
      "选择要买嘛？>>:\n",
      "invalid option\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n",
      "选择要买嘛？>>:1\n",
      "\u001b[41;1m你的余额只剩[8000]啦，还买个毛线\u001b[0m\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n",
      "选择要买嘛？>>:0\n",
      "Added ('Iphone', 5800) into shopping cart, your current balance is \u001b[31;1m2200\u001b[0m\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n",
      "选择要买嘛？>>:6\n",
      "product code[6] is not exist!\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n",
      "选择要买嘛？>>:q\n",
      "-----------shopping list----------------\n",
      "('Iphone', 5800)\n",
      "Your current balance: 2200\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n",
      "选择要买嘛？>>:p\n",
      "invalid option\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n",
      "选择要买嘛？>>:no\n",
      "invalid option\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n",
      "选择要买嘛？>>:4\n",
      "Added ('Coffee', 31) into shopping cart, your current balance is \u001b[31;1m2169\u001b[0m\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n",
      "选择要买嘛？>>:4\n",
      "Added ('Coffee', 31) into shopping cart, your current balance is \u001b[31;1m2138\u001b[0m\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n",
      "选择要买嘛？>>:4\n",
      "Added ('Coffee', 31) into shopping cart, your current balance is \u001b[31;1m2107\u001b[0m\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n",
      "选择要买嘛？>>:43\n",
      "product code[43] is not exist!\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n",
      "选择要买嘛？>>:2\n",
      "\u001b[41;1m你的余额只剩[2107]啦，还买个毛线\u001b[0m\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n",
      "选择要买嘛？>>:1\n",
      "\u001b[41;1m你的余额只剩[2107]啦，还买个毛线\u001b[0m\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n",
      "选择要买嘛？>>:2\n",
      "\u001b[41;1m你的余额只剩[2107]啦，还买个毛线\u001b[0m\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n",
      "选择要买嘛？>>:3\n",
      "\u001b[41;1m你的余额只剩[2107]啦，还买个毛线\u001b[0m\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n",
      "选择要买嘛？>>:4\n",
      "Added ('Coffee', 31) into shopping cart, your current balance is \u001b[31;1m2076\u001b[0m\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n",
      "选择要买嘛？>>:5\n",
      "Added ('Alex Python', 120) into shopping cart, your current balance is \u001b[31;1m1956\u001b[0m\n",
      "0 ('Iphone', 5800)\n",
      "1 ('Mac Pro', 9800)\n",
      "2 ('Bike', 5800)\n",
      "3 ('Watch', 10600)\n",
      "4 ('Coffee', 31)\n",
      "5 ('Alex Python', 120)\n"
     ]
    }
   ],
   "source": [
    "# 购物篮程序\n",
    "\n",
    "product_list = [\n",
    "    ('Iphone', 5800),\n",
    "    ('Mac Pro', 9800),\n",
    "    ('Bike', 5800),\n",
    "    ('Watch', 10600),\n",
    "    ('Coffee', 31),\n",
    "    ('Alex Python', 120),\n",
    "]\n",
    "shopping_list = []\n",
    "salary = input(\"Input your salary:\")\n",
    "\n",
    "if salary.isdigit():\n",
    "    salary = int(salary)\n",
    "    while True:\n",
    "        '''for item in product_list:\n",
    "            print(product_list.index(item),item)\n",
    "        '''\n",
    "        for index, item in enumerate(product_list):\n",
    "            print(index, item)\n",
    "        user_choice = input(\"选择要买嘛？>>:\")\n",
    "        if user_choice.isdigit():\n",
    "            user_choice = int(user_choice)\n",
    "            if user_choice < len(product_list) and user_choice >= 0:\n",
    "                p_item = product_list[user_choice]\n",
    "                if p_item[1] <= salary:\n",
    "                    shopping_list.append(p_item)\n",
    "                    salary -= p_item[1]\n",
    "                    print(\n",
    "                        \"Added %s into shopping cart, your current balance is \\033[31;1m%s\\033[0m\"\n",
    "                        % (p_item, salary))\n",
    "                else:\n",
    "                    print(\"\\033[41;1m你的余额只剩[%s]啦，还买个毛线\\033[0m\" % salary)\n",
    "            else:\n",
    "                print(\"product code[%s] is not exist!\" % user_choice)\n",
    "        elif user_choice == 'q':\n",
    "            print('-----------shopping list----------------')\n",
    "            for p in shopping_list:\n",
    "                print(p)\n",
    "                print(\"Your current balance:\", salary)\n",
    "            exit()\n",
    "        else:\n",
    "            print(\"invalid option\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6.Set操作"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 3, 4, 5, 6, 7, 9} <class 'set'>\n"
     ]
    }
   ],
   "source": [
    "# 集合set  集合关系测试\n",
    "list_1=[1,4,5,7,3,6,7,9]\n",
    "list_1=set(list_1)\n",
    "print(list_1,type(list_1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0, 2, 4, 6, 8, 22} <class 'set'>\n"
     ]
    }
   ],
   "source": [
    "list_2=set([2,6,0,6,22,8,4])\n",
    "print(list_2,type(list_2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--------------------------------\n",
      "方法一\n",
      "{4, 6}\n"
     ]
    }
   ],
   "source": [
    "print(\"--------------------------------\")\n",
    "# 取交集\n",
    "print(\"方法一\")\n",
    "print(list_1.intersection(list_2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "方法二\n",
      "{4, 6}\n",
      "--------------------------------\n"
     ]
    }
   ],
   "source": [
    "print(\"方法二\")\n",
    "print(list_1&list_2)\n",
    "print(\"--------------------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "方法一\n",
      "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 22}\n"
     ]
    }
   ],
   "source": [
    "# 取并集\n",
    "print(\"方法一\")\n",
    "print(list_1.union(list_2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "方法二\n",
      "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 22}\n",
      "--------------------------------\n"
     ]
    }
   ],
   "source": [
    "print(\"方法二\")\n",
    "print(list_1|list_2)\n",
    "print(\"--------------------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 3, 5, 7, 9}\n",
      "{1, 3, 5, 7, 9}\n",
      "--------------------------------\n"
     ]
    }
   ],
   "source": [
    "# 差集 in list_1 but not in list_2\n",
    "print(list_1.difference(list_2))\n",
    "print(list_1-list_2)\n",
    "print(\"--------------------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "# 子集\n",
    "list_3=[1,4,6]\n",
    "list_4=[1,4,6,7]\n",
    "list_3=set(list_3)\n",
    "list_4=set(list_4)\n",
    "print(list_3.issubset(list_4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "--------------------------------\n"
     ]
    }
   ],
   "source": [
    "print(list_4.issuperset(list_3))\n",
    "print(\"--------------------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0, 1, 2, 3, 5, 7, 8, 9, 22}\n",
      "{0, 1, 2, 3, 5, 7, 8, 9, 22}\n",
      "--------------------------------\n"
     ]
    }
   ],
   "source": [
    "# 对称差集 把list_1与list_2互相都没有的元素放在一块，其实就是去掉重复元素\n",
    "print(list_1.symmetric_difference(list_2))\n",
    "print(list_1^list_2)\n",
    "print(\"--------------------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "--------------------------------\n"
     ]
    }
   ],
   "source": [
    "# 是否没有交集 Return True if two sets have a null intersection.\n",
    "list_5=set([1,2,3,4])\n",
    "list_6=set([5,6,7])\n",
    "print(list_5.isdisjoint(list_6))\n",
    "print(\"--------------------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 3, 4, 5, 6, 7, 'x', 9}\n"
     ]
    }
   ],
   "source": [
    "# 基本操作\n",
    "# 添加一项\n",
    "list_1.add('x')\n",
    "print(list_1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 3, 4, 5, 6, 7, 'x', 9, 10, 37, 42}\n"
     ]
    }
   ],
   "source": [
    "# 添加多项\n",
    "list_1.update([10,37,42])\n",
    "print(list_1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 3, 4, 5, 6, 7, 'x', 9, 37, 42}\n"
     ]
    }
   ],
   "source": [
    "# 删除一项\n",
    "list_1.remove(10)\n",
    "print(list_1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n"
     ]
    }
   ],
   "source": [
    "# set长度\n",
    "print(len(list_1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "# 测试9是否是list_1的成员\n",
    "print(9 in list_1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "# pop()删除并且返回一个任意的元素\n",
    "print(list_1.pop())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{3, 4, 5, 6, 7, 9, 37, 42}\n"
     ]
    }
   ],
   "source": [
    "# 删除一个指定的值\n",
    "list_1.discard('x')\n",
    "print(list_1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 7.字符串操作"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Alex\n"
     ]
    }
   ],
   "source": [
    "name=\"alex\"\n",
    "print(name.capitalize()) # 首字母大写"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "print(name.count(\"a\")) # 统计字母个数"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-----------------------alex-----------------------\n"
     ]
    }
   ],
   "source": [
    "print(name.center(50,\"-\")) #总共打印50个字符，并把nam放在中间，不够的用-补上"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print(name.endswith(\"ex\")) # 判断字符串以什么结尾"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "alex                          name is alex\n"
     ]
    }
   ],
   "source": [
    "name=\"alex \\tname is alex\"\n",
    "print(name.expandtabs(tabsize=30)) # 将name中\\t转为30个空格"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "print(name.find(\"x\")) # 取索引"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x \tname is alex\n"
     ]
    }
   ],
   "source": [
    "print(name[name.find(\"x\"):]) # 字符串切片"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my \tname is alex and i am 23 old\n"
     ]
    }
   ],
   "source": [
    "name=\"my \\tname is {name} and i am {year} old\"\n",
    "print(name.format(name=\"alex\",year=23))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my \tname is alex and i am 23 old\n"
     ]
    }
   ],
   "source": [
    "print(name.format_map({'name':'alex','year':23}))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print('ab123'.isalnum()) #isalnum()包含所有字母及数字，如果不是这两个，则为False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print('ab123'.isalpha()) # False  isalpha()包含纯英文字符"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print('1A'.isdecimal()) # 是否是十进制 False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print('1A'.isdigit()) # 是否是整数 False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print('_'.isidentifier()) #判断是否是合法的标识符，实质是否为合法变量名 True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print('aasd'.islower()) # 判断是否是小写 True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print(''.isspace()) # 是否是空格 False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print('My name is'.istitle()) # 字符串首字母大写为title，否则不是"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1+2+3\n"
     ]
    }
   ],
   "source": [
    "print('+'.join(['1','2','3'])) # 对一列表中所有元素进行join操作"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my \tname is {name} and i am {year} old************\n"
     ]
    }
   ],
   "source": [
    "print(name.ljust(50,'*')) # 左对齐字符串，多余位用*补全"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "------------my \tname is {name} and i am {year} old\n"
     ]
    }
   ],
   "source": [
    "print(name.rjust(50,'-')) # 右对齐字符串，多余位用*-补全"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Alex\n"
     ]
    }
   ],
   "source": [
    "print('\\n Alex'.lstrip()) # 去掉左边的空格/回车"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Alex\n"
     ]
    }
   ],
   "source": [
    "print('\\nAlex\\n'.rstrip()) # 去掉右边的空格/回车"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Alex\n"
     ]
    }
   ],
   "source": [
    "print('\\nAlex\\n'.strip()) # 去掉左边和右边的空格/回车"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Alex\n"
     ]
    }
   ],
   "source": [
    "print('Alex')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1l5x li\n"
     ]
    }
   ],
   "source": [
    "p=str.maketrans(\"abcdef\",\"123456\")\n",
    "print(\"alex li\".translate(p))  #把alex li换成上一行对应的值"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "aLex li\n"
     ]
    }
   ],
   "source": [
    "print(\"alex li\".replace('l','L',1)) # 替换 1表示替换几个l,从左到右计算替换个数"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "print(\"alex li\".rfind('l')) # 找到的最右边的下标返回"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'ex ', 'i']\n"
     ]
    }
   ],
   "source": [
    "print(\"alex li\".split('l')) \n",
    "# 默认将字符串按照空格分隔成列表，也可以在()中填写相应的分隔符，比如以字符l分隔，print(\"alex li\".split(‘l’)),而且分隔符在列表中不会出现"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['1', '2', '3', '4']\n"
     ]
    }
   ],
   "source": [
    "print(\"1+2+3+4\".split('+')) # ['1', '2', '3', '4']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['1+2', '+3+4']\n"
     ]
    }
   ],
   "source": [
    "print(\"1+2\\n+3+4\".splitlines()) # ['1+2', '+3+4']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "aLEX lI\n"
     ]
    }
   ],
   "source": [
    "print(\"Alex Li\".swapcase()) # aLEX lI"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lex Li\n"
     ]
    }
   ],
   "source": [
    "print('lex li'.title()) # Lex Li"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "00000000000000000000000000000000000000000000lex li\n",
      "---\n"
     ]
    }
   ],
   "source": [
    "print('lex li'.zfill(50)) #不够以0填充\n",
    "print('---')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 8.字典"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'stu1101': 'tengxun', 'stu1102': 'baidu', 'stu1103': 'ali'}\n"
     ]
    }
   ],
   "source": [
    "# 字典无序\n",
    "info={\n",
    "    'stu1101':\"tengxun\",\n",
    "    'stu1102':\"baidu\",\n",
    "    'stu1103':\"ali\",\n",
    "}\n",
    "\n",
    "print(info)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tengxun\n"
     ]
    }
   ],
   "source": [
    "# 0.查找\n",
    "# 方法一:确定存在\n",
    "print(info[\"stu1101\"]) # 查找若不在，则报错"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "print(info.get(\"stu11004\")) # 查找不在不会报错，直接返回None，若有直接返回"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print('stu1103' in info) # True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'stu1101': '腾讯', 'stu1102': 'baidu', 'stu1103': 'ali'}\n"
     ]
    }
   ],
   "source": [
    "# 1.修改\n",
    "info[\"stu1101\"]=\"腾讯\"\n",
    "print(info)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'stu1101': '腾讯', 'stu1102': 'baidu', 'stu1103': 'ali', 'stu1104': 'zhubajie'}\n"
     ]
    }
   ],
   "source": [
    "# 2.增加\n",
    "info[\"stu1104\"]=\"zhubajie\"\n",
    "print(info)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'stu1102': 'baidu', 'stu1103': 'ali', 'stu1104': 'zhubajie'}\n"
     ]
    }
   ],
   "source": [
    "# 3.删除\n",
    "# 方法一\n",
    "del info[\"stu1101\"]\n",
    "print(info)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'stu1103': 'ali', 'stu1104': 'zhubajie'}\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'\\n# 随机删除\\ninfo.popitem()\\nprint(info)\\n'"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 方法二\n",
    "info.pop(\"stu1102\")\n",
    "print(info)\n",
    "'''\n",
    "# 随机删除\n",
    "info.popitem()\n",
    "print(info)\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'stu1103': 'ali', 'stu1104': 'zhubajie', 'stu1101': 'Alex', 1: 3, 2: 5}\n"
     ]
    }
   ],
   "source": [
    "# 4.多级字典嵌套及操作\n",
    "av_catalog = {\n",
    "    \"A\":{\n",
    "        \"www.yo333.com\": [\"aaa\",\"111\"],\n",
    "        \"www.po333.com\": [\"bbb\",\"222\"],\n",
    "        \"333you.com\": [\"ccc\",\"333\"],\n",
    "        \"333art.com\":[\"ddd\",\"444\"]\n",
    "    },\n",
    "    \"B\":{\n",
    "        \"tokyo-lot\":[\"eee\",\"555\"]\n",
    "    },\n",
    "    \"C\":{\n",
    "        \"1022\":[\"fff\",\"666\"]\n",
    "    }\n",
    "}\n",
    "b={\n",
    "    'stu1101':\"Alex\",\n",
    "    1:3,\n",
    "    2:5\n",
    "}\n",
    "info.update(b) #将两个字典合并，存在key,则更新value，不存在key，则合并\n",
    "print(info)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_items([('stu1103', 'ali'), ('stu1104', 'zhubajie'), ('stu1101', 'Alex'), (1, 3), (2, 5)])\n"
     ]
    }
   ],
   "source": [
    "print(info.items()) #把一个字典转成列表"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{6: 'test', 7: 'test', 8: 'test'}\n"
     ]
    }
   ],
   "source": [
    "c=info.fromkeys([6,7,8],\"test\")\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{6: [1, {'name': 'alex'}, 444], 7: [1, {'name': 'alex'}, 444], 8: [1, {'name': 'alex'}, 444]}\n"
     ]
    }
   ],
   "source": [
    "c=info.fromkeys([6,7,8],[1,{'name':'alex'},444])\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{6: [1, {'name': 'Jack Chen'}, 444], 7: [1, {'name': 'Jack Chen'}, 444], 8: [1, {'name': 'Jack Chen'}, 444]}\n"
     ]
    }
   ],
   "source": [
    "c[7][1]['name']='Jack Chen' # 3个key共用一个value,修改一个则所有的都修改了\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--------\n",
      "{'A': {'www.yo333.com': ['aaa', '111'], 'www.po333.com': ['bbb', '222'], '333you.com': ['ccc', '可以在国内做镜像'], '333art.com': ['ddd', '444']}, 'B': {'tokyo-lot': ['eee', '555']}, 'C': {'1022': ['fff', '666']}, 'taiwan': {'www.baidu.com': [1, 2]}}\n"
     ]
    }
   ],
   "source": [
    "print(\"--------\")\n",
    "av_catalog[\"A\"][\"333you.com\"][1]=\"可以在国内做镜像\" # 二级字典替换\n",
    "av_catalog.setdefault(\"taiwan\",{\"www.baidu.com\":[1,2]}) # 如果不重名，即创建一个新的值，如果重名，将找到的值返回\n",
    "print(av_catalog)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys(['stu1103', 'stu1104', 'stu1101', 1, 2])\n"
     ]
    }
   ],
   "source": [
    "print(info.keys()) # 打印出所有的key"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_values(['ali', 'zhubajie', 'Alex', 3, 5])\n"
     ]
    }
   ],
   "source": [
    "print(info.values()) # 打印出所有的value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "---------------\n",
      "stu1103 ali\n",
      "stu1104 zhubajie\n",
      "stu1101 Alex\n",
      "1 3\n",
      "2 5\n",
      "---------------\n"
     ]
    }
   ],
   "source": [
    "print(\"---------------\")\n",
    "for i in info:\n",
    "    print(i,info[i])  #效率更高点\n",
    "print(\"---------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "stu1103 ali\n",
      "stu1104 zhubajie\n",
      "stu1101 Alex\n",
      "1 3\n",
      "2 5\n"
     ]
    }
   ],
   "source": [
    "for k,v in info.items():\n",
    "    print(k,v)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 9.函数"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "in the fun1\n",
      "in the fun2\n",
      "1\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "# 1.无参函数\n",
    "# 定义一个函数\n",
    "def fun1():\n",
    "    '''testing'''\n",
    "    print('in the fun1')\n",
    "    return 1\n",
    "\n",
    "# 定义一个过程 实质就是无返回值的函数\n",
    "def fun2():\n",
    "    '''testing2'''\n",
    "    print('in the fun2')\n",
    "\n",
    "x=fun1()\n",
    "y=fun2()\n",
    "print(x)\n",
    "print(y)  # 没有返回值得情况下，python隐式地返回一个None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "in the test1\n",
      "in the test2\n",
      "in the test3\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "def logger():\n",
    "    time_format='%Y-%m-%d %X %A %B %p %I'\n",
    "    time_current=time.strftime(time_format)\n",
    "    with open('a.txt','a+')as f:\n",
    "        f.write('time %s end action\\n'%time_current)\n",
    "def test1():\n",
    "    print('in the test1')\n",
    "    logger()\n",
    "\n",
    "\n",
    "def test2():\n",
    "    print('in the test2')\n",
    "    logger()\n",
    "    return 0\n",
    "\n",
    "def test3():\n",
    "    print('in the test3')\n",
    "    logger()\n",
    "    return 1,{5:\"sda\",6:\"zad\"},[1,2,3]\n",
    "\n",
    "x=test1()\n",
    "y=test2()\n",
    "z=test3()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n",
      "0\n",
      "(1, {5: 'sda', 6: 'zad'}, [1, 2, 3])\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'\\n总结：\\n    返回值数=0:返回None\\n    返回值数=1:返回object\\n    返回值数>1:返回tuple\\n'"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(x) # None\n",
    "print(y) # 0\n",
    "print(z) # (1, {5: 'sda', 6: 'zad'}, [1, 2, 3])\n",
    "\n",
    "\n",
    "'''\n",
    "总结：\n",
    "    返回值数=0:返回None\n",
    "    返回值数=1:返回object\n",
    "    返回值数>1:返回tuple\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "2\n",
      "1\n",
      "3\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "# 2.有参函数\n",
    "# 默认参数特点：调用函数的时候，默认参数非必须传递\n",
    "# 用途：1.默认安装值\n",
    "\n",
    "def test(x,y):\n",
    "    print(x)\n",
    "    print(y)\n",
    "\n",
    "test(1,2)     # 位置参数调用 与形参意义对应\n",
    "test(y=1,x=2) # 关键字调用，与形参顺序无关\n",
    "test(3,y=2) # 如果既有关键字调用又有位置参数，前面一个一定是位置参数，一句话：关键参数一定不能写在位置参数前面\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "比如加入一个参数z\n",
    "'''\n",
    "def test1(x,y,z):\n",
    "    print(x)\n",
    "    print(y)\n",
    "    print(z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "4\n",
      "6\n",
      "3\n",
      "4\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "# 关键参数一定不能放在位置参数前面\n",
    "test1(3,4,z=6)\n",
    "test1(3,z=6,y=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "# 默认参数,\n",
    "def test(x,y,z=2):\n",
    "    print(x)\n",
    "    print(y)\n",
    "    print(z)\n",
    "\n",
    "test(1,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 3, 4, 5, 5, 6)\n",
      "(1, 3, 4, 5, 5, 6)\n",
      "1\n",
      "(2, 3, 4, 5, 6, 7)\n"
     ]
    }
   ],
   "source": [
    "# 用*args传递多个参数，转换成元组的方式 *表示一个功能代号，表示接受的参数不固定，args可以随意起名\n",
    "def test(*args):\n",
    "    print(args)\n",
    "test(1,3,4,5,5,6)\n",
    "test(*[1,3,4,5,5,6]) # args=tuple([1,2,3,4,5])\n",
    "def test(x,*args):\n",
    "    print(x)\n",
    "    print(args)\n",
    "test(1,2,3,4,5,6,7) # 1 (2,3,4,5,6,7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'alex', 'age': 8, 'id': 10, 'sex': 'M'}\n",
      "alex 8 10 M\n"
     ]
    }
   ],
   "source": [
    "# 字典传值 **kwagrs:把N个关键字参数，转换成字典的方式\n",
    "def test(**kwargs):\n",
    "    print(kwargs)\n",
    "    print(kwargs['name'],kwargs['age'],kwargs['id'],kwargs['sex'])\n",
    "\n",
    "test(name='alex',age=8,id=10,sex='M') # {'name': 'alex', 'age': 8, 'id': 10, 'sex': 'M'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'alex', 'age': 8, 'id': 10, 'sex': 'M'}\n",
      "alex 8 10 M\n"
     ]
    }
   ],
   "source": [
    "test(**{'name':'alex','age':8,'id':10,'sex':'M'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "alex\n",
      "{'age': 18, 'sex': 'M'}\n"
     ]
    }
   ],
   "source": [
    "def test(name,**kwargs):\n",
    "    print(name)\n",
    "    print(kwargs)\n",
    "test('alex',age=18,sex='M') # 字典 {'age': 18, 'sex': 'M'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "alex\n",
      "3\n",
      "{'sex': 'M', 'hobby': 'tesla'}\n"
     ]
    }
   ],
   "source": [
    "# 默认参数得放在参数组前面\n",
    "def test(name,age=18,**kwargs):\n",
    "    print(name)\n",
    "    print(age)\n",
    "    print(kwargs)\n",
    "\n",
    "test('alex',sex='M',hobby='tesla',age=3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "alex\n",
      "3\n",
      "{'sex': 'M', 'hobby': 'tesla'}\n"
     ]
    }
   ],
   "source": [
    "test('alex',3,sex='M',hobby='tesla')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "alex\n",
      "18\n",
      "{}\n"
     ]
    }
   ],
   "source": [
    "test('alex') # 后面的**kwargs不赋值输出为空字典"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "alex\n",
      "34\n",
      "()\n",
      "{'sex': 'M', 'hobby': 'tesla'}\n"
     ]
    }
   ],
   "source": [
    "def test(name,age=18,*args,**kwargs):\n",
    "    print(name)\n",
    "    print(age)\n",
    "    print(args)\n",
    "    print(kwargs)\n",
    "test('alex',age=34,sex='M',hobby='tesla') # alex 34 () {'sex': 'M', 'hobby': 'tesla'}\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 10.高阶函数"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "# 高阶函数 变量可以指向函数，函数的参数能接受变量，那么一个函数就可以接受另一个函数作为参数，这个函数就叫做高阶函数\n",
    "def f(x):\n",
    "    return x\n",
    "def add(x,y,f):\n",
    "    return f(x)+f(y)\n",
    "res=add(1,2,f)\n",
    "print(res)  # 3"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
