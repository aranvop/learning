# 基础 
## 一.编写 helloworld  
$\qquad$使用echo 输出  
$\qquad$代码:
```
echo helloworld
```
$\qquad$输出结果:
```
hello world
```
## 二用type查看是否为内置命令
$\qquad$实例
```sh
type sl cat apt ls tldr man git cd
```
$\qquad$输出如下:
```
sl 是 /usr/games/sl
cat 是 /bin/cat
apt 是 /usr/bin/apt
ls 是“ls --color=auto”的别名
tldr 是 /usr/bin/tldr
man 是 /usr/bin/man
git 是 /usr/bin/git
cd 是 shell 内建
```
$\qquad$可以看出cd是shell内置的命令  
## 三变量
### 3.1变量:
$\qquad$变量定义与python相似,可直接定义  
$\qquad$使用变量需要在变量前加美元符号$  
$\qquad$删除变量:可以用unset删除变量
```sh
myname=qran
echo $myname
unset myname
echo $myname
```
$\qquad$输出如下:
```
qran

```
$\qquad$可以看出第二行为空白,这表明myname已经删除
## 3.2环境变量
$\qquad$ 3.2.1 环境变量的定义:环境变量（environment variables）一般是指在操作系统中用来指定操作系统运行环境的一些参数，如：临时文件夹位置和系统文件夹位置等。  
$\qquad\qquad$linux部分环境变量:`PATH HOSTNAME TERM SHELL HISTSIZE USER PS1`  
$\qquad\qquad$RANDOM变量为环境变量提供的随机数:  
$\qquad\qquad$使用RANDOM:`echo $RANDOM $RANDOM $RANDOM $RANDOM`  
$\qquad\qquad$输出结果:`18495 10433 21614 486`    
$\qquad$ 3.2.2 输出环境变量:     
$\qquad\qquad$使用echo输出部分环境变量`echo PATH HOSTNAME TERM SHELL HISTSIZE USER`    
$\qquad\qquad$可以用 `env` 命令可以输出全部环境变量  
$\qquad\qquad$也可以用 `set` 命令可以输出全部变量 (包括环境变量和自定义变量)  