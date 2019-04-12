ETW is an efficient kernel-level tracing facility that lets you log kernel or application-defined eventos to a log file.

ETW lets you enable or disable event tracing dynamically, allowing you to perform detailed tracing in a production environment without requiring computer or application restarts.

The Event Tracing API is broken into three distinct components:

* **Controllers**: Start/Stop event  tracing sessions and enable providers.
* **Providers**: Who provides the events.
* **Consumers**: Who consumes the events.