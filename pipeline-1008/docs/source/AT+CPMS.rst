
AT+CPMS
=======

**Title**: 首选短信存储器
**Types**: 执行, 查询

Formats::
   AT+CPMS

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <mem1>
<mem2>
<mem3>
"SM"：
"ME"：
"MT"：
     - 读取和删除 SMS 时使用的存储器,字符串类型
存储和发送 SMS 时使用的存储器
若没有建立到 TE 的路由，则将接收的 SMS 存储在该存储器内
SIM 卡 SMS 存储器
ME SMS 存储器
SIM 卡和 ME SMS 存储器
     - N/A
   * - <mem1>
     - 字符串类型, 例如："SM", "ME"
"SM"：SIM only
"ME"：ME only
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 例如
            - "SM"
          * - "ME"
"SM"
            - SIM o
          * - ly
"ME"
            - ME o
   * - <used>
     - 已使用数目。
     - N/A
   * - <total>
     - 存储器总容量数目。
     - N/A

**Description**: 用于首选短信存储器。\n命令格式