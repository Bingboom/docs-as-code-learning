
AT+CMGL
=======

**Title**: 短信列表
**Types**: 执行, 查询

Formats::
   AT+CMGL

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <stat>
     - 字符串类型或者数字类型
当设置AT+CMGF=1时：
"REC UNREAD"：接收到的未读的短信
"REC READ"：接收到的已读的短信
"STO UNSENT"：存储的未发送的短信
"STO SENT"：存储的已发送的短信
"ALL"：所有短信
当设置AT+CMGF=0时：
0：接收到的未读的短信
1：接收到的已读的短信
2：存储的未发送的短信
3：存储的已发送的短信
4：所有短信
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 当设置AT+CMGF=1时
            - 
          * - "REC UNREAD"
            - 接收到的未读的短信
          * - "REC READ"
            - 接收到的已读的短信
          * - "STO UNSENT"
            - 存储的未发送的短信
          * - "STO SENT"
            - 存储的已发送的短信
          * - "ALL"
            - 所有短信
          * - 当设置AT+CMGF=0时
            - 
          * - 0
            - 接收到的未读的短信
          * - 1
            - 接收到的已读的短信
          * - 2
            - 存储的未发送的短信
          * - 3
            - 存储的已发送的短信
          * - 4
            - 所有短信

**Description**: 读取某一类存储的短信，短信会被从+CPMS 指令选取的当前的存储器中读出来。
命令格式