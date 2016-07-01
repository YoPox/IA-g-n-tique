class Equip:

    def __init__(self, nom, cat=0, stats=[0, 0, 0, 0, 0, 0, 0], buffs=[]):
        self.nom = nom
        # 0 : WEAPON
        # 1 : ARMOR
        # 2 : SPELL
        self.cat = cat
        self.stats = stats
        self.buffs = buffs

    def genArme(self, type, credits):
        pass
