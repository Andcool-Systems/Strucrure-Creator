import pygame
def load():


    grass_block = pygame.image.load('data/textures/blocks/grass_block.png').convert_alpha()
    leaves = pygame.image.load(f'data/textures/blocks/trees/leaves.png').convert_alpha()
    leaves_log_birch = pygame.image.load(f'data/textures/blocks/trees/leaves_log_birch.png').convert_alpha()
    leaves_log = pygame.image.load(f'data/textures/blocks/trees/leaves_log.png').convert_alpha()

    grass_block_overlay_right = pygame.image.load('data/textures/blocks/grass_overlay/grass_block_overlay_right.png').convert_alpha()
    grass_block_overlay_left = pygame.image.load('data/textures/blocks/grass_overlay/grass_block_overlay_left.png').convert_alpha()
    grass_block_overlay = pygame.image.load('data/textures/blocks/grass_overlay/grass_block_overlay.png').convert_alpha()

    grass_block_overlay_right_angle = pygame.image.load('data/textures/blocks/grass_overlay/grass_block_overlay_right_angle.png').convert_alpha()
    grass_block_overlay_left_angle = pygame.image.load('data/textures/blocks/grass_overlay/grass_block_overlay_left_angle.png').convert_alpha()

    dirt = pygame.image.load('data/textures/blocks/dirt.png').convert_alpha()

    snow = pygame.image.load('data/textures/blocks/block_snow.png').convert_alpha()
    stone = pygame.image.load('data/textures/blocks/stone.png').convert_alpha()
    sand = pygame.image.load('data/textures/blocks/sand.png').convert_alpha()
    gramophone = pygame.image.load('data/textures/blocks/gramophone.png').convert_alpha()
    floor = pygame.image.load('data/textures/blocks/floor.png').convert_alpha()
    spawner = pygame.image.load('data/textures/blocks/spawner.png').convert_alpha()
    
    barrier = pygame.image.load('data/textures/blocks/barrier.png').convert_alpha()
    ice = pygame.image.load('data/textures/blocks/ice.png').convert_alpha()
    not_found = pygame.image.load('data/textures/blocks/not_found.png').convert_alpha()

    lamp_0 = pygame.image.load('data/textures/blocks/lamps/lamp_0.png').convert_alpha()
    lamp_1 = pygame.image.load('data/textures/blocks/lamps/lamp_1.png').convert_alpha()
    der = pygame.image.load('data/textures/blocks/lamps/der.png').convert_alpha()

    log = pygame.image.load('data/textures/blocks/trees/log.png').convert_alpha()
    log_birch = pygame.image.load('data/textures/blocks/trees/log_birch.png').convert_alpha()
    leaves = pygame.image.load('data/textures/blocks/trees/leaves.png').convert_alpha()
    cactus = pygame.image.load('data/textures/blocks/trees/cactus.png').convert_alpha()

    random = pygame.image.load('data/textures/blocks/random.png').convert_alpha()



    chamomile = pygame.image.load('data/textures/blocks/flowers/chamomile.png').convert_alpha()
    tulip_red = pygame.image.load('data/textures/blocks/flowers/tulip_red.png').convert_alpha()
    tulip_orange = pygame.image.load('data/textures/blocks/flowers/tulip_orange.png').convert_alpha()
    tulip_white = pygame.image.load('data/textures/blocks/flowers/tulip_white.png').convert_alpha()
    grass = pygame.image.load('data/textures/blocks/grass.png').convert_alpha()
    snow_plate = pygame.image.load('data/textures/blocks/snow_plate.png').convert_alpha()
    respawn_crystal = pygame.image.load('data/textures/blocks/respawn_crystal.png').convert_alpha()
    air = pygame.image.load('data/textures/blocks/air.png').convert_alpha()
    down = pygame.image.load('data/textures/blocks/down.png').convert_alpha()

    blocks = {-1: air,
              1: dirt, 
              2: grass_block,
              3: floor,
              4: snow,
              5: stone,
              7: respawn_crystal,
              9: log,
              10: leaves,
              17: leaves_log,
              28: log_birch,
              29: leaves_log_birch,

              12: ice,
              13: gramophone,
              15: spawner,
              
              19: sand,
              20: cactus,
              26: grass,

              30: lamp_0,
              
              -2: random,
              -3: down}
    
    blocks_name = {-1: "Воздух",
              1: "Земля", 
              2: "Дерн",
              3: "Нерушимый камень",
              4: "Снег",
              5: "Камень",
              7: "Кристалл возрождения",
              9: "Сосновое бревно",
              10: "Листья",
              17: "Сосновое бревно с листьями",
              28: "Берёзовое бревно",
              29: "Берёзовое бревно с листьями",

              12: "Лед",
              13: "Граммофон",
              15: "Призыватель существ",
              
              19: "Песок",
              20: "Кактус",
              26: "Трава",
              
              30: "Фонарь",
              
              -2: "Установка блока с шансом 1/2",
              -3: "Заполнение блоками вниз"}
    
    return blocks, blocks_name