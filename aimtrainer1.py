import pygame
import random

pygame.init()

# Färger
vit = (255, 255, 255)
svart = (0, 0, 0)
röd = (255, 0, 0)
grön = (0, 255, 0)

# Skärminställningar
bred = 800
höjd = 600

# Skapar skärmen
skärm = pygame.display.set_mode((bred, höjd))
pygame.display.set_caption("Aim Trainer")

# tiden och start poäng
klocka = pygame.time.Clock()
poäng = 0
objektRäknare = 0

# Huvudklass
class Target(pygame.sprite.Sprite):
    def __init__(self, x, y, färg):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(färg)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# underklass måltavlor för huvudklass Target
class Bullseye(Target):
    def __init__(self, x, y):
        super().__init__(x, y, grön)

    def update(self):
        self.rect.x += random.randint(-5, 5)
        self.rect.y += random.randint(-5, 5)


# underklass Bomber för huvudklass Target
class Bomb(Target):
    def __init__(self, x, y):
        super().__init__(x, y, röd)

    def update(self):
        self.rect.x += random.randint(-2, 2)
        self.rect.y += random.randint(-2, 2)


# Gör en grupp för targets och där skapar hur många bomber och bullseyes som skapas
targets = pygame.sprite.Group()


for objekt in range(20):
    x = random.randint(60, bred - 60)
    y = random.randint(60, höjd - 60)
    if objekt % 4 == 0:
        targets.add(Bomb(x, y))
        objektRäknare += 1
    else:
        targets.add(Bullseye(x, y))
        objektRäknare += 1



# funktion för att se poäng på skärmen
def visa_poäng(skärm, Poäng):
    font = pygame.font.SysFont("arial", 24)
    Poäng_text = font.render("Poäng: " + str(Poäng), True, svart)
    skärm.blit(Poäng_text, (10, 10))


# Spelets loop
running = True
while running:
    # Hanterar om spellet är igång eller inte
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Titar om det blir en träf när man trycker på ett obejekt
            for target in targets:
                if target.rect.collidepoint(event.pos):
                    # Gör så du får -poäng för bomber och +poäng för måltavla
                    if isinstance(target, Bomb):
                        poäng -= 1
                        objektRäknare -= 1
                    if isinstance(target, Bullseye):
                        poäng += 1
                        objektRäknare -= 1
                    # Gör så att targets försviner när dom trycks på
                    target.kill()

    # Gör skärmens bakrund vit
    skärm.fill(vit)

    # Sätter in targets på skärmen
    targets.draw(skärm)

    # Tar och uppdaterar posistionen ifrån funkstionen update
    targets.update()

    # Visar poängen på skärmen
    visa_poäng(skärm, poäng)

    # Uppdaterar skärmen
    pygame.display.update()

    # Bestämer spelets FPS
    klocka.tick(20)

    # avslutar spelet
    if objektRäknare == 10:
        pygame.quit()
