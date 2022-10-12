# 正则
## $\qquad$ 1. 符号^
$\qquad\qquad$ 正则`^`,如`^sudo`  
$\qquad\qquad$匹配所有以sudo开头的行.
$\qquad\qquad$实例:
```
cat ./.bash_history |grep ^sudo
```
$\qquad\qquad$输出所有以sudo为开头的行  
## $\qquad$ 2. 符号$
$\qquad\qquad$ 正则`$`,如`update$` 
```
cat ./.bash_history |grep false$
```
$\qquad\qquad$输出所有以false为结尾的一行
## $\qquad$ 3. 符号: '.'
$\qquad\qquad$ 正则`.`符号,如`su.o` 
```
history |grep su.o
history |grep .
```
$\qquad\qquad$`.`匹配任意一个字符  
$\qquad\qquad$第二个命令会输出所有历史记录
## $\qquad$ 4. 符号: '*'
$\qquad\qquad$ 正则`*`符号,如`.*` 
$\qquad\qquad$ 实例:
```
history |grep .*
history |grep a.*e
```
$\qquad\qquad$匹配任意一个字符,*表示上一个字符0次或多次  
$\qquad\qquad$而第一个命令是错误的 
## $\qquad$ 5. 中括号: '[]'
$\qquad\qquad$ 正则`[]`符号,如`[a c]` 
$\qquad\qquad$ 实例:
```
history |grep r[a t]
```
$\qquad\qquad$`[]`匹配一个连续的区间,