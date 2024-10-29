# Edge System for Sustainable Building

**Edge System for Sustainable Building** is an innovative solution designed to make buildings intelligent and sustainable. The project focuses on monitoring and controlling energy consumption and managing electronic devices, with the goal of automating processes and minimizing risks.

Through a notification and response system, actuators are activated to balance the measured parameters with preset values. Users can interact with the processed data via a user-friendly interface on the platform.

## Architecture

The system architecture is divided into two main components: the **Edge** and the **Cloud**.

### Edge Layer
The edge layer begins with **Libelium One** environmental sensors, which regularly measure parameters such as temperature, humidity, and CO/CO₂ emissions. These sensors generate data that is first sent to a **Cisco Catalyst switch** (using the MQTT protocol) with the **IOx operating system**. Here, the data is aggregated and converted into a common format before being forwarded to the cloud.

### Cloud Layer
Once the data has been pre-processed at the edge, it is sent to the cloud for detailed analysis and storage. This transmission is handled via a REST API, where messages are received by the cloud backend, developed using **Django**, a Python web framework. The data is then stored in a **PostgreSQL** database. 

The platform's **frontend**, built with JavaScript, provides users with statistical insights on these parameters, displayed in an intuitive and accessible way.

## Key Features

- **Energy Monitoring and Control**: Continuous monitoring of energy usage to optimize consumption.
- **Environmental Data Collection**: Sensors collect temperature, humidity, and gas emissions data.
- **Automated Process Management**: The system manages devices and activates actuators based on preset conditions.
- **User Interaction Platform**: A user-friendly platform allows users to interact with real-time data and analytics.
- **Edge and Cloud Integration**: Data is processed on edge devices and further analyzed in the cloud, optimizing resource use.

## Technologies Used

- **Libelium One Sensors**: Environmental sensors for data collection.
- **Cisco Catalyst Switch with IOx OS**: For data aggregation and MQTT protocol support.
- **MQTT Protocol**: Used for transmitting data from sensors to the edge switch.
- **Django**: Cloud backend developed using the Django framework.
- **PostgreSQL**: Database for secure data storage.
- **JavaScript**: Frontend for data visualization and user interaction.

## Project Goals

The **Edge System for Sustainable Building** aims to provide a smart, automated solution for managing building sustainability, energy consumption, and safety. By combining edge and cloud capabilities, the system enables real-time monitoring, efficient process management, and comprehensive data insights to promote sustainable building practices.

---

This `README` structure should provide clear information for anyone interested in understanding and potentially contributing to the project.
