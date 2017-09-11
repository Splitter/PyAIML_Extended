import abc


class BasePlugin(object):  
    metaclass=abc.ABCMeta
    """Base class for all response plugins

        Attributes:
            settings (list): list of dicitonaries that represent each setting for plugin

    """
    @abc.abstractmethod
    def getResponse(self, args):
        """called when an AIML pattern from .aiml file matches and redirects responseController to run corresponding plugin
        
            args:
                args(string): string argument passed from AIML file to plugin script
            
            returns:
                a string of the next response to end user    
        """
        return ""
