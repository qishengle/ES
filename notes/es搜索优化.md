## [Function Score Query](https://blog.csdn.net/wwd0501/article/details/78652850)

> ### <font color="lightpink"  face="思源黑体">优化Elasticsearch搜索结果</font>
- #### <table><tr><td bgcolor="lightgreen"><code>function_score 提供了几种默认的计算分值的函数：</code></td></tr></table>

#### 1.  <font color="orange">weight</font>：设置权重
    只需要设置一个数字作为权重，文档的分数就会乘以该权重。
	最大的用途应该就是和过滤器一起使用
#### 2. <font color="orange">field_value_factor</font>：将某个字段的值进行计算得出分数。
通过文档中某个字段的值计算出一个分数，它有以下属性：
- field：指定字段名
- factor：对字段值进行预处理，乘以指定的数值（默认为 1）
- modifier将字段值进行加工，有以下的几个选项：
	- none：不处理
	- log：计算对数
	- log1p：先将字段值 +1，再计算对数
	- log2p：先将字段值 +2，再计算对数
	- ln：计算自然对数
	- ln1p：先将字段值 +1，再计算自然对数
	- ln2p：先将字段值 +2，再计算自然对数
	- square：计算平方
	- sqrt：计算平方根
	- reciprocal：计算倒数
---
```
{
  "query": {
    "function_score": {
      "query": {
        "match": {
          "title": "雨伞"
        }
      },
      "field_value_factor": {
        "field": "sales",
        "modifier": "log1p",
        "factor": 0.1
      },
      "boost_mode": "sum"
    }
  }
}
```
这条查询会将标题中带有雨伞的商品检索出来，然后对这些文档计算一个与库存相关的分数，并与之前相关度的分数相加，对应的公式为：
_score = _score + log (1 + 0.1 * sales)
#### 3. <font color="orange">random_score</font>：随机得到 0 到 1 分数
衰减函数：同样以某个字段的值为标准，距离某个值越近得分越高

#### 4. <font color="orange">script_score</font>：通过自定义脚本计算分值
它还有一个属性boost_mode可以指定计算后的分数与原始的_score如何合并，有以下选项：
  - <font color="green">multiply</font>：将结果乘以_score

  - <font color="green">sum</font>：将结果加上_score
  - <font color="green">min</font>：取结果与_score的较小值
  - <font color="green">max</font>：取结果与_score的较大值
  - <font color="green">replace</font>：使结果替换掉_score

### 
