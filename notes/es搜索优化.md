## [Function Score Query](https://blog.csdn.net/wwd0501/article/details/78652850)

> ### <font color="lightpink"  face="思源黑体">优化Elasticsearch搜索结果</font>
- #### <code>function_score 提供了几种默认的计算分值的函数：</code>

1. <font color="orange">weight</font>：设置权重

2. <font color="orange">field_value_factor</font>：将某个字段的值进行计算得出分数。

3. <font color="orange">random_score</font>：随机得到 0 到 1 分数
衰减函数：同样以某个字段的值为标准，距离某个值越近得分越高

4. <font color="orange">script_score</font>：通过自定义脚本计算分值
它还有一个属性boost_mode可以指定计算后的分数与原始的_score如何合并，有以下选项：

    - <font color="green">multiply</font>：将结果乘以_score
    
    - <font color="green">sum</font>：将结果加上_score
    - <font color="green">min</font>：取结果与_score的较小值
    - <font color="green">max</font>：取结果与_score的较大值
    - <font color="green">replace</font>：使结果替换掉_score