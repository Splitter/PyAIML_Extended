# PyAIML_Extended
## [PyAIML](https://pypi.python.org/pypi/PyAIML) with added \<plugin\> tag to implement simple plugin system, as well as added support for the caret(^) tag(0 or more wildcard match).

The new \<plugin\> tag functions almost exactly as the \<template\> tag with the added ability for response to be sent to a custom python plugin before final response is returned.

## Usage:

### Example AIML file...
(SideNote: All plugins must contain AIML files.)

* Every \<plugin\> tag must have a 'name' attribute corresponding to the plugins Python Class name
```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml>
    <category>
        <pattern>WHO IS THE REAL IRON MAN</pattern>
        <plugin name="ironman">
            Data you want sent to plugin if pattern matched
        </plugin>
    </category>
</aiml>
```

And seeing that the \<plugin\> tag is similar in function to the \<template\> you could do something like this...
```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml>
    <category>
        <pattern>WHO IS THE REAL IRON MAN</pattern>
        <plugin name="ironman">
            Data you want sent to plugin if pattern matched
        </plugin>
    </category>   
    <category>
        <pattern>WHO IS IRON MAN</pattern>
        <template>
            <srai>WHO IS THE REAL IRON MAN</srai>
        </template>
    </category>
    <category>
        <pattern>DO YOU KNOW WHO IRON MAN REALLY IS</pattern>
        <template>
            <srai>WHO IS THE REAL IRON MAN</srai>
        </template>
    </category>

</aiml>
```
Or...
```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml>
    <category>
        <pattern>Weather forecast for *</pattern>
        <plugin name="weather">
            <star/>
        </plugin>
    </category>
</aiml>
```

### Example Python Plugin...
(SideNote: Not all plugins need python code, without it the plugin just adds a new AIML file to learn)

* Every Plugin must implement a 'getResponse' method that returns a string that will be the final response. There is a base class to inherit from to enforce this.
* The class name must correspond to the plugin name in AIML file
```python
from aiml import BasePlugin

class ironman(BasePlugin.BasePlugin):  
 
    def getResponse(self, args):
        return "Tony Stark is the Real Iron Man!!!"

```
 
### Plugin directory structure...

* Plugins should each be in individual directories
* Individual plugin directory names should correspond to plugin class name
* Individual plugin file names should correspond to plugin class name
* Plugins should be in a parent plugin directory(no naming enforement for parent directory)


```
   |-- Plugins/
        |-- ironman/
            |-- ironman.aiml
            |-- ironman.py   
```


### Loading the plugins and corresponding AIML files...
* After creating an AIML Kernel instance call the loadPlugins method passing in Path to the Plugins directory

```python
import aiml

bot = aiml.Kernel();
bot.loadPlugins("./Plugins");

while 1:
	print bot.respond(raw_input('> '))

```




