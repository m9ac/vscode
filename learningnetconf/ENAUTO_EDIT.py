from ncclient import manager
from router_info import router

config_template = open("/home/micah/vscode/learningnetconf/ios_config.xml").read()

netconf_config = config_template.format(
    interface_name="GigabitEthernet2", interface_desc="Micah was here")

with manager.connect(**router, hostkey_=False) as m:
    response = m.edit_config(netconf_config, target="candidate")

print(response)