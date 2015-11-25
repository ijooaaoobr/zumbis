# coding: utf-8

import sys, os
sys.path.append(os.getcwd() + "/mapengine/")

from mapengine import Scene, simpleloop

from mapengine.base import Actor, Hero, GameObject, Event, Directions


class Zombie(Actor):
    move_rate = 14
    poder = 1
    def update(self):
        if not self.tick % self.move_rate:
            self.move((-1, 0))
            if self.pos[0] < 0:
                self.kill()
        super(Zombie, self).update()

        if self.pos[0] < 0:
            try:
                jogador = self.controller.main_character.sprites()[0]
            except (AttributeError, IndexError):
                return
            jogador.vida -= self.poder
            print ("Zumbi escapou - você perdeu {} de vida. Vida: {}".format(self.poder, jogador.vida))
                  
        
    def on_over(self, outro):
         if isinstance(outro, Jogador):
              outro.tirarvida()
              self.kill()
              
         elif isinstance(outro, Tiro):
              self.kill()
              outro.kill()


             
class Zombie1(Zombie):
    pass
              
class Zombie2(Zombie):
    poder = 1
    pass

class Estrelas(Actor):
    def on_over(self, other):
        if isinstance(other, Jogador):
            self.kill()
            other.vida += 3
            print ("Voce ganhou 3 de vida")
            
class Chaofase2(GameObject):
    def on_touch(self, other):
       cena = Scene("fase2")
       self.controller.load_scene(cena)
       self.controller.force_redraw = True

class Zumbi(Zombie):
    pass

class ZumbiForte(Zombie):
    poder = 5
    pass
    
class Tiro(Actor):
    move_rate = 1
    direction = None
    def update(self):
        self.move(self.direction) 
        super(Tiro, self).update()  
        if not self.controller.is_position_on_screen(self.pos):
            self.kill()

class Agua(GameObject):
    def on_over(self, other):
        if isinstance(other, Jogador):
            other.kill()

class Jogador(Hero):
    firetick = 0
    fire_rate = 20
    vida = 20
    margin = 5
    horizontal_move_direction = Directions.RIGHT
    def on_fire(self):
        if self.tick - self.firetick < self.fire_rate:
             return
        self.firetick = self.tick
        pos = self.pos + self.horizontal_move_direction
        tiro = Tiro(self.controller, pos)
        tiro.direction = self.horizontal_move_direction
        self.controller.all_actors.add(tiro)
        # self.controller.actors["tiro"].add(tiro)
       
    def move(self, direction):
        scene = self.controller.scene
        if (direction[0] == 1 and self.pos[0] >= scene.width - 1 or 
            direction[0] == -1 and self.pos[0] <= 0 or
            direction[1] == 1 and self.pos[1] >= scene.height - 1 or 
            direction[1] == -1 and self.pos[1] <= 0):
            return 
        result = super(Jogador, self).move(direction)
        if self.move_direction in (Directions.LEFT, Directions.RIGHT):
            self.horizontal_move_direction = self.move_direction
    
    def update(self):
        super(Jogador, self).update()
        if self.vida <= 0:
            self.kill()
            
    def tirarvida(self):
        self.vida -= 5 
        print ("Zumbi Te acertou - você perdeu 5 de vida. Vida: {}".format(self.vida))             
    
   
class Ceu(GameObject):
    hardness = 5

class Madeirafinal(GameObject):
    def on_over(self, other):
        if isinstance(other, Jogador):
            other.show_text(u"Achei a Saída", duration=3)
            other.events.add(Event(30, self.fim, None))
    def  fim(self):
        import pygame, sys
        
        pygame.quit()
        print("Parabens, voce ganhou!!!\n")
        sys.exit(0)


def main():
    scene = Scene("scene0",)
    scene.margin = 0
    scene.window_height = 9
    # scene.window_width = 9
    simpleloop(scene, (800, 400),)


main()
