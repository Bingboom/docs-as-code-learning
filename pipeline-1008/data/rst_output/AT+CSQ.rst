
AT+CSQ
======

**Title**: 获取信号强度
**Types**: 执行, 查询

Formats::
   AT+CSQ

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <signal>
     - 以下为signal(CSQ)与rssi对应关系：
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 0
            - <4或99 | <-107 dBm or unknown
          * - 1
            - <10 | <-93dBm
          * - 2
            - <16 | <-81 dBm
          * - 3
            - <22 | <-69dBm
          * - 4
            - <28 | <-57dBm
          * - 5
            - >=28 | >=-57 dBm
   * - <ber>
     - —
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 99
            - 误码率无法测量

**Description**: 查询接收信号强度<rssi>。\n命令格式