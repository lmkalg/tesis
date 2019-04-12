# Questions

* Why isn't possible to load the PDB for ntdll? They don't export all the symbols or what? 
* All the triggers I developed are made from spontaenus events. Is it mandatory to make something not spontaneus? I don't see why
* Why some of the calls back have just until the user land? 
* Did you know this [page](https://docs.microsoft.com/en-us/windows/privacy/basic-level-windows-diagnostic-events-and-fields-1709#common-data-fields)? It's pretty useful. But is not for our version with is 1607 right?
* What is the difference between what I developed with the windbg scripts and the extension you already developed for minitoring the events? 
* The point of the "Determine origin of telemtry data" was just to develop workloads right? I mean, although I print the call stacks in each call, for the triggers I developed so far, I didn't used it too much.
* All triggers developed in the first part should trigger events at the **Basic** level? 
* Should the Executioner be able to just receive the name of the script and execute it? or it should be whitelisted inside the Executioner.exe ? (the former will allow to add new scripts/exe without recompiling)
