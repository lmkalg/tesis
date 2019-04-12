Applications that contain event tracing instrumentation. After a **provider** registers itself, a **controller** can either enable or disable event tracing in the **provider**.
**The provider defines its interpretation of being enabled or disabled**.

Generally speaking, an enabled **provider** generates events, while a disabled one doesn't.

**Controllers** & **providers** are usually shown as separate entities, but an application can include both of them.

#### Types

All providers fundamentally use the Event Tracing family of API's (**TraceEvent** for legacy technologies **EventWrite**/**EventWriteEx** for newer ones)

##### MOF (Classic)

* They use MOF classes to define events so consumers know who to consume them.
* **TraceEvent** / **RegisterTraceGuids**

##### WPP

* Have TMF files associated (compiled as .pdb) containing decoding information inferred from the preprocessor's scan of WPP instrumentation in source code.
* **TraceEvent** / **RegisterTraceGuids**

##### Manifest-based 

* Use a manifest to inform how there events should be consumed.
* **EventRegister** / **EventWrite**

##### TraceLogging

* Self-describing events. 
* **TraceLoggingRegister** / **TraceLoggingWrite**

