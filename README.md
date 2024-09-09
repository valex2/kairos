# Kairos
The objective of this project was to develop a low-cost, portable AQI (Air Quality Index) monitor that logs key air quality metrics and stores them for long-term tracking.

This is driven by the worsening air quality due to climate change, particularly in regions like California where wildfires contribute to increased particulate matter in the atmosphere. Affordable sensors, such as Kairos, offer a scalable solution for monitoring air quality across large areas, providing national agencies with valuable data to analyze climate patterns, identify hotspots, and allocate resources more effectively.

A key advantage of Kairos is its portability and accessibility. Designed to be carried by individuals, it requires minimal infrastructure, reducing the overhead costs typically associated with large-scale environmental monitoring. This enables on-the-ground data collection and empowers individuals to better understand and respond to the air quality and environmental hazards in their immediate surroundings, while also meaningfully contributing to a larger, community or state-wide, AQI dataset. This version of Kairos serves as a proof of concept and has the following features:

1. Embedded compute
    1. The [**ATMEL SAMD51J19**](https://www.microchip.com/en-us/product/atsamd51j19a), an accessible chip, with 120MHz CPU, 256 KB RAM, and plenty of IO buses to handle sensor data and logging.
2. Instrumentation
    1. A [**Bosch SensorTech BME 688**](https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors/bme688/) — enabling high-accuracy pressure, humidity, temperature, Volatile Organic Compound (VOC) and Volatile Sulfur Compound (VSC) monitoring.
    2. An [**LTR-329ALS-01**](https://www.mouser.com/datasheet/2/239/Lite-On_LTR-329ALS-01%20DS_ver1.1-348647.pdf) — enabling visible- and IR-range light intensity measurements.
3. Communication modalities
    1. A **USB bus** — for communication with a host computer
    2. A **microSD** bus — for time-stamped ***logging*** of sensor values. Using an external SD card allows for prolonged operation without needing to pause logging
    3. A **display** — for on the go monitoring of sensor values
4. Two different power modes
    1. **USB Power** — embedded voltage regulators enable Kairos to be used in a stationary setting, say a roof of a building, for extended periods of time
    2. **Battery Power** — a 2500mAh LiPO and embedded charging circuitry allow Kairos to be taken on the go, for better-monitoring frequently travelled environments without requiring frequent charging.

While this version of Kairos demonstrates proof of concept, future iterations should expand its capabilities with the following features:

1. **UV Sensor**: To capture sun intensity across more (and more dangerous) wavelengths, providing a more comprehensive solar exposure assessment.
2. **GPS Module**: To enable precise tracking of Kairos’ location, facilitating the creation of accurate heatmaps for key AQI metrics.
3. **Bluetooth Syncing**: To allow seamless data transfer to mobile phones, removing the need to manually retrieve data from an SD card.
4. **A Centralized Server**: To aggregate data from multiple Kairos units, generating regional-level heatmaps and providing actionable insights from averaged data points across different areas.
5. **A rugged, waterproof, miniaturized shell for on the go use.**