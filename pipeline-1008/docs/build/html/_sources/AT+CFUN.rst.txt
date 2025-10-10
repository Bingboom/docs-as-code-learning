
AT+CFUN
=======

**Title**: 设置模组功能
**Types**: 执行, 查询

Formats::
   AT+CFUN

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <fun>
     - 0：最小功能（turn off radio and SIM power）
1：全功能（默认）
4：关闭模组的发送和接收射频电路（飞行模式）
9：升级功能（可通过上位机工具升级版本）
     - N/A
   * - <rst>
     - 0：do not reset the MT before setting it to <fun> power level
1：reset the MT before setting it to <fun> power level
     - N/A

**Description**: 通过设置<fun>来选择模组的功能。<fun>只支持某些值。\n设置该参数后，掉电不保存。\n命令格式