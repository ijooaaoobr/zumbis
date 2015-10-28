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
    pass
   
class Zombie2(Zombie):
    move_rate = 8

class Estrelas(Actor):
    pass

class Jogador(Hero):
    pass
    
class Ceu(GameObject):
    hardness = 5


def main():
    scene = Scene("scene0")
    simpleloop(scene, (800, 600),)


main()
