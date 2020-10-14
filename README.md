# Custom Logs File generator for LOGS HUB Python 3

### Installation

- pip install LogsHub
- copy .env to root directory of the project or if you have .env file already copy content of the file (new variables in the .env)

### Available functions 
We have 4 types of logs:
 - warning
 - error
 - critical
 - info

### Function Parameters
For each function we have five parameters three of them are required and the others are optional
 - message (*)
 - application (*)
 - execution_level (*)
 - user_id
 - extra_data



### Usage & Examples
import LogsHub

- LogsHub.warning("message","application_name",300,3,{"key":"value"});
- LogsHub.error("MESSAGE","NEWS",30);
- LogsHub.info("MESSAGE","NEWS");
- LogsHub.critical("MESSAGE","NEWS",0,None,{"key":"value"});


License
----
Odai Atef
**Free to use**