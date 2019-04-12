# Work Plan

**Ultimate deadline: 23.09.2018**

1. Analyze and generate workloads for relevant ETW providers that are triggered spontaneously. **Deadline: 15.06.2018**
    * **Analysis**
        * Monitor the system and extract analysis info (automate!)
            * __Requirement:__ Production-ready software will be needed!
            * __Requirement:__ The software needs to run on Windows without installing additional software (as much as possible)
            * __Requirement:__ Dumped data at kernel-level needs to be compared against data at network-level (implementation of conversion software possible)

        * Determine origin of Telemetry data and how it can be triggered (conditions, theoretically both in user- and kernel-stacks)
            * Reason: The triggered Telemetry data needs always to be native!
    * **Generating workloads**
        * Develop executables (scripts, .exes, whatever) that trigger the Telemetry data (ETW writes) analyzed above
            * One executable per trigger!
            * Start with at least 3 workload triggers and develop more based on time estimation


2. Analyze and generate workloads for relevant ETW providers that are not triggered spontaneously. (e.g., the Security-level providers)  **Deadline: 16.06.2018 - 16.08.2018**
    * **Analysis**
        * Identify when writes to the ETW providers takes place (!) and extract analysis info (automate!)
            * __Requirement:__ We focus on Security-level ETW providers
            * __Requirement:__ Production-ready software will be needed!
            * __Requirement:__ The software needs to run on Windows without installing additional software (as much as possible)

        * Determine origin of Telemetry data and how it can be triggered (conditions, theoretically both in user- and kernel-stacks)
            * Reason: The triggered Telemetry data needs always to be native!
    * **Generating workloads**
        * Develop executables (scripts, .exes, whatever) that trigger the Telemetry data (ETW writes) analyzed above
            * One executable per trigger!
            * Try to cover all Security-level ETW providers with workload generators

3. Develop a meta-language to control the execution of workload triggers (central workload trigger that manages all individual workload triggers)  **Deadline: 17.08.2018 - 10.09.2018**

4. Software verification and improvement (production-ready)  **Deadline: 11.09.2018 - 29.09.2018**