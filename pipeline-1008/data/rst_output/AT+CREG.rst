
AT+CREG
=======

**Title**: 查询网络注册状态
**Types**: 执行, 查询

Formats::
   AT+CREG

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <n>
     - 0：禁止网络注册主动提供结果代码（默认设置）
1：允许网络注册主动提供结果代码
2：允许网络注册主动提供所在地讯息（CELL ID、LOCAL ID）。
     - N/A
   * - <stat>
     - 0：未注册，终端当前并未在搜寻新的运营商
1：已注册本地网络
2：未注册，终端正在搜寻基站
3：注册被拒绝
4：未知代码
5：已注册，处于漫游状态
6：ltesms only home
7：ltesms only roaming
8：EMER SVCE ONLY
9：CSFB NOT PREFER HOME
10：CSFB NOT PREFER ROAMING
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - ly home
7
            - ltesms o
          * - g
8
            - EMER SV
          * - E ONLY
9
            - 
   * - <lac>
     - 字符串型，2字节十六进制位置区代码
     - N/A
   * - <ci>
     - 字符串型，2字节十六进制小区编号
     - N/A
   * - <Act>
     - 0：GSM
1：GSM compact
2：UTRAN
3：GSM w/EGPRS
4：UTRAN w/HSDPA
5：UTRAN w/HSUPA
6：UTRAN w/HSDPA AND w/HSUPA
7：E-UTRAN
8：UTRAN w/HSPA+
     - N/A

**Description**: 查询模组的当前网络注册状态。\n命令格式