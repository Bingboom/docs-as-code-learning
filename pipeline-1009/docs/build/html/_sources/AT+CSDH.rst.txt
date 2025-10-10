
AT+CSDH
=======

**Title**: 显示文本模式参数
**Types**: 执行, 查询

Formats::
   AT+CSDH

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <show>
     - 0：不显示（默认值）
1：显示
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 0
            - 不显示（默认值）
          * - 1
            - 显示

**Description**: 设置是否在文本模式下的结果码中显示详细的头信息。该指令在短信文本模式下有效，需发送AT+CMGF=1设置成文本模式。
命令格式