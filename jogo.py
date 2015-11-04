# coding: utf-8

import sys, os
sys.path.append(os.getcwd() + "/mapengine/")

from mapengine import Scene, simpleloop

from mapengine.base import Actor, Hero, GameObject

class Zombie(Actor):
    move_rate = 12

    def update(self):
        if not self.tick % self.move_rate:
            self.move((-1, 0))
            if self.pos[0] < 0:
                self.kill()
        super(Zombie, self).update()
   
    def on_over(self, outro):
         if isinstance(outro, Jogador):
              outro.kill()
     
class Zombie1(Zombie):
  
    def on_touch(self, other):
        if isinstance(outro, Tiro):
            self.kill()
              
class Zombie2(Zombie):
    pass

class Estrelas(Actor):
    pass

class Tiro(Actor):
    move_rate = 2
    def update(self):
        self.move((1, 0)) 
        super(Tiro, self).update()

class Jogador(Hero):
    def on_fire(self):
        pos = self.pos[0] + 1, self.pos[1]
        tiro = Tiro(self.controller, pos)
        self.controller.all_actors.add(tiro)
        # self.controller.actors["tiro"].add(tiro)
    
class Ceu(GameObject):
    hardness = 5


def main():
    scene = Scene("scene0",)
    simpleloop(scene, (800, 600),)


main()
