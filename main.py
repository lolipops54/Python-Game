import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1280, 748))
pygame.display.set_caption('In Search of Blood')
icon = pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(icon)

bg = pygame.image.load('images/bg3.png').convert_alpha()
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

ghost_step = 0
bg_x = 0

ghost_speed = 20
ghost_x = 150
ghost_y = 540

is_jump = False
jump_count = 8

bg_sound = pygame.mixer.Sound('sounds/bg.mp3')
bg_sound.play(-1)

enemy = pygame.image.load('images/enemy.png').convert_alpha()

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 4500)

enemy_list = []

label = pygame.font.Font('fonts/RubikBurned-Regular.ttf', 80)
lose_label = label.render('Bro, you lose...', False, 'White')
restart_label = label.render('Click HERE to restart', False, (102, 157, 175))
restart_label_hitbox = restart_label.get_rect(topleft = (185, 400))

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
knifes = []

knifes_step = 0
knifes_left = 3

knife_bar_full = pygame.image.load('images/knife_bar/knife_bar_full.png').convert_alpha()
knife_bar_medium = pygame.image.load('images/knife_bar/knife_bar_medium.png').convert_alpha()
knife_bar_low = pygame.image.load('images/knife_bar/knife_bar_low.png').convert_alpha()
knife_bar_zero = pygame.image.load('images/knife_bar/knife_bar_zero.png').convert_alpha()

hp_full = pygame.image.load('images/hp/hp_full.png').convert_alpha()
hp_medium = pygame.image.load('images/hp/hp_medium.png').convert_alpha()
hp_low = pygame.image.load('images/hp/hp_low.png').convert_alpha()

health_points = 3

heal_potion = pygame.image.load('images/potions/medical.png').convert_alpha()
heal_potion_empty = pygame.image.load('images/potions/medical_empty.png').convert_alpha()

potion_flag = False
is_potion = False

gameplay = True

running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1280, 0))

    if gameplay:

        if health_points == 3:
            screen.blit(hp_full, (20, 700))

        if knifes_left == 3:
            screen.blit(knife_bar_full, (365, 700))

        if is_potion == False:
            screen.blit(heal_potion_empty, (485, 680))

        ghost_hitbox = walk_left[0].get_rect(topleft = (ghost_x, ghost_y))

        if enemy_list:
            for i, el in enumerate(enemy_list):
                screen.blit(enemy, el)
                el.x -= 15

                if el.x < -10:
                    enemy_list.pop(i)

                if ghost_hitbox.colliderect(el):
                    health_points -= 1
                    enemy_list.pop(i)

        if health_points == 2:
            screen.blit(hp_medium, (20, 700))

        if health_points == 1:
            screen.blit(hp_low, (20, 700))

        if health_points == 0:
            gameplay = False

        if knifes_left == 2:
            screen.blit(knife_bar_medium, (365, 700))

        if knifes_left == 1:
            screen.blit(knife_bar_low, (365, 700))

        if knifes_left == 0:
            screen.blit(knife_bar_zero, (365, 700))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            screen.blit(walk_left[ghost_step], (ghost_x, ghost_y))
        else:
            screen.blit(walk_right[ghost_step], (ghost_x, ghost_y))

        if keys[pygame.K_d] and ghost_x < 1200:
            ghost_x += ghost_speed
        elif keys[pygame.K_a] and ghost_x > 10:
            ghost_x -= ghost_speed

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

        if ghost_step == 15:
            ghost_step = 0
        else:
            ghost_step += 1

        if knifes_step == 7:
            knifes_step = 0
        else:
            knifes_step += 1

        bg_x -= 2
        if bg_x == -1280:
            bg_x = 0

        if knifes:
            for i, el in enumerate(knifes):
                screen.blit(knifes_anim[knifes_step], (el.x, el.y))
                el.x += 25

            if el.x > 1300:
                knifes.pop(i)

            if enemy_list:
                for index, enemy_el in enumerate(enemy_list):
                    if el.colliderect(enemy_el):
                        enemy_list.pop(index)
                        knifes.pop(i)
                        potion_flag = True
                        potion_x = el.x
                        potion_y = el.y

        if potion_flag:
            screen.blit(heal_potion, (potion_x + 5, potion_y + 3))
            heal_potion_hitbox = heal_potion.get_rect(topleft = (potion_x + 5, potion_y + 3))
            if heal_potion_hitbox.colliderect(ghost_hitbox):
                is_potion = True
                heal_potion_hitbox = heal_potion.get_rect(topleft=(-50, -50))
                potion_x -= 1500
                potion_y -= 1500

        if is_potion:
            screen.blit(heal_potion, (485, 680))

        if keys[pygame.K_e] and is_potion and 0 < health_points < 3:
            health_points += 1
            is_potion = False

    else:
        bg_sound.stop()
        screen.fill((87, 88, 89))
        screen.blit(lose_label, (370, 300))
        screen.blit(restart_label, restart_label_hitbox)

        mouse = pygame.mouse.get_pos()
        if restart_label_hitbox.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            bg_sound.play(-1)
            ghost_x = 150
            enemy_list.clear()
            knifes.clear()
            knifes_left = 3
            bg_x = 0
            health_points = 3
            screen.blit(hp_full, (20, 700))
            screen.blit(knife_bar_full, (365, 700))
            screen.blit(heal_potion_empty, (485, 680))
            is_potion = False

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == enemy_timer:
            enemy_list.append(enemy.get_rect(topleft = (1290, 540)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE and knifes_left > 0:
            knifes.append(knifes_anim[0].get_rect(topleft = (ghost_x + 30, ghost_y + 10)))
            knifes_left -= 1

    clock.tick(20)