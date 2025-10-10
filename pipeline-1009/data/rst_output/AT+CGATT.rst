
AT+CGATT
========

**Title**: 设置GPRS附着和分离
**Types**: 执行, 查询

Formats::
   AT+CGATT

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <state>
     - 取值范围（0,1）
0：表示分离
1：表示附着
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 0
            - 表示分离
          * - 1
            - 表示附着

**Description**: 该指令用来查询、设置GPRS附着和分离。掉电不保存。
模组默认情况下，会主动进行GPRS附着。
进行PPP连接之前要确保GPRS是处于附着状态，AT流程增加查询指令AT+CGATT?：
如果返回值是1，则可以直接进行PPP连接；
如果返回值是0，则需进行手动附着，即AT+CGATT=1。
命令格式