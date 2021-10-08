import pygame
import random

pygame.init()

background_color = (0, 0, 0)
(width, height) = (600, 400)

class Wall:
    def __init__(self, x, y):
        self.position = (x, y)
        self.color = (255, 0, 0)

    def update(self, speed):
        self.position = (self.position[0] - speed, self.position[1])
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], 10, 1000))
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1] - 1100, 10, 1000))

class WallManager:
    def getRandHeight():
        return int(min(0.7, random.uniform(0, 1) + 0.3) * height)

    def __init__(self):
        self.speed = 5
        self.walls = []
        for i in range(6):
            self.walls += [Wall(width + 5 + i * 150, WallManager.getRandHeight())]
    
    def update(self):
        self.speed += 0.01
        for wall in self.walls:
            wall.update(self.speed)
            if wall.position[0] <= -5:
                furthest = 0
                for w in self.walls:
                    furthest = max(furthest, w.position[0])
                wall.position = (furthest + 150, WallManager.getRandHeight())

    def draw(self, screen):
        for wall in self.walls:
            wall.draw(screen)


class Bird:
    def __init__(self):
        self.position = (100, height//2)
        self.color = (255,255,255)
        self.radius = 10
        self.acceleration = 0
        self.speed = 5

    def update(self):
        self.acceleration = max(-3, self.acceleration - 1)
        y = self.position[1] - self.speed * self.acceleration
        y = max(min(height - self.radius, y), self.radius)
        self.position = (self.position[0], y)

    def jump(self):
        self.acceleration = min(8, self.acceleration + 4)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)


screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption('Flappy Bird')
screen.fill(background_color)

bird = Bird()
manager = WallManager()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        bird.jump()

  screen.fill(background_color)
  
  bird.update()
  manager.update()

  bird.draw(screen)
  manager.draw(screen)

  pygame.display.flip()

  for wall in manager.walls:
      if abs(bird.position[0] - wall.position[0]) <= 5:
          if bird.position[1] > wall.position[1] or bird.position[1] < wall.position[1] - 100:
              bird.speed = 0
              manager.speed = 0

  clock.tick(10)