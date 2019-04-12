# 

* Session management functionalities are implemented as part of the **subystem DLLs**. Example he **StartTrace** function aimed to activate a session is implemented in the **advapi32.dll**

* Example of ETW Controller: **xperf** (Windows Performance Toolkit).

* Example of Consumer:
    * **xperf**
    * **Windows Event Viewer**

* **EventLog** use to exist as a different component from the ETW, until the 10 came up. It as primarily used for logging of Windows Events (kernel events). 

* In the **Event viewer** utility you can see all the Event logging channels and the events, even witht the **EventLog** format.

* For the xperf.exe, logger are sessions.