Tasks done:
    - Fixing version and deactivate Windows Updates
        - Didn't find the vbox image inside the shared servers (neither data1 nor data3). 
        - Found an ISO that you have me the first time, and I used that to do a new installation (now the kernels matched)
        - The version is 1607 and now the updates are deactivated.
        - The framework is working again :) 
    
    - Bubble chart:
        - Guess I missed some part of this chart. 
        - I created the one that relates each process name that was used. The thing was that there was not any reason for creating a graph/nodes chart, due to all the nodes were going to point to the telemetry one (or the central). That's why I created a PIE chart.. Did I miss something? 
        - There was something related with the DLL libs that were loaded right? 


        - ADD PID INFORMATION <-----
        - PERCENTAJE 
        - NAME OF EXECUTABLE.
        - AMOUNT OF WRITES
    

    - Service isolation:
        - Automatic executed after 1703 (creators update) when amount of RAM > 3.5 Gb.
        - There is a registry key that can be manipulated (SvcHostSplitThresholdInKB)
        - Command to put a service to run on their own process instead of being shared.
        sc config <service> 
        - Once modified, machine should be rebooted.
        - Sources:
            - https://winaero.com/blog/set-split-threshold-svchost-windows-10/
            - https://superuser.com/questions/1212665/did-svchost-exe-behaviour-change-in-windows-10-creators-update-build-1703/1212692#1212692
            - https://blogs.windows.com/windowsexperience/2016/10/07/announcing-windows-10-insider-preview-build-14942-for-pc/#MeSl5BkVzzBoksQj.97



        - READ THE REGISTRY KEY OF THE DEBUGERE FROM THE DEBUGGER
        - ANALYZE THE KEYS AND SEE THE DLL WHICH IS BINDED.
        - 
        !reg openkeys 8c40c370
        !REG 

    - Video:
        - Finished it
        - Where / how to send it?

    - PRESENTATION PHASE:
        - CHNAGE EVENT ID BECAUSE IT CCAN BE CONFUSED WITH THE EVENT ID OF WINDOWS MESSGS:
            https://docs.microsoft.com/en-us/windows/desktop/msi/event-logging
        - Go deeper with the meta name of the events ETW (reread the page of events windows)
