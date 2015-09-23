#coding :UTF-8
'''
Created on 2015-9-16

@author: sun
'''
import random
from xml.dom import minidom
class Data_IO(object):
    def create_savedata(self,Hero):
        doc = minidom.Document()
        game = doc.createElement("game")
        doc.appendChild(game)
        hero = doc.createElement("hero")
        game.appendChild(hero)
        name = doc.createElement("name")
        hero.appendChild(name)
        hero_health = doc.createElement("health")
        hero_attack = doc.createElement("attack")
        hero_defence = doc.createElement("defence")
        hero_exp = doc.createElement("exp")
        name.setAttribute("heroname", Hero.name)
        name.appendChild(hero_health)
        name.appendChild(hero_attack)
        name.appendChild(hero_defence)
        name.appendChild(hero_exp)
        hnode = doc.createTextNode(str(Hero.health))
        anode = doc.createTextNode(str(Hero.attack))
        dnode = doc.createTextNode(str(Hero.defence))
        enode = doc.createTextNode(str(Hero.exp))
        hero_health.appendChild(hnode)
        hero_attack.appendChild(anode)
        hero_defence.appendChild(dnode)
        hero_exp.appendChild(enode)       
        f = open('savedata.xml','w')
        f.write(doc.toprettyxml(indent = '    '))
        f.close()
        
    def load_savedata(self,Hero):
        dom = minidom.parse("savedata.xml")
        root = dom.documentElement
        for node in dom.getElementsByTagName("name"):
            for item in node.childNodes:
                print item
            #print (node,node.tagName,node.getAttribute("heroname"))
        
class Instruction(object):
    def __call__(self):
        print "ok"

class Hero(object):
    def __init__(self,name = "monster", health = 35, attack = 10, defence = 12):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        self.exp = 0
        self.level = 1
        self.hg = self.ag = self.dg = self.lg = 0
        self.max_exp = 100
    
    def gain_exp(self):
        exp = random.randint(10,20)    
        self.exp += exp
        print "gain exp " + str(exp)
        print str(self.exp) + "/" + str(self.max_exp)
        self.check_level_up()
        
    def check_level_up(self):
        if self.exp >= self.max_exp:
            self.lg = self.exp / self.max_exp
            self.exp -= self.max_exp * self.lg
            self.level += self.lg
            self.level_up_message()
    
    def level_up_message(self):
        print self.name + " level up!!"
        print "level " + str(self.level) + "  ~ +" + str(self.lg)
            
    
class Event(object):
    def __init__(self):
        log = ""
    
    def exp_rand(self):
        if random.uniform(0,10) > 3:
            return True
    
    def battle(self,Hero,map = 0):
        print "have a battle!!"
        if random.uniform(0,10) > 4:
            print "win the battle!"
            Hero.gain_exp()
        else:
            print "lose the battle"
        return
    
    def explore(self,Hero):
        while True:
            try: act = raw_input("(explore:)").strip().lower().split()
            except EOFError:
                return
            if len(act) == 0 or act[0] == "":
                if self.exp_rand() == True:
                    self.battle(Hero)
                else:
                    print "nothing happens"
                
            elif act[0] == "home":
                print "back to home"
                return
            elif act[0] == "help":
                Instruction()
                
    
def main():
    hero = Hero(name = "vitamin")
    event = Event()
    dio = Data_IO()
    dio.load_savedata(hero)
    while True:
        try: ins = raw_input("(home:)").strip().lower().split()
        except EOFError:
            return
        if len(ins) == 0:
            continue
        if ins[0] == "quit":
            return;
        elif ins[0] == "save":
            dio.create_savedata(hero)
            return;
        elif ins[0] == "exp":
            event.explore(hero)
            
if __name__ == "__main__":
    main()
