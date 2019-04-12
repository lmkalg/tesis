### Description
Runs as a service with display  name **DiagTrack**. Service name: **utcsrc**

### Configuration Levels

The type of telemetry data, can be gather is determined by four different levels:

* **Security (not in all w10 versions)**: Information needed to help protect Windows. For example: Data about the Telemetry and Connected User Experiences component, the Malicious Software Removal Tool and WindowsDefender.
* **Basic**: Device information, data related to quality, compatibility of the application, application usage data and *security* level data. 
* **Enhanced**: Use of Windows, Windows Server, System center and applications. The performance, advanced reliability data and data from *basic* and *security* levels. 
* **Full**: All the necessary data to identify problems and help solve them, in addition to data from *basic*, *security* and *enhanced* levels. 

#### Change telemetry level

Execute: gpedit.msc

### Sources of information

There are at least 3 different sources: 

* **DiagTrackListener (ETW Session)**
* **AutoLoggerDiagTrackListener (ETW Session)**
* **External Executables**

### References

1. http://www.zdnet.com/article/windows-10-telemetry-secrets/
2. https://docs.microsoft.com/es-es/windows/configuration/configure-windows-diagnostic-data-in-your-organization
