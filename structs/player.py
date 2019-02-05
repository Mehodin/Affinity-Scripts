import client

class player():
    def __init__(self):
        self.setAttributeFunctions = {
            #
            # Dictionary which holds all the functions to be called using the overloaded __setattr__ function.
            #
            'angles': self.__setAngles,
            'clantag': self.__setClantag,
        }
        
        self.getAttributeFunctions = {
            #
            # Dictionary which holds all the functions to be called using the overloaded __getattr__ function.
            #
            'index': self.__getIndex
        }


        self.__dict__ = self.setAttributeFunctions # Overloading __dict__ member.

    def __setattr__(self, attribute, value):
        """
        Overloaded set attribute function to work with Affinity, assuming everything will be functions.
        """
        if attribute.lower() in self.setAttributeFunctions:
            try:
                self.setAttributeFunctions[attribute.lower()](value)
            except KeyError:
                raise ValueError(f"Failed to change attribute {attribute} to {value}, due to the function not being defined in 'self.setAttributeFunctions'")
            return
        self.__dict__[attribute.lower()] = value

    def __getattr__(self, attribute):
        """
        Overloaded get attribute function to work with Affinity, assuming everything will be functions.
        """
        if attribute.lower() in self.setAttributeFunctions:
            try:
                self.getAttributeFunctions[attribute.lower()]()
            except KeyError:
                raise ValueError(f"Failed to get attribute {attribute}, due to the function not being defined in 'self.getAttributeFunctions'")
            return
        return self.__dict[attribute.lower()]

    def __iter__(self):
        raise NotImplementedError("Not yet implemented")

    def __dict__(self):
        return self.setAttributeFunctions

    def __setAngles(self, angles: tuple, *args, **kwargs):
        """
        Set angle function.
        Takes `angles` which is a tuple consisting of 3 values.
        index 0 = pitch, index 1 = yaw, index 2 = roll
        """
        return client.set_angles(angles[0], angles[1], angles[2])

    def __setClantag(self, clantag: str, *args, **kwargs):
        """
        Set clantag function.
        Takes `clantag` which is a string.
        """
        return client.set_clantag(clantag)

    def __getIndex(self, clantag: str, *args, **kwargs):
        """
        Returns index of current entity.
        """
        for entity in client.get_entities():
            if entity.name == self.name:
                return entity.index
        return