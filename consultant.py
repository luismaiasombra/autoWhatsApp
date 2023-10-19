

import sqlite3


class Consultant:
    consultants = []
    rewarded = {}
    LEVELS = [5500,2200,900,300]
    LEVEL_TITLES = {}
    LEVEL_TITLES[5500]="Diamante"
    LEVEL_TITLES[2200]="Ouro"
    LEVEL_TITLES[900]="Prata"
    LEVEL_TITLES[300]="Bronze"
    #def reward(self,LEVELS=LEVELS,rewarded=rewarded,LEVEL_TITLES=LEVEL_TITLES):

    def reward(self,LEVELS=LEVELS,rewarded={},LEVEL_TITLES=LEVEL_TITLES):
        #let's just override rewarded so that nothing changes
        rewarded['Diamante'] = self.won_diamond
        rewarded['Prata'] = self.won_silver
        rewarded['Ouro'] = self.won_gold
        rewarded['Bronze'] = self.won_copper
        for i in LEVELS:
            try:
                if int(self.points) >= i:
                    if rewarded[self.level] != True:
                        rewarded[self.level] = True
                        print(f"{self.name}, you are now a {LEVEL_TITLES[i]}")
                        self.level = LEVEL_TITLES[i]
                        return rewarded
            except Exception as er:
                #I don't know why I'm getting self.level == None in the end
                pass

                

    def __init__(self, row):
        self.code = row[0].value
        self.name = row[1].value
        self.phone = row[2].value
        self.level = row[3].value
        self.status = row[4].value #current situation of the consultant
        self.debit_status = row[5].value
        self.perks =  row[6].value
        self.points = row[7].value
        self.points_to_copper = row[8].value
        self.won_copper = False
        self.points_to_silver = row[9].value
        self.won_silver = False
        self.points_to_gold = row[10].value
        self.won_gold = False
        self.won_silver = False
        self.points_to_diamond = row[11].value #if you reach 0, reachedCopper becaomes false
        self.won_diamond = False
        self.add_tuple_to_db()
        print('Tuple loaded')
        Consultant.rewarded[self.level] = False
        Consultant.consultants.append(self)
        
    def add_tuple_to_db(self, db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO consultants 
            (code, name, phone, level, status, debit_status, perks, points, points_to_copper, points_to_silver, points_to_gold, points_to_diamond, won_copper, won_silver, won_gold, won_diamond)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.code, self.name, self.phone, self.level, self.status, self.debit_status, self.perks, self.points, self.points_to_copper, self.points_to_silver, self.points_to_gold, self.points_to_diamond, self.won_copper, self.won_silver, self.won_gold, self.won_diamond))
        conn.commit()
        conn.close()

    def set_level(self):
        pass
    @classmethod
    def print_all(cls):
        for consultant in cls.consultants:
            print("Code:", consultant.code)
            print("Name:", consultant.name)
            print("Phone:", consultant.phone)
            print("Level:", consultant.level)
            print("Status:", consultant.status)
            print("Debit Status:", consultant.debit_status)
            print("Perks:", consultant.perks)
            print("Points:", consultant.points)
            print("Points to Copper:", consultant.points_to_copper)
            print("Points to Silver:", consultant.points_to_silver)
            print("Points to Gold:", consultant.points_to_gold)
            print("Points to Diamond:", consultant.points_to_diamond)
            print("\n")










