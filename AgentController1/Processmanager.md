Processmanager
==============


The processmanager is the main thread of the controller. It's where synchronized tasks run and 

By default we have 3 different kind of queues.

-   **default**: We have two workers listening on the default queue doing
    all kinds of miscellaneous tasks
-   **io**: There is one IO queue which is typical used for backup/restore
    and long IO bound related work.
-   **hypervisor**: There is one Hypervisor queue which takes on tasks
    related to VM management.

