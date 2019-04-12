{!windbg/useful_functions.md!}

### Scripting
{!windbg/scripting.md!}


### Commands
* **dp** _address_: Shows the memory pointed by that pointer.


### Tricks

#### To set up initial debugging with the kernel

Debug --> Kernel Connection --> Cycle Initial Break


#### Iterating an output of a command
```
kd>.foreach /pS 13 /ps 13 (name {!process -1 0 }) { .echo name }
```
In this case, it will iterate the list gathered as output of **!process -1 0**, will go till the value at index 0x13, and will print it. 

```
kd> .foreach /pS 13 /ps 13 (name {!process -1 0 }) { aS ${/v:ProcessName} "${name}" }
kd> .echo ProcessName
explorer.exe
```
In this case, will save it inside an alias variable. 




#### Comparing strings 

With alias:
```
kd> .if ($spat("${ProcessName}","explorer.exe ") !=0) {.echo "a"} .else {.echo "b"}
```
**ProcesName** in this case is an alias. If both strings are equal, an **a** will be printed. Otherwise, a **b** will be printed. 

s

$$poi()$$