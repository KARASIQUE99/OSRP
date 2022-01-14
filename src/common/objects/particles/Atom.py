from src.common.objects.enums.ChemicalElement import ChemicalElement


class Atom:
    def __init__(self, element, isotope = None):
        if element is ChemicalElement:
            if element == ChemicalElement.H:
                pass
            if element == ChemicalElement.He:
                pass
        else:
            raise ValueError("Given argument is not a ChemicalElement enum")
