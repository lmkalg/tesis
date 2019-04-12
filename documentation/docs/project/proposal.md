Reverse engineering of Windows Kernel telemetry component

Although technology evolves each time faster, human beings cannot adapt to it with the same speed. Even though tools and software which gather information has existed since several years ago, most of the people are realizing the impact of others having their private information not too long ago.

Windows, the widest used operating system in the world, has a component embedded in the kernel called Telemetry. It gathers information from the system with the goal of analzying and fixing software problems, improving the user experience, helping to improve the quality of Windows, among others. What kind of information can be obtained by this component, is partially configurable in four different levels: security, basic, enhanced and full. Being "security" the level where less information is gathered and "full" the opposite case.

How Telemetry stores/process/administrates the information extracted? It uses a widely used framework called Event Tracer for Windows (ETW). Embedded in most of the kernel modules, the ETW has the goal of providing a common interface to log events and therefore help to debug applications or understand how the system is working. Making use of sessions (were the events are stored) the different modules (acting as providers) write events depicting what are they doing, if some issues has happened, etc. Later on, other entities (acting as consumers) read and process these events, with the goal of react against them.

Although the information is gathered from the system itself, the processing phase is not carried out inside it. Once the information is extracted, there exists some components which are in charge of sending that information, using a secure channel, to the Microsoft backend server where all the analysis is finally performed.

There is not plenty documentation about the Telemetry component, and as we already know, Windows is not a open-source project, which makes the analysis of a native application or kernel module much harder. Although we can't read the source code of the component, we do have the executables files where all the logic is implemented.

In this project, we are going to reverse engineer a part of the Windows's kernel to better understand how Telemetry works from an internal perspective. In the process, we will also have to deal with not documented kernel internal structures, bigger frameworks (such as ETW), functions with not symbols exported, etc. Other types of analysis, such as the differences among the levels of Telemetry, analysis of the traffic going to the Microsoft servers will be performed as well. This work will make windows analysts, IT admins or even windows users, more aware about the functionality of the Telemetry component.

Previous works on the same topic, were based on either online documentation or just in the analysis of the traffic sent to Microsoft.

Check:
https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ICSE-logging-submisson.pdf


