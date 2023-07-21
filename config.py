# ************************************** CONFIGURATION FILE **************************************

# SET THE ROOM NAME
ROOM = "DTLab"

# SET THE PROTOCOL
PROTOCOL = "MQTT"

# SET A DESCRIPTOR FOR KIND OF MEASUREMENTS
DESCRIPTOR = "Sustainability"

# SET THE SENSOR'S NAME
SENSOR_NAME = "Libellium"

# SET THE SENSOR'S MODEL
SENSOR_MODEL = "?"

# SET THE BROKER FOR MQTT SERVICES
BROKER = "broker.emqx.io"

# SET THE TOPIC WHERE MEASUREMENTS WILL BE PUBLISHED
TOPIC_MEASUREMENTS  = f"{ROOM}/measurements"

# SET THE TOPIC WHERE COMMANDS FOR THE ACTUATORS WILL BE PUBLISHED
TOPIC_COMMANDS = f"{ROOM}/commands"