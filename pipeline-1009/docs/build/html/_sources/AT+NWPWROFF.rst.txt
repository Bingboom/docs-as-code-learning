
AT+NWPWROFF
===========

**Title**: 模组关机指令
**Types**: 执行, 查询

Formats::
   AT+NWPWROFF

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <n>
     - 关机选项，数值形式，取值如下：
0：快速关机
1：正常流程关机
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 取值如下
            - 
          * - 0
            - 快速关机
          * - 1
            - 正常流程关机

**Description**: 模组关机指令。发送 AT+NWPWROFF 之前，需悬空或拉高模组 POWERKEY 管脚电平。返回 OK 后，若需重新开机，可拉低 POWERKEY 管脚电平。
命令格式