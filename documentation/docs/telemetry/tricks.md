#### Get Providers 

```powershell
Get-EtwTraceProvider | where {$_.SessionName -match "Diagtrack-Listener"} | Out-File ..\..\Users\Targeto\Desktop\etw_providers.txt
```


#### Configuring telemetry
[Link][https://www.askvg.com/truth-behind-disallowing-telemetry-and-data-collection-trick-in-windows-10/]


#### Update group policy
``` 
gpupdate /force
```     



### Isolate services SVCHost

https://www.askvg.com/windows-10-fix-too-many-svchost-exe-service-host-process-running-in-task-manager/

