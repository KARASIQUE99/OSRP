from src.common.objects.enums.ChemicalElement import ChemicalElement

ce_path = "common//objects//particles//data//elements"


class Atom:
    name = ""
    symbol = None
    number = 0
    configuration = ""
    atomic_weight = 0

    def __parse(self, filename):
        with open(filename) as description:
            lines = description.readlines()
            for line in lines:
                if line.startswith("name"):
                    self.name = line.split('=')[1].replace("\n", "")
                if line.startswith("symbol"):
                    self.symbol = line.split('=')[1].replace("\n", "")
                if line.startswith("number"):
                    self.number = int(line.split('=')[1].replace("\n", ""))
                if line.startswith("number"):
                    self.atomic_weight = int(line.split('=')[1].replace("\n", ""))
                if line.startswith("configuration"):
                    self.configuration = line.split('=')[1].replace("\n", "")

    def __init__(self, element):
        if isinstance(element, ChemicalElement):
            if element == ChemicalElement.H:
                self.__parse(ce_path + "//s-elements//hydrogen.ce")
            elif element == ChemicalElement.He:
                self.__parse(ce_path + "//s-elements//helium.ce")
            elif element == ChemicalElement.Li:
                self.__parse(ce_path + "//s-elements//lithium.ce")
            elif element == ChemicalElement.Be:
                self.__parse(ce_path + "//s-elements//berilium.ce")
            elif element == ChemicalElement.B:
                self.__parse(ce_path + "//p-elements//borum.ce")
            elif element == ChemicalElement.C:
                self.__parse(ce_path + "//p-elements//carbon.ce")
            elif element == ChemicalElement.N:
                self.__parse(ce_path + "//p-elements//nitrogen.ce")
            elif element == ChemicalElement.O:
                self.__parse(ce_path + "//p-elements//oxygen.ce")
            elif element == ChemicalElement.F:
                self.__parse(ce_path + "//p-elements//fluorine.ce")
            elif element == ChemicalElement.Ne:
                self.__parse(ce_path + "//p-elements//neon.ce")
            elif element == ChemicalElement.Na:
                self.__parse(ce_path + "//s-elements//sodium.ce")
            elif element == ChemicalElement.Mg:
                self.__parse(ce_path + "//s-elements//magnesium.ce")
            elif element == ChemicalElement.Al:
                self.__parse(ce_path + "//p-elements//aluminum.ce")
            elif element == ChemicalElement.Si:
                self.__parse(ce_path + "//p-elements//silicon.ce")
            elif element == ChemicalElement.P:
                self.__parse(ce_path + "//p-elements//phosphorus.ce")
            elif element == ChemicalElement.S:
                self.__parse(ce_path + "//p-elements//sulfur.ce")
            elif element == ChemicalElement.Cl:
                self.__parse(ce_path + "//p-elements//chlorine.ce")
            elif element == ChemicalElement.Ar:
                self.__parse(ce_path + "//p-elements//argon.ce")
            elif element == ChemicalElement.K:
                self.__parse(ce_path + "//s-elements//potassium.ce")
            elif element == ChemicalElement.Ca:
                self.__parse(ce_path + "//s-elements//calcium.ce")
            elif element == ChemicalElement.Sc:
                self.__parse(ce_path + "//d-elements//scandium.ce")
            elif element == ChemicalElement.Ti:
                self.__parse(ce_path + "//d-elements//titanium.ce")
            elif element == ChemicalElement.V:
                self.__parse(ce_path + "//d-elements//vanadium.ce")
            elif element == ChemicalElement.Cr:
                self.__parse(ce_path + "//d-elements//chromium.ce")
            elif element == ChemicalElement.Mn:
                self.__parse(ce_path + "//d-elements//manganese.ce")
            elif element == ChemicalElement.Fe:
                self.__parse(ce_path + "//d-elements//iron.ce")
            elif element == ChemicalElement.Co:
                self.__parse(ce_path + "//d-elements//cobaltum.ce")
            elif element == ChemicalElement.Ni:
                self.__parse(ce_path + "//d-elements//nickel.ce")
            elif element == ChemicalElement.Cu:
                self.__parse(ce_path + "//d-elements//copper.ce")
            elif element == ChemicalElement.Zn:
                self.__parse(ce_path + "//d-elements//zinc.ce")
            elif element == ChemicalElement.Ga:
                self.__parse(ce_path + "//p-elements//gallium.ce")
            elif element == ChemicalElement.Ge:
                self.__parse(ce_path + "//p-elements//germanium.ce")
            elif element == ChemicalElement.As:
                self.__parse(ce_path + "//p-elements//arsenic.ce")
            elif element == ChemicalElement.Se:
                self.__parse(ce_path + "//p-elements//selenium.ce")
            elif element == ChemicalElement.Br:
                self.__parse(ce_path + "//p-elements//bromine.ce")
            elif element == ChemicalElement.Kr:
                self.__parse(ce_path + "//p-elements//krypton.ce")
            elif element == ChemicalElement.Rb:
                self.__parse(ce_path + "//s-elements//rubidium.ce")
            elif element == ChemicalElement.Sr:
                self.__parse(ce_path + "//s-elements//strontium.ce")
            elif element == ChemicalElement.Y:
                self.__parse(ce_path + "//d-elements//yttrium.ce")
            elif element == ChemicalElement.Zr:
                self.__parse(ce_path + "//d-elements//zirconium.ce")
            elif element == ChemicalElement.Nb:
                self.__parse(ce_path + "//d-elements//niobium.ce")
            elif element == ChemicalElement.Mo:
                self.__parse(ce_path + "//d-elements//molybdenum.ce")
            elif element == ChemicalElement.Tc:
                self.__parse(ce_path + "//d-elements//technetium.ce")
            elif element == ChemicalElement.Ru:
                self.__parse(ce_path + "//d-elements//ruthenium.ce")
            elif element == ChemicalElement.Ro:
                self.__parse(ce_path + "//d-elements//rhodium.ce")
            elif element == ChemicalElement.Pd:
                self.__parse(ce_path + "//d-elements//palladium.ce")
            elif element == ChemicalElement.Ag:
                self.__parse(ce_path + "//d-elements//silver.ce")
            elif element == ChemicalElement.Cd:
                self.__parse(ce_path + "//d-elements//cadmium.ce")
            elif element == ChemicalElement.In:
                self.__parse(ce_path + "//p-elements//indium.ce")
            elif element == ChemicalElement.Sn:
                self.__parse(ce_path + "//p-elements//tin.ce")
            elif element == ChemicalElement.Sb:
                self.__parse(ce_path + "//p-elements//antimony.ce")
            elif element == ChemicalElement.Te:
                self.__parse(ce_path + "//p-elements//tellurium.ce")
            elif element == ChemicalElement.I:
                self.__parse(ce_path + "//p-elements//iodine.ce")
            elif element == ChemicalElement.Xe:
                self.__parse(ce_path + "//p-elements//xenon.ce")
            elif element == ChemicalElement.Cs:
                self.__parse(ce_path + "//s-elements//caesium.ce")
            elif element == ChemicalElement.Ba:
                self.__parse(ce_path + "//s-elements//barium.ce")
            elif element == ChemicalElement.La:
                self.__parse(ce_path + "//f-elements//lanthanum.ce")
            elif element == ChemicalElement.Ce:
                self.__parse(ce_path + "//f-elements//cerium.ce")
            elif element == ChemicalElement.Pr:
                self.__parse(ce_path + "//f-elements//praseodymium.ce")
            elif element == ChemicalElement.Nd:
                self.__parse(ce_path + "//f-elements//neodymium.ce")
            elif element == ChemicalElement.Pm:
                self.__parse(ce_path + "//f-elements//promethium.ce")
            elif element == ChemicalElement.Sm:
                self.__parse(ce_path + "//f-elements//samarium.ce")
            elif element == ChemicalElement.Eu:
                self.__parse(ce_path + "//f-elements//europium.ce")
            elif element == ChemicalElement.Gd:
                self.__parse(ce_path + "//f-elements//gadolinium.ce")
            elif element == ChemicalElement.Tb:
                self.__parse(ce_path + "//f-elements//terbium.ce")
            elif element == ChemicalElement.Dy:
                self.__parse(ce_path + "//f-elements//dysprosium.ce")
            elif element == ChemicalElement.Ho:
                self.__parse(ce_path + "//f-elements//holmium.ce")
            elif element == ChemicalElement.Er:
                self.__parse(ce_path + "//f-elements//erbium.ce")
            elif element == ChemicalElement.Tm:
                self.__parse(ce_path + "//f-elements//thulium.ce")
            elif element == ChemicalElement.Yb:
                self.__parse(ce_path + "//f-elements//ytterbium.ce")
            elif element == ChemicalElement.Lu:
                self.__parse(ce_path + "//d-elements//lutetium.ce")
            elif element == ChemicalElement.Hf:
                self.__parse(ce_path + "//d-elements//hafnium.ce")
            elif element == ChemicalElement.Ta:
                self.__parse(ce_path + "//d-elements//tantalum.ce")
            elif element == ChemicalElement.W:
                self.__parse(ce_path + "//d-elements//tungsten.ce")
            elif element == ChemicalElement.Re:
                self.__parse(ce_path + "//d-elements//rhenium.ce")
            elif element == ChemicalElement.Os:
                self.__parse(ce_path + "//d-elements//osmium.ce")
            elif element == ChemicalElement.Ir:
                self.__parse(ce_path + "//d-elements//iridium.ce")
            elif element == ChemicalElement.Pt:
                self.__parse(ce_path + "//d-elements//platinum.ce")
            elif element == ChemicalElement.Au:
                self.__parse(ce_path + "//d-elements//gold.ce")
            elif element == ChemicalElement.Hg:
                self.__parse(ce_path + "//d-elements//mercury.ce")
            elif element == ChemicalElement.Tl:
                self.__parse(ce_path + "//p-elements//thallium.ce")
            elif element == ChemicalElement.Pb:
                self.__parse(ce_path + "//p-elements//lead.ce")
            elif element == ChemicalElement.Bi:
                self.__parse(ce_path + "//p-elements//bismuth.ce")
            elif element == ChemicalElement.Po:
                self.__parse(ce_path + "//p-elements//polonium.ce")
            elif element == ChemicalElement.At:
                self.__parse(ce_path + "//p-elements//astatine.ce")
            elif element == ChemicalElement.Rn:
                self.__parse(ce_path + "//p-elements//radon.ce")
            elif element == ChemicalElement.Fr:
                self.__parse(ce_path + "//s-elements//francium.ce")
            elif element == ChemicalElement.Ra:
                self.__parse(ce_path + "//s-elements//radium.ce")
            elif element == ChemicalElement.Ac:
                self.__parse(ce_path + "//f-elements//actinium.ce")
            elif element == ChemicalElement.Th:
                self.__parse(ce_path + "//f-elements//thorium.ce")
            elif element == ChemicalElement.Pa:
                self.__parse(ce_path + "//f-elements//protactinium.ce")
            elif element == ChemicalElement.U:
                self.__parse(ce_path + "//f-elements//uranium.ce")
            elif element == ChemicalElement.Ne:
                self.__parse(ce_path + "//f-elements//neptunium.ce")
            elif element == ChemicalElement.Pu:
                self.__parse(ce_path + "//f-elements//plutonium.ce")
            elif element == ChemicalElement.Am:
                self.__parse(ce_path + "//f-elements//americium.ce")
            elif element == ChemicalElement.Cm:
                self.__parse(ce_path + "//f-elements//curium.ce")
            elif element == ChemicalElement.Bk:
                self.__parse(ce_path + "//f-elements//berkelium.ce")
            elif element == ChemicalElement.Cf:
                self.__parse(ce_path + "//f-elements//californium.ce")
            elif element == ChemicalElement.Es:
                self.__parse(ce_path + "//f-elements//einsteinium.ce")
            elif element == ChemicalElement.Fm:
                self.__parse(ce_path + "//f-elements//fermium.ce")
            elif element == ChemicalElement.Md:
                self.__parse(ce_path + "//f-elements//mendelevium.ce")
            elif element == ChemicalElement.No:
                self.__parse(ce_path + "//f-elements//nobelium.ce")
            elif element == ChemicalElement.Lr:
                self.__parse(ce_path + "//d-elements//lawrencium.ce")
            elif element == ChemicalElement.Rf:
                self.__parse(ce_path + "//d-elements//rutherfordium.ce")
            elif element == ChemicalElement.Db:
                self.__parse(ce_path + "//d-elements//dubnium.ce")
            elif element == ChemicalElement.Sg:
                self.__parse(ce_path + "//d-elements//seaborgium.ce")
            elif element == ChemicalElement.Bh:
                self.__parse(ce_path + "//d-elements//bohrium.ce")
            elif element == ChemicalElement.Hs:
                self.__parse(ce_path + "//d-elements//hassium.ce")
            elif element == ChemicalElement.Mt:
                self.__parse(ce_path + "//d-elements//meitnerium.ce")
            elif element == ChemicalElement.Ds:
                self.__parse(ce_path + "//d-elements//darmstadtium.ce")
            elif element == ChemicalElement.Rg:
                self.__parse(ce_path + "//d-elements//roenthgenium.ce")
            elif element == ChemicalElement.Cn:
                self.__parse(ce_path + "//d-elements//copernicium.ce")
            elif element == ChemicalElement.Nh:
                self.__parse(ce_path + "//d-elements//nihonium.ce")
            elif element == ChemicalElement.Fl:
                self.__parse(ce_path + "//d-elements//flerovium.ce")
            elif element == ChemicalElement.Mc:
                self.__parse(ce_path + "//d-elements//moscovium.ce")
            elif element == ChemicalElement.Lv:
                self.__parse(ce_path + "//d-elements//livermorium.ce")
            elif element == ChemicalElement.Ts:
                self.__parse(ce_path + "//d-elements//tennessine.ce")
            elif element == ChemicalElement.Og:
                self.__parse(ce_path + "//d-elements//oganesson.ce")

        else:
            raise ValueError("Given argument is not a ChemicalElement enum")
