
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
     - 信号强度CSQ
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
     - Xx
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 99
            - 误码率无法测量