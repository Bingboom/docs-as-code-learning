
AT+NWDNS
========

**Title**: 域名解析
**Types**: 执行, 查询

Formats::
   AT+NWDNS

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <hostname>
     - 字符串，域名，可不带双引号，最大长度128
     - N/A
   * - <IP>
     - 字符串，IP地址
     - N/A
   * - <Sign>
     - 字符串，IP类型，IPV4，IPV6
     - N/A

**Description**: 内置协议栈拨号后，查询DNS解析结果。\n先使用AT+XIIC命令拨号成功后，才能执行该命令。\n域名填入不校验正确性，需保证填入内容的正确性。\n命令格式