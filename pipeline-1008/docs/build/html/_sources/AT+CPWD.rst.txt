
AT+CPWD
=======

**Title**: 修改密码指令
**Types**: 执行, 查询

Formats::
   AT+CPWD

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <fac>
     - 需带双引号""
"P2"：SIM PIN2
"SC"：SIM卡
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 需带双引号""
"P2"
            - SIM PIN2
"S
          * - "
            - SIM卡
   * - <oldpwd>
     - 需带双引号""，旧密码或操作码，字符串类型
     - N/A
   * - <newpwd>
     - 需带双引号""，新密码或操作码，字符串类型
     - N/A

**Description**: 修改模组锁功能的密码。\n若需修改PIN码，需锁定SIM卡（AT+CLCK="SC",1,"1234"）后才能修改。\n命令格式