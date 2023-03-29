import json

from ClientOilCase import ClientOilCase

client = ClientOilCase('http://localhost:8080', 'p1@p1.com', '111111')

# client.add_result(client.get_available_resource(), 'get_available_resource')
# client.add_result(client.complete_move(), "complete_move")
# client.add_result(client.purchased_objects(), "purchased_objects")
# client.add_result(client.purchased_boreholes(), "purchased_boreholes")
client.add_result(client.purchased_seismic(), "purchased_seismic")

text = client.out_result('result.json')
print(json.dumps(text, indent=4))

