
AT+CSCS
=======

**Title**: 设置TE字符集
**Types**: 执行, 查询

Formats::
   AT+CSCS

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <chset>
     - "GSM"：GSM默认字母表（GSM03.38.6.2.1）
"IRA"：国际参考字母表(international reference alphabet)(ITU-T T.50)
"UCS2"：16-bit universal multiple-octet coded character set (USO/IEC10646)。UCS2字符串被转换成一个十六进制数（0x0000～0xFFFF），只有在相应语句中的字符串才用UCS2编码，其余的命令和响应仍旧是IRA字母表格式的。
"PCCP936"：等同GBK编码格式
"IRA"：国际参考字母表(international reference alphabet)(ITU-T T.50)
"UTF-8"：针对Unicode的一种可变长度字符编码
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - "GSM"
            - GSM默认字母表（GSM
          * - ）
"IRA"
            - 国际参考字母表(i
          * - S2"
            - 
          * - P936"
            - 等同G
          * - K编码格式
"IRA"
            - 国际参考字母表(i
          * - -8"
            - 针对U

**Description**: 设置TE字符集格式。\n命令格式