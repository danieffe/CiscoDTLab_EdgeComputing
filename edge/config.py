# ************************************** CONFIGURATION FILE **************************************

import os

# SET SERVER
IP_ADDRESS = os.environ.get('SERVER_IP_ADDRESS', '0.0.0.0')
PORT_NUMBER = os.environ.get('SERVER_PORT_NUMBER', '8080')
BUFFER_SIZE = os.environ.get('SERVER_BUFFER_SIZE', '1024')

# SET ROOM NAME
ROOM = os.environ.get('ROOM_NAME', 'DTLab')

# SET THE LOCAL BROKER ADDRESS FOR MQTT SERVICES
BROKER_IP_ADDRESS = os.environ.get('BROKER_IP_ADDRESS', '127.0.0.1')
BROKER_PORT_NUMBER = os.environ.get('BROKER_PORT_NUMBER', '1883')

CLOUD_IP_ADDRESS = os.environ.get('CLOUD_IP_ADDRESS', '127.0.0.1')

# SET THE TOPIC WHERE MEASUREMENTS WILL BE PUBLISHED
TOPIC_MEASUREMENTS  = f"{ROOM}/measurements"

# SET THE TOPIC WHERE COMMANDS FOR THE ACTUATORS WILL BE PUBLISHED
TOPIC_COMMANDS = f"{ROOM}/commands"