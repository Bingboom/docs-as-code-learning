
AT+CMGD
=======

**Title**: 删除短消息
**Types**: 执行, 查询

Formats::
   AT+CMGD

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <index>
     - 存贮的短消息的记录号
     - N/A
   * - <delflag>
     - 整型值
0：删除指定记录号的短信
1：删除所有已读短信
2：删除所有已读和已发送的短信
3：删除所有已读、已发送和未发送的短信
4：删除所有短信
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 0
            - 删除指定记录号的短信
          * - 1
            - 删除所有已读短信
          * - 2
            - 删除所有已读和已发送的短信
          * - 3
            - 删除所有已读、已发送和未发送的短信
          * - 4
            - 删除所有短信

**Description**: 从当前存储器中删除短消息。
命令格式