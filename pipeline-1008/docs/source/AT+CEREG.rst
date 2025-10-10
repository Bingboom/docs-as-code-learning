
AT+CEREG
========

**Title**: 获取EPS网络注册状态
**Types**: 执行, 查询

Formats::
   AT+CEREG

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
2：允许网络注册主动提供所在地信息（CELL ID、LOCAL ID）
4：允许网络注册主动提供Active-Time和Periodic-TAU
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - AL ID）
4
            - 允许网络注册主动提供Active-Time和Periodic-TAU
   * - <stat>
     - 0：未注册，终端当前并未在搜寻新的运营商
1：已注册本地网络
2：未注册，终端正在搜寻基站
3：注册被拒绝
4：未知代码
5：已注册，处于漫游状态
     - N/A
   * - <tac>
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
6：UTRAN w/HSDPA and HSUPA
7：E-UTRAN
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - d HSUPA
7
            - E-UTRAN

**Description**: 查询EPS网络注册状态。\n命令格式