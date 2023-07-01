from ncclient import manager
from router_info import router

with open('/home/micah/vscode/learningnetconf/ios_config.xml') as file:
    config_template = file.read()


netconf_config = config_template.format(
    interface_name="GigabitEthernet2", interface_desc="Micah was here")

with manager.connect(**router, hostkey_verify=False) as m:
    response = m.edit_config(netconf_config, target="candidate")

print(response)