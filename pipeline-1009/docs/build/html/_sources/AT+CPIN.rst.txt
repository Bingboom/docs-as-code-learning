
AT+CPIN
=======

**Title**: 输入PIN码
**Types**: 执行, 查询

Formats::
   AT+CPIN

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <pin>, <newpin>
     - 字符串类型
     - N/A
   * - <code>
     - READY：不需要输入任何密码
NO SIM：未检测到卡
SIM PIN：需要输入PIN码
SIM PUK：需要输入PUK码
SIM PIN2：需要输入PIN2码
SIM PUK2：需要输入PUK2码
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - READY
            - 不需要输入任何密码
          * - NO SIM
            - 未检测到卡
          * - SIM PIN
            - 需要输入PIN码
          * - SIM PUK
            - 需要输入PUK码
          * - SIM PIN2
            - 需要输入PIN2码
          * - SIM PUK2
            - 需要输入PUK2码

**Description**: 查询PIN状态以及输入PIN码。
若要输入PIN码，需锁定当前SIM卡（AT+CLCK="SC",1,"1234"）后，重启模组才能输入PIN码；输入三次错误的PIN码后，会要求输入PUK码才能解锁。
命令格式