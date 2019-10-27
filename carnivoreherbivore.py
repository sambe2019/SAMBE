class carnivore:
    def __init__(self,p):
        self._poidsViande = p
    def devorer(self):
        print("Je mange ",self._poidsViande,"kilogs de steack par jour")



class herbivore:
    def __init__(self,p):
        self._poidsHerbe = p
    def brouter(self):
        print("Je mange ",self._poidsHerbe,"kilogs de gazon par jour")


class omnivore(carnivore,herbivore):
    def __init__(self,pv,ph,h):
        carnivore.__init__(self,pv)
        herbivore.__init__(self,ph)
        self.__humain = h
teddy = omnivore(10,5,False)
teddy.devorer()
teddy.brouter()
print("fin")
