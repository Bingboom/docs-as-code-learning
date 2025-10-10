
AT+CSMP
=======

**Title**: 设置文本模式参数
**Types**: 执行, 查询

Formats::
   AT+CSMP

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <fo>
     - <fo>：取决于该命令或结果码：GSM 03.40 SMS-DELIVER的前8位；
SMS-SUBMIT(缺省值：17)；或采用整数型的SMS-COMMAND（缺省值：2）
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - <fo>
            - 取决于该命令或结果码：GSM
          * - MIT(缺省值
            - 
          * - OMMAND（缺省值
            - 2）
   * - <vp>
     - —
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 0-143
            - (vp+1)*5mins，最大为12小时
          * - 144-167
            - 12hours +((vp–143)*30mins)，最大为24小时
          * - 168-196
            - (vp–166)*1day
          * - 197-255
            - (vp–192)*1week
   * - <pid>
     - 整数型的TP-协议-标识（缺省值：0）
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 整数型的TP-协议-标识（缺省值
            - 
   * - <dcs>
     - 整数型的小区广播数据编码方案（缺省值：0）
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 整数型的小区广播数据编码方案（缺省值
            - 

**Description**: 文本模式下，选择需要的附加参数取值；设置从SMSC接收到该消息时算起的有效期或定义有效期终止的绝对时间。\n命令格式