# Producers & Consumers

- Each service instance can consume a service delivered by a producer
- A producer is another service instance delivering a service
- When installing you can specify the consumption you are doing by e.g. '-c mongodb!main' construct
    - Easier is to specify by means of role e.g. '-c $mongodb' will only work if not more than 1 found per node or global
