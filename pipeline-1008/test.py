from jinja2 import Template

cmd = {
    'command': 'AT+CSQ',
    'title': '获取信号强度',
    'type': ['执行', '查询'],
    'formats': ['AT+CSQ'],
    'parameters': [
        {
            'name': '<signal>',
            'desc': '信号强度CSQ',
            'valmap': {
                '0': '<4或99',
                '1': '<10',
                '2': '<16',
                '3': '<22',
                '4': '<28',
                '5': '>=28'
            }
        },
        {
            'name': '<ber>',
            'desc': 'Xx',
            'valmap': {
                '0...7': '参考GSM 05.08 8.2.4 章节表格中RXQUAL 的取值',
                '99': '误码率无法测量'
            }
        }
    ],
    'examples': [{'cmd': 'AT+CSQ', 'resp': ''}],
    'description': '获取信号强度',
    'notes': '',
}

print("DEBUG: cmd['parameters'] valmap types and contents:")
for p in cmd['parameters']:
    print(f"p['name']={p['name']}, type(p.get('valmap'))={type(p.get('valmap'))}, p['valmap']={p.get('valmap')}")

TEMPLATE_STR = '''
{{ cmd.command }}
{{ '=' * cmd.command|length }}

**Title**: {{ cmd.title }}
**Types**: {{ cmd.type|join(', ') }}

Formats::
{%- for f in cmd.formats %}
   {{ f }}
{%- endfor %}

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
{%- for p in cmd.parameters %}
   * - {{ p.name }}
     - {{ p.desc or '—' }}
     - {%- if p.valmap %}
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
{%- for k, v in p.valmap.items() %}
          * - {{ k }}
            - {{ v }}
{%- endfor %}
       {%- else %} N/A {%- endif %}
{%- endfor %}

Examples
--------
{%- for ex in cmd.examples %}
.. code-block:: none

   {{ ex.cmd }}
   {{ ex.resp }}
{%- endfor %}

**Description**: {{ cmd.description or '' }}

{%- if cmd.notes %}
**Notes**: {{ cmd.notes }}
{%- endif %}
'''

RST_TMPL = Template(TEMPLATE_STR)

if __name__ == "__main__":
    print("TEMPLATE CONTENTS:\n", TEMPLATE_STR)
    print(RST_TMPL.render(cmd=cmd))