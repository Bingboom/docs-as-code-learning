
AT+NWRFTEST
===========

**Title**: 模组强发强收指令（仅可用于测试）
**Types**: 执行, 查询

Formats::
   AT+NWRFTEST

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <rftest_mode>
     - 0：退出强发强收测试模式
1：进入强发强收测试模式
     - N/A
   * - <rat>
     - 1：LTE 当前仅支持rat为LTE 的测试
     - N/A
   * - <band>
     - 频段指示
1：LTE band 1
2：LTE band 2
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 2
            - LTE ba
   * - <bw>
     - 带宽，平台限制，当前仅支持bw传入为0
     - N/A
   * - <channel>
     - 频点信息（平台限制，当前仅支持每个频段的中心频点，默认值0 即表示中心频点），各频段中心频点信息如下：
LTE Band 1：上行频点18300   下行频点300
LTE Band 2：上行频点18900下行频点900
LTE Band 3：上行频点19500下行频点1575
LTE Band 4：上行频点20175下行频点2175
LTE Band 5：上行频点20525下行频点2525
LTE Band 6：上行频点20700下行频点2700
LTE Band 7：上行频点21100下行频点3100
LTE Band 8：上行频点12625下行频点3625
LTE Band 20：上行频点24300下行频点6300
LTE Band 28：上行频点27435下行频点9435
LTE Band 34：上行频点36275下行频点36275
LTE Band 38：上行频点38000下行频点38000
LTE Band 39：上行频点38450下行频点38450
LTE Band 40：上行频点39150下行频点39150
LTE Band 41：上行频点40620下行频点40620
LTE Band 66：上行频点59250下行频点59350
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 即表示中心频点），各频段中心频点信息如下
            - LTE
          * - d 2
            - 上行频点
          * - d 3
            - 上行频点
          * - d 4
            - 上行频点2
          * - d 5
            - 上行频点2
          * - d 6
            - 上行频点2
          * - d 7
            - 上行频点2
          * - d 8
            - 上行频点
          * - d 28
            - 上行频点27435下行频点9435
LTE
          * - d 34
            - 上行频点36275下行频点36275
LTE
          * - d 38
            - 上行频点38
          * - d 39
            - 上行频点3845
          * - d 66
            - 上行频点5925
   * - <chain_idx>
     - 不适用，直接填入默认值0
     - N/A
   * - <expected_rxagc>
     - 预期接收功率，为负值
     - N/A
   * - <tx_enable>,
     - 强发测试设置为1，强收测试设置为0
     - N/A
   * - <tx_power>
     - 发射功率，平台限制，当前仅支持传入23和10，分别表示最大发射功率23db和发射功率10db
     - N/A
   * - <lte_start_rb>
     - 不适用，直接填入默认值0
     - N/A
   * - <lte_num_rb>
     - 不适用，直接填入默认值0
     - N/A
   * - <waveform>
     - 不适用，直接填入默认值0
     - N/A

**Description**: 用于在测试模式下验证模组强发强收功能, 只能测试每个频段的中心频点的发射功率和接收功率精度。由于平台限制，强收强发测试精度均有一些误差。\n强发测试只能验证最大发射功率23db和10db，其他值无法验证。\n命令格式