import pygame

# Initialization
pygame.init()

window_x = 1280
window_y = 748

screen = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('In Search of Blood')
pygame.display.set_icon(pygame.image.load('images/icons/icon.png').convert_alpha())
clock = pygame.time.Clock()
surface = pygame.Surface((window_x, window_y), pygame.SRCALPHA)


# Animations
walk_right = [
    pygame.image.load('images/ghost/walk/right/1.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/right/1 — копия.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/right/2.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/right/2 — копия.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/right/3.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/right/3 — копия.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/right/4.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/right/4 — копия.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/right/5.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/right/5 — копия.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/right/6.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/right/6 — копия.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/right/7.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/right/7 — копия.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/right/8.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/right/8 — копия.png').convert_alpha()
]
walk_left = [
    pygame.image.load('images/ghost/walk/left/1.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/left/1 — копия.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/left/2.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/left/2 — копия.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/left/3.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/left/3 — копия.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/left/4.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/left/4 — копия.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/left/5.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/left/5 — копия.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/left/6.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/left/6 — копия.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/left/7.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/left/7 — копия.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/left/8.png').convert_alpha(),
    pygame.image.load('images/ghost/walk/left/8 — копия.png').convert_alpha()
]
knifes_anim = [
    pygame.image.load('images/knife/knife1.png').convert_alpha(),
    pygame.image.load('images/knife/knife1 — копия.png').convert_alpha(),
    pygame.image.load('images/knife/knife2.png').convert_alpha(),
    pygame.image.load('images/knife/knife2 — копия.png').convert_alpha(),
    pygame.image.load('images/knife/knife3.png').convert_alpha(),
    pygame.image.load('images/knife/knife3 — копия.png').convert_alpha(),
    pygame.image.load('images/knife/knife4.png').convert_alpha(),
    pygame.image.load('images/knife/knife4 — копия.png').convert_alpha(),
]
eye_fly = [
    pygame.image.load('images/eye/eye1.png').convert_alpha(),
    pygame.image.load('images/eye/eye1 — копия.png').convert_alpha(),
    pygame.image.load('images/eye/eye1 — копия (2).png').convert_alpha(),
    pygame.image.load('images/eye/eye2.png').convert_alpha(),
    pygame.image.load('images/eye/eye2 — копия.png').convert_alpha(),
    pygame.image.load('images/eye/eye2 — копия (2).png').convert_alpha()
]


# Images
bg1 = pygame.image.load('images/bg/bg1.JPG').convert_alpha()
bg2 = pygame.image.load('images/bg/bg2.JPG').convert_alpha()
enemy = pygame.image.load('images/enemy/enemy.png').convert_alpha()
ghost_stand = pygame.image.load('images/ghost/ghost_stand.png').convert_alpha()

knife_bar_full = pygame.image.load('images/knife_bar/knife_bar_full.png').convert_alpha()
knife_bar_medium = pygame.image.load('images/knife_bar/knife_bar_medium.png').convert_alpha()
knife_bar_low = pygame.image.load('images/knife_bar/knife_bar_low.png').convert_alpha()
knife_bar_zero = pygame.image.load('images/knife_bar/knife_bar_zero.png').convert_alpha()

hp_full = pygame.image.load('images/hp/hp_full.png').convert_alpha()
hp_medium = pygame.image.load('images/hp/hp_medium.png').convert_alpha()
hp_low = pygame.image.load('images/hp/hp_low.png').convert_alpha()

heal_potion = pygame.image.load('images/potions/medical.png').convert_alpha()
heal_potion_empty = pygame.image.load('images/potions/medical_empty.png').convert_alpha()

shield_bar_full = pygame.image.load('images/shield/shield_full.png').convert_alpha()
shield_bar_good = pygame.image.load('images/shield/shield_good.png').convert_alpha()
shield_bar_medium = pygame.image.load('images/shield/shield_medium.png').convert_alpha()
shield_bar_low = pygame.image.load('images/shield/shield_low.png').convert_alpha()
shield_bar_zero = pygame.image.load('images/shield/shield_zero.png').convert_alpha()


# Variables
ghost_step = 0
ghost_speed = 20
ghost_x = 150
ghost_y = 540

knifes_step = 0
knifes_left = 3

jump_count = 8
health_points = 7
bg_x = 0

potion_x = -100
potion_y = -100

eye_step = 0


# Arrays and Tuples
enemy_list = []
eye_list = []
knifes = []

shield_bar_xy = [window_x - 329, 20]
hp_bar_xy = [window_x - 326, 70]
knifes_bar_xy = [window_x - 317, 120]
heal_potion_bar_xy = [window_x - 194, 105]


# Flags
is_jump = False
potion_flag = False
is_potion = False
gameplay = True
running = True
paused = False


# Sound
bg_sound = pygame.mixer.Sound('sounds/bg.mp3')
bg_sound.play(-1)


# Enemy Timer
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 4500)


# Restart Window
label = pygame.font.Font('fonts/RubikBurned-Regular.ttf', 80)
lose_label = label.render('Bro, you lose...', False, 'White')
restart_label = label.render('Click HERE to restart', False, (102, 157, 175))
restart_label_hitbox = restart_label.get_rect(topleft = (185, 400))


while running:
    mouse = (-100, -100)

    # Screen Emersion
    screen.blit(bg1, (bg_x, 0))
    screen.blit(bg2, (bg_x + window_x, 0))


    if gameplay:

        # Ghost Hitbox
        ghost_hitbox = walk_left[0].get_rect(topleft = (ghost_x, ghost_y))


        # Enemy Emersion
        if enemy_list:
            for i, el in enumerate(enemy_list):
                screen.blit(enemy, el)
                if not paused:
                    el.x -= 15

                if el.x < -10:
                    enemy_list.pop(i)

                if ghost_hitbox.colliderect(el):
                    health_points -= 1
                    enemy_list.pop(i)

        if eye_list:
            for j, elem in enumerate(eye_list):
                if not paused:
                    screen.blit(eye_fly[eye_step], elem)
                    elem.x -= 22
                else:
                    screen.blit(eye_fly[0], elem)

                if elem.x < -10:
                    eye_list.pop(j)

                if ghost_hitbox.colliderect(elem):
                    health_points -= 2
                    eye_list.pop(j)


        # Steps
        if ghost_step == 15:
            ghost_step = 0
        else:
            ghost_step += 1

        if knifes_step == 7:
            knifes_step = 0
        else:
            knifes_step += 1

        if eye_step == 5:
            eye_step = 0
        else:
            eye_step += 1


        # Background Movement
        if not paused:
            bg_x -= 2
            if bg_x == -window_x:
                bg_x = 0


        # Knife and enemy collision
        if knifes:
            for i, el in enumerate(knifes):
                screen.blit(knifes_anim[knifes_step], (el.x, el.y))
                if not paused:
                    el.x += 25

            if el.x > window_x + 20:
                knifes.pop(i)

            if enemy_list:
                for index, enemy_el in enumerate(enemy_list):
                    if el.colliderect(enemy_el):
                        enemy_list.pop(index)
                        knifes.pop(i)

            if eye_list:
                for index, eye_el in enumerate(eye_list):
                    if el.colliderect(eye_el):
                        eye_list.pop(index)
                        knifes.pop(i)

                        # Potion Drop
                        potion_flag = True
                        potion_x = el.x
                        potion_y = el.y


        # Potion Emersion
        if potion_flag:
            screen.blit(heal_potion, (potion_x + 5, potion_y + 3))
            heal_potion_hitbox = heal_potion.get_rect(topleft = (potion_x + 5, potion_y + 3))
            if heal_potion_hitbox.colliderect(ghost_hitbox):
                is_potion = True
                heal_potion_hitbox = heal_potion.get_rect(topleft=(-50, -50))
                potion_x -= (window_x + 300)
                potion_y -= (window_x + 300)


        # Keys
        keys = pygame.key.get_pressed()

        # Run Left
        if not paused:
            if keys[pygame.K_a]:
                screen.blit(walk_left[ghost_step], (ghost_x, ghost_y))
            else:
                screen.blit(walk_right[ghost_step], (ghost_x, ghost_y))
        else:
            screen.blit(ghost_stand, (ghost_x, ghost_y))

        # Run Right
        if keys[pygame.K_d] and ghost_x < (window_x - 80) and not paused:
            ghost_x += ghost_speed
        elif keys[pygame.K_a] and ghost_x > 10 and not paused:
            ghost_x -= ghost_speed

        # Use Heal Potion
        if keys[pygame.K_e] and is_potion and 0 < health_points < 3 and not paused:
            health_points += 1
            is_potion = False

        # Jump
        if not paused:
            if not is_jump:
                if keys[pygame.K_w]:
                    is_jump = True
            else:
                if jump_count >= -8:
                    if jump_count > 0:
                        ghost_y -= (jump_count ** 2)
                    else:
                        ghost_y += (jump_count ** 2)
                    jump_count -= 2
                else:
                    is_jump = False
                    jump_count = 8


        # Potion Bar
        if is_potion:
            screen.blit(heal_potion, heal_potion_bar_xy)
        else:
            screen.blit(heal_potion_empty, heal_potion_bar_xy)

        # Shield Bar
        if health_points == 7:
            screen.blit(shield_bar_full, shield_bar_xy)
            screen.blit(hp_full, hp_bar_xy)
        if health_points == 6:
            screen.blit(shield_bar_good, shield_bar_xy)
            screen.blit(hp_full, hp_bar_xy)
        if health_points == 5:
            screen.blit(shield_bar_medium, shield_bar_xy)
            screen.blit(hp_full, hp_bar_xy)
        if health_points == 4:
            screen.blit(shield_bar_low, shield_bar_xy)
            screen.blit(hp_full, hp_bar_xy)

        # Health_Point Bar
        if health_points == 3:
            screen.blit(hp_full, hp_bar_xy)
            screen.blit(shield_bar_zero, shield_bar_xy)
        if health_points == 2:
            screen.blit(hp_medium, hp_bar_xy)
            screen.blit(shield_bar_zero, shield_bar_xy)
        if health_points == 1:
            screen.blit(hp_low, hp_bar_xy)
            screen.blit(shield_bar_zero, shield_bar_xy)
        if health_points <= 0:
            gameplay = False

        # Knifes Bar
        if knifes_left == 3:
            screen.blit(knife_bar_full, knifes_bar_xy)
        if knifes_left == 2:
            screen.blit(knife_bar_medium, knifes_bar_xy)
        if knifes_left == 1:
            screen.blit(knife_bar_low, knifes_bar_xy)
        if knifes_left == 0:
            screen.blit(knife_bar_zero, knifes_bar_xy)


        # Pause
        if paused:
            pygame.draw.rect(surface, (128, 128, 128, 150), [0, 0, window_x, window_y])
            screen.blit(surface, (0, 0))


    else:

        # Restart Window
        bg_sound.stop()
        screen.fill((87, 88, 89))
        screen.blit(lose_label, (370, 300))
        screen.blit(restart_label, restart_label_hitbox)

        # Restart Button Click
        mouse = pygame.mouse.get_pos()
        if restart_label_hitbox.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            bg_sound.play(-1)

            ghost_x = 150
            knifes_left = 3
            bg_x = 0
            health_points = 7
            potion_x -= (window_x + 300)
            potion_y -= (window_x + 300)

            enemy_list.clear()
            eye_list.clear()
            knifes.clear()

            screen.blit(shield_bar_full, shield_bar_xy)
            screen.blit(hp_full, hp_bar_xy)
            screen.blit(knife_bar_full, knifes_bar_xy)
            screen.blit(heal_potion_empty, heal_potion_bar_xy)
            heal_potion_hitbox = heal_potion.get_rect(topleft = (-50, -50))

            gameplay = True
            is_potion = False


    # Display Update
    pygame.display.update()


    # Event Scan
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if paused:
                    paused = False
                else:
                    paused = True

        if event.type == enemy_timer and not paused:
            enemy_list.append(enemy.get_rect(topleft = (window_x + 10, 540)))
            eye_list.append(eye_fly[0].get_rect(topleft = (window_x + 30, 440)))

        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE and knifes_left > 0 and not paused:
            knifes.append(knifes_anim[0].get_rect(topleft = (ghost_x + 30, ghost_y + 10)))
            knifes_left -= 1


    # Delay
    clock.tick(20)