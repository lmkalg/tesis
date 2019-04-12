### List all providers associated to DiagTrack running session (Powershell)

```powershell
Get-EtwTraceProvider | where {$_.SessionName -match "Diagtrack-Listener"}
```

### Get all providers (powershell)

```powershell
Get-EtwTraceProvider | Out-File providers.txt
```

### Creating ETW session and attaching providers (original)

```
xperf -start UserTrace -on Microsoft-Windows-Diagtrack+43ac453b-97cd-4b51-4376-db7c9bb963ac+da995380-18dc-5612-a0db-161c5db2c2c1+6489b27f-7c43-5886-1d00-0a61bb2a375b+836D9D37-46C1-41BE-A56-09B88F964468 -f C:\tmp\diaglog%d.etl -FileMode Newfile -MaxFile 50
```

### Creating ETW session and attaching providers (new)

```
xperf -start UserTrace -on Microsoft-Windows-Diagtrack+43ac453b-97cd-4b51-4376-db7c9bb963ac+da995380-18dc-5612-a0db-161c5db2c2c1+6489b27f-7c43-5886-1d00-0a61bb2a375b+4bfe0fde-99d6-5630-8a47-da7bfaefd876+e34441d9-5bcf-4958-b787-3bf824f362d7+3d6120a6-0986-51c4-213a-e2975903051d+836D9D37-46C1-41BE-A956-09B88F964468 -f C:\tmp\diaglog%d.etl -FileMode Newfile -MaxFile 50
```

### Running datavisualizator

```
Desktop\partu\development\dataVisualizator\dataVisualizator\bin\Debug\dataVisualizator.exe Desktop\partu\development\data\log_temp.txt C:\Users\ERNW\Desktop\partu\development\data\output 1
```

### Checking the log

```
type Desktop\partu\development\dataVisualizator\dataVisualizator\bin\Debug\log.txt
```

### Opening statistics

```
Desktop\partu\development\data\output\statistics.html
```

### Running powershell scripts

```
powershell.exe -executionPolicy bypass  -File isolate_all_services_reg_keys.ps1
```

### Run Yara Rule

```
yara -r -s -m find_sec_provider_guid.txt C:\Windows\
```

### Run a binary as a service
```
sc create <service_name> binPath="<path_to_binary>"
```


### Trigger for svchost

```
sc create srvcdevicecensus binPath="C:\Windows\System32\DeviceCensus.exe"
sc start srvcdevicecensus
```