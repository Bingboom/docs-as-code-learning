
AT+CCLK
=======

**Title**: 时钟管理
**Types**: 执行, 查询

Formats::
   AT+CCLK

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <time>
     - 字符串，格式为 “yy/MM/dd,hh:mm:ss[TZ]”，指示年、月、日、小时、分钟、秒
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 格式为
            - “yy/MM/dd
          * - hh
            - mm:ss[TZ]”
   * - TZ
     - 2位数字表示当地时间与GMT之间时差。
该信息可选，只有当网络支持时该信息才显示。当地时间为GMT时间时不显示。
     - N/A

**Description**: 设置和查询模组的实时时钟。
设置的时间立即生效，掉电保存；默认时钟为0时区，使用1/4时区。
命令格式