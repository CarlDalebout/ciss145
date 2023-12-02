
import pygame, math, random, os, sys
from Globals import *

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, screen, name = "bolder", position = (0, 0), icon = ASTEROID_ICON):
        self.screen         = screen
        self.name           = name
        self.angle          = 0
        self.speed          = 2
        self.position       = position
        self.orig_icon      = icon
        self.icon           = pygame.transform.scale(self.orig_icon, (63, 63))
        self.rect           = self.icon.get_rect()
        self.rect.topleft   = self.position
        self.orig_icon      = self.icon

    def icon(self):
        return self.icon

    def rect(self):
        return self.rect
        
    def get_vec(self, pos_x, pos_y):
        vec_x = pos_x - self.rect.x
        vec_y = pos_y - self.rect.y
        normal_scaler = math.sqrt(pow(vec_x, 2) + pow(vec_y, 2))
        vec_x /= normal_scaler
        vec_y /= normal_scaler
        vec_x *= self.speed
        vec_y *= self.speed
        return vec_x, vec_y

    def update(self, pos_x, pos_y):
        x_offset, y_offset = self.get_vec(pos_x, pos_y)
        self.rect.x += x_offset
        self.rect.y += y_offset