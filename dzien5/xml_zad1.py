# <ExchangeRatesSeries xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
# <Table>A</Table>
# <Currency>dolar amerykański</Currency>
# <Code>USD</Code>
# <Rates>
# <Rate>
# <No>241/A/NBP/2025</No>
# <EffectiveDate>2025-12-12</EffectiveDate>
# <Mid>3.6027</Mid>
# </Rate>
# </Rates>
# </ExchangeRatesSeries>

from xml.dom import minidom

root = minidom.Document()
xml = root.createElement('root')
root.appendChild(xml)

productChild = root.createElement('product')
productChild.setAttribute("name", "RAJ")
xml.appendChild(productChild)

xml_str = root.toprettyxml(indent='\t')
print(xml_str)
# <?xml version="1.0" ?>
# <root>
# 	<product name="RAJ"/>
# </root>

with open('dane_xml.xml',"w") as f:
    f.write(xml_str)