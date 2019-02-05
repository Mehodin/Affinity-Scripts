import client

class player():
    def __init__(self):
        self.setAttributeFunctions = {
            'angles':self.__setAngles,
            'clantag': self.__setClantag
        }

    def __setattr__(self, attribute, value):
        """
        Overloaded set attribute function to work with Affinity, assuming everything will be functions.
        """
        if attribute.lower() in self.setAttributeFunctions:
            try:
                self.setAttributeFunctions[attribute.lower()](value)
            except:
                raise ValueError(f"Failed to change attribute {attribute} to {value}, due to the function not being defined in 'self.setAttributeFunctions'")
            return
        self.__dict__[attribute.lower()] = value
        
    def __setAngles(self, angles: tuple, *args, **kwargs):
        """
        Set angle function.
        Takes `angles` which is a tuple consisting of 3 values.
        index 0 = pitch, index 1 = yaw, index 2 = roll
        """
        client.set_angles(angles[0], angles[1], angles[2])

    def __setClantag(self, clantag: str, *args, **kwargs):
        """
        Set clantag function.
        Takes `clantag` which is a string.
        """
        client.set_clantag(clantag)
