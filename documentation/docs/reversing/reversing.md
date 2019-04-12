### Path

Went to **EtwWrite** and x-reference it.
 
Reached a function called **PopDiagTraceSetSystemState** (There are many functions called **PopDiagTrace\***). After checking if the **POP_ETW_EVENT_SETSYSTEMSTATE** event descriptor is enabled (calling **EtwEventEnabled**), it calls to the **EtwWrite** functionality. 

X referencing **PopDiagTraceSetSystemState**, I found that **PopSetSystemState** is the only one performing a call. 

X referencing **PopSetSystemState**, we found 4 different functionalities, whereas one of them is named **PoSetUserPresent**. 

This last functionality is exported by the kernel, therefore a user-land application should be able to use it. 

#### Summary

**PoSetUserPresent** --> **PopSetSystemState** --> **PopDiagTraceSetSystemState** --> **EtwWrite**  

### Tricks / Notes

### Ideas

Put a breakpoint each time a new provider registers, and try if the GUID that they're providing is some of known guids, print the stack trace. So we can know from where they're called (windbg scripting?).
Once we identify that guy, we can also set another breakpoint of write just when the handler returned by the registering function is used. 
That are two differnt scipts
take into account the structure of the GUID when comparting it with the one received by parameter.

#### Calling Convention

**Integers**:

1. RCX
2. RDX
3. R8
4. R9

Rest of parameters by stack leaving the place for these ones!

**Floating point**:

1. xmm0
2. xmm1
3. xmm2
4. xmm3

#### Word values

1. **w | word** = 16 bits (2 bytes)
2. **dw | dword** = 32 bits (4 bytes)
3. **qw | word** = 64 bits (8 bytes)

#### What is GS Segment? 
Reference: https://www.andrea-allievi.com/blog/x64-memory-segmentation-is-the-game-over/

A pointer to the **TEB**

#### Symbols

Where to dowload the symbols manually:

[Windows Symbols](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/debugger-download-symbols%)



## Useful Structures

Kernel structures that seem to be important for us:

* **nt!\_ETW_REG_ENTRY**
* **nt!\_ETW_GUID_ENTRY**
* **nt!\_GUID**
* **nt!\_WMI_LOGGER_CONTEXT**
* **nt!\_ENABLE_TRACE_INFO**
* **nt!\_ESERVERSILO_GLOBALS**
* **nt!\_OBJECT_HEADER**
* **nt!\_DEVICE_OBJECT**
* **nt!\_WMI_BUFFER_HEADER**


## WTF

**0DC328033B3EBAA54994547854849625h** (Founded in EtwRegisterEx as SecurityGUid or something like that).

EtwpRegistrationObjectType inside the ObReferenceObjectByHandle of EtwpTrackProviderBinary function.
