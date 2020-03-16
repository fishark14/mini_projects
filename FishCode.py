#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Pokemon class

class Pokemon:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = level * 5
        self.health = level * 5
        self.is_KO = False
        
    def lose_health(self, pts):
        self.health -= pts
        if self.health <= 0:
            self.health = 0
            self.KO()
        else:
            print('{pokemon} now has {pts} health'.format(pokemon=self.name, pts=self.health))
        
    def restore_health(self, pts):
        self.health += pts
        if self.health >= self.max_health:
            self.health = self.max_health
        print('{pokemon} now has {pts} health.'.format(pokemon=self.name, pts=self.health))
        
    def KO(self):
        self.is_KO = True
        if self.health != 0:
            self.health = 0
        print('{pokemon} has fainted! ...'.format(pokemon=self.name))
        
    def revive(self):
        self.KO = False
        self.health = 1
        print('{pokemon} is revived!'.format(pokemon=self.name))
        
    def attack(self, target):
        
        if (self.type == 'Fire' and target.type == 'Grass') or (self.type == 'Grass' and target.type == 'Water') or (self.type == 'Water' and target.type == 'Fire'):
            damage = (self.level * 2)
            target.lose_health(damage)
            print('''{self} attacked {target}.
It was very effective!!
{target} received {damage} damage. {target} has {health} HP left.'''.format(self=self.name, target=target.name, damage=int(damage), health=int(target.health)))
            
        if (self.type == 'Grass' and target.type == 'Fire') or (self.type == 'Water' and target.type == 'Grass') or (self.type == 'Fire' and target.type == 'Water'):
            damage = (self.level * .5)
            target.lose_health(damage)
            print('''{self} attacked {target}.
It was not effective...
{target} received {damage} damage. {target} has {health} HP left.'''.format(self=self.name, target=target.name, damage=int(damage), health=int(target.health)))
            
        else:
            damage = self.level
            target.lose_health(damage)
            print('''{self} attacked {target}.
{target} received {damage} damage. {target} has {health} HP left.'''.format(self=self.name, target=target.name,\
                        damage=int(damage), health=int(target.health)))            


# In[24]:


# Trainer class

class Trainer:
    def __init__(self, name, pokemons, potions, main_pokemon):
        self.name = name
        self.pokemons = pokemons
        self.potions = potions
        self.main_pokemon = 0
        
    def __repr__(self):
        return """Name: {name}
Pokemons: {pokemons}
Main Pokemon: {main}
Potions Left: {potions}
""".format(name=self.name, main=self.pokemons[self.main_pokemon].name,pokemons = [i.name for i in self.pokemons],\
           potions=self.potions)
        
    def use_potion(self):
        if self.potions > 1:
            print('{trainer} used a potion on {pokemon}...'.
                  format(trainer=self.name,pokemon=self.pokemons[self.main_pokemon].name))
            self.pokemons[self.main_pokemon].restore_health(20)
            self.potions -= 1
        else:
            print('No more potions!')
        
    def attack(self, target_trainer):
        my_pokemon = self.pokemons[self.main_pokemon]
        their_pokemon = target_trainer.pokemons[target_trainer.main_pokemon]
        my_pokemon.attack(their_pokemon)
        
        if target_trainer.pokemons[target_trainer.main_pokemon].is_KO:
            print('{their_pokemon} has fainted...'.format(their_pokemon=their_pokemon.name))
            target_trainer.main_pokemon += 1
            next_pokemon = target_trainer.pokemons[target_trainer.main_pokemon].name
            print('{trainer} sends... {next_pokemon}. Go {next_pokemon}!'.format(trainer=target_trainer.name, next_pokemon=next_pokemon))
        
    def switch_main(self, pokemon_to_switch):
        print('{trainer}: "{pokemon}, time for a rest!"'.format(trainer = self.name,pokemon = self.pokemons[self.main_pokemon].name))
        self.main_pokemon = pokemon_to_switch
        print('{trainer}:"{pokemon}, i choose you!"'.format(trainer = self.name,pokemon = self.pokemons[self.main_pokemon].name))

