import pygame
import sys
import random
import os

os.chdir('C:\\Users\\fujitsu\\Pictures\\other game\\image')
# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

# Set up the game title
pygame.display.set_caption("Game")
font = pygame.font.Font(None, 24)
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
flag = 0
# Load background images
background_images = []
for i in range(96):  # assuming 19 background images
    image = pygame.image.load(f'background{i}.png').convert_alpha()
    image = pygame.transform.scale(image, (screen_width, screen_height))  # scale the image to fit the screen
    background_images.append(image)

background_index = 0
background_timer = 0

# Load NPC and building images
goblin_images = []
for i in range(4):  # assuming 5 goblin images
    image = pygame.image.load(f'goblin{i}.png').convert_alpha()
    image = pygame.transform.scale(image, (400, 400))  # scale the image to fit the screen
    goblin_images.append(image)


# Load NPC and building images
character_images_run = []
for i in range(10):  # assuming 5 goblin images
    image = pygame.image.load(f'C:\\Users\\fujitsu\\Pictures\\other game\\Hero Knight\\Sprites\\HeroKnight\\Run\\HeroKnight_Run_{i}.png').convert_alpha()
    image = pygame.transform.scale(image, (400, 400))  # scale the image to fit the screen
    character_images_run.append(image)

river_images = []
for i in range(9):  # assuming 5 goblin images
    image = pygame.image.load(f'river-{i}.png').convert_alpha()
    image = pygame.transform.scale(image, (screen_width, screen_height))  # scale the image to fit the screen
    river_images.append(image)

inn_image = pygame.image.load('inn.png').convert_alpha()
cave_image = pygame.image.load('cave.png').convert_alpha()

# Define the character's starting stats
character_name = "Author"
character_health = 100
character_strength = 10
character_agility = 10
character_intelligence = 10

inn_image = pygame.image.load('inn.png').convert_alpha()
village = pygame.image.load('village.png').convert_alpha()
village =  pygame.transform.scale(village, (screen_width, screen_height))
cave_image = pygame.image.load('cave.png').convert_alpha()
cave_image = pygame.transform.scale(cave_image, (screen_width, screen_height))

mountain_image = pygame.image.load('mountain.png').convert_alpha()
mountain_image = pygame.transform.scale(mountain_image, (screen_width, screen_height))

castle_image = pygame.image.load('castle.png').convert_alpha()
castle_image = pygame.transform.scale(castle_image, (screen_width, screen_height))

dark_forest_image = pygame.image.load('dark_forest.png').convert_alpha()
dark_forest_image = pygame.transform.scale(dark_forest_image, (screen_width, screen_height))

stranger_image = pygame.image.load('stranger.png').convert_alpha()

mine_image = pygame.image.load('mine.png').convert_alpha()
mine_image = pygame.transform.scale(mine_image, (screen_width, screen_height))

oasis_image = pygame.image.load('oasis.png').convert_alpha()
oasis_image = pygame.transform.scale(oasis_image, (screen_width, screen_height))

factory_image = pygame.image.load('factory.png').convert_alpha()
factory_image = pygame.transform.scale(factory_image, (screen_width, screen_height))

riverboat_image = pygame.image.load('riverboat.png').convert_alpha()
riverboat_image = pygame.transform.scale(riverboat_image, (screen_width, screen_height))

wildwest = pygame.image.load('wildwest.png').convert_alpha()
wildwest = pygame.transform.scale(wildwest, (screen_width, screen_height))

#2 char
saloon_image = pygame.image.load('saloon.png').convert_alpha()
sheriff_image = pygame.image.load('sheriff.png').convert_alpha()

train_image = pygame.image.load('train.png').convert_alpha()
train_image = pygame.transform.scale(train_image, (screen_width, screen_height))

camping_image = pygame.image.load('camping.png').convert_alpha()
camping_image = pygame.transform.scale(camping_image, (screen_width, screen_height))

# Define the game's events and choices
events = [
    {"name": "Forest Encounter", "description": "You encounter a group of goblins in the forest.", "choices": [
        {"text": "Fight the goblins", "action": "fight", "image": goblin_images[0]},
        {"text": "Try to reason with them", "action": "reason", "image": goblin_images[0]},
        {"text": "Run away", "action": "run", "image": None}
    ]},
    {"name": "Village Visit", "description": "You arrive at a small village.", "choices": [
        {"text": "Visit the local inn", "action": "inn", "image": inn_image},
        {"text": "Explore the village", "action": "explore", "image": None},
        {"text": "Leave the village", "action": "leave", "image": None}
    ]},
    {"name": "Cave Exploration", "description": "You enter a dark cave.", "choices": [
        {"text": "Light a torch", "action": "torch", "image": cave_image},
        {"text": "Search for treasure", "action": "treasure", "image": cave_image},
        {"text": "Go back outside", "action": "outside", "image": None}
    ]},
    
    {"name": "River Crossing", "description": "You come across a fast-moving river.", "choices": [
        {"text": "Try to swim across", "action": "swim", "image": None},
        {"text": "Look for a shallow point", "action": "shallow", "image": None},
        {"text": "Follow the river downstream", "action": "downstream", "image": None}
    ]},
    {"name": "Mountain Climb", "description": "You begin to climb a steep mountain.", "choices": [
        {"text": "Keep climbing", "action": "climb", "image": mountain_image},
        {"text": "Search for a path", "action": "path", "image": mountain_image},
        {"text": "Turn back", "action": "turn_back", "image": None}
    ]},
    {"name": "Abandoned Castle", "description": "You come across an abandoned castle.", "choices": [
        {"text": "Explore the castle", "action": "explore_castle", "image": castle_image},
        {"text": "Search for treasure", "action": "treasure_castle", "image": castle_image},
        {"text": "Leave the castle", "action": "leave_castle", "image": None}
    ]},
    {"name": "Dark Forest", "description": "You enter a dark and foreboding forest.", "choices": [
        {"text": "Press on", "action": "press_on", "image": dark_forest_image},
        {"text": "Search for a clearing", "action": "clearing", "image": dark_forest_image},
        {"text": "Turn back", "action": "turn_back", "image": None}
    ]},
    {"name": "Mysterious Stranger", "description": "You meet a mysterious stranger on the road.", "choices": [
        {"text": "Talk to the stranger", "action": "talk", "image": stranger_image},
        {"text": "Be cautious", "action": "cautious", "image": stranger_image},
        {"text": "Ignore the stranger", "action": "ignore", "image": None}
    ]},
        {"name": "Abandoned Mine", "description": "You stumble upon an abandoned mine on the outskirts of town.", "choices": [
        {"text": "Explore the mine", "action": "explore_mine", "image": mine_image},
        {"text": "Search for valuable resources", "action": "search_resources", "image": mine_image},
        {"text": "Leave the mine", "action": "leave_mine", "image": None}
    ]},
    {"name": "Desert Oasis", "description": "You come across a small oasis in the middle of the desert.", "choices": [
        {"text": "Rest and refresh", "action": "rest", "image": oasis_image},
        {"text": "Explore the surrounding area", "action": "explore_area", "image": oasis_image},
        {"text": "Continue on your journey", "action": "continue_journey", "image": None}
    ]},
    {"name": "Old Factory", "description": "You enter an old, abandoned factory on the outskirts of town.", "choices": [
        {"text": "Explore the factory", "action": "explore_factory", "image": factory_image},
        {"text": "Search for useful items", "action": "search_items", "image": factory_image},
        {"text": "Leave the factory", "action": "leave_factory", "image": None}
    ]},
    {"name": "Riverboat", "description": "You board a riverboat traveling down a major river.", "choices": [
        {"text": "Talk to the captain", "action": "talk_captain", "image": riverboat_image},
        {"text": "Explore the boat", "action": "explore_boat", "image": riverboat_image},
        {"text": "Get off at the next stop", "action": "get_off", "image": None}
    ]},
    {"name": "Wild West Town", "description": "You ride into a small town in the Wild West.", "choices": [
        {"text": "Visit the saloon", "action": "visit_saloon", "image": saloon_image},
        {"text": "Talk to the sheriff", "action": "talk_sheriff", "image": sheriff_image},
        {"text": "Leave town", "action": "leave_town", "image": None}
    ]},
    {"name": "Train Station", "description": "You arrive at a bustling train station in a major city.", "choices": [
        {"text": "Buy a ticket", "action": "buy_ticket", "image": train_image},
        {"text": "Explore the station", "action": "explore_station", "image": train_image},
        {"text": "Leave the station", "action": "leave_station", "image": None}
    ]},
    {"name": "Camping Trip", "description": "You go on a camping trip in the mountains.", "choices": [
        {"text": "Set up camp", "action": "set_up_camp", "image": camping_image},
        {"text": "Go hiking", "action": "go_hiking", "image": camping_image},
        {"text": "Return home", "action": "return_home", "image": None}
    ]}


]

# Initialize the current event index
current_event_index = 0

# Initialize the animation start time
animation_start_time = 0

# Initialize the goblin animation
goblin_index = 0
goblin_timer = 0

character_index = 0
character_timer = 0

ri = 0
rt = 0

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the animation
    current_time = pygame.time.get_ticks()
    if current_time - background_timer >= 100:
        background_index = (background_index + 1) % len(background_images)
        background_timer = current_time

    # Present the animated background
    screen.blit(background_images[background_index], (0, 0))
    #(background_index)
    end = random.randint(1,9)*1000
  # loop 20 times
    current_time = pygame.time.get_ticks()
    if current_time - character_timer >= 100:
        character_index = (character_index + 1) % len(character_images_run)
        character_timer = current_time
        #(f"Showing goblin image {goblin_index}")  # # the current goblin image index

    frame = character_images_run[character_index]
    frame_rect = frame.get_rect()
    frame_rect.center = (500, 700)
    screen.blit(background_images[background_index], (0, 0))  # use the first background image
    screen.blit(frame, frame_rect)
    
    # Check if 3 seconds have passed
    if animation_start_time == 0:
        animation_start_time = pygame.time.get_ticks()
    elif pygame.time.get_ticks() - animation_start_time >= end:  # 3 seconds
        # Get a random event
        current_event_index = random.randint(0, len(events) - 1)

        # Draw the last goblin image
        frame = character_images_run[-1]  
        frame_rect = frame.get_rect()
        frame_rect.center = (600, 700)
        screen.blit(frame, frame_rect)
        print(1)
        
        print()
        if flag == 0:
                
            current_event = events[current_event_index]
        else:
            current_event = events[0]
        screen.blit(background_images[background_index], (0, 0))
        pygame.display.flip()
        if str(current_event["description"]) == "You arrive at a small village.": 
            village = pygame.transform.scale(village, (screen_width, screen_height))
            screen.blit(village, (0, 0))
        if str(current_event["description"]) == "You enter a dark cave.": 
            cave_image = pygame.transform.scale(cave_image, (screen_width, screen_height))
            screen.blit(cave_image, (0, 0))
        if str(current_event["description"]) == "You begin to climb a steep mountain.": 
            mountain_image = pygame.transform.scale(mountain_image, (screen_width, screen_height))
            screen.blit(mountain_image, (0, 0))
        if str(current_event["description"]) == "You come across an abandoned castle.": 
            castle_image = pygame.transform.scale(castle_image, (screen_width, screen_height))
            screen.blit(castle_image, (0, 0))
        if str(current_event["description"]) == "You enter a dark and foreboding forest.": 
            dark_forest_image = pygame.transform.scale(dark_forest_image, (screen_width, screen_height))
            screen.blit(dark_forest_image, (0, 0))
        if str(current_event["description"]) == "You meet a mysterious stranger on the road.": 
            stranger_image = pygame.transform.scale(stranger_image, (100, 100))
            screen.blit(stranger_image, (0, 0))
        if str(current_event["description"]) == "You stumble upon an abandoned mine on the outskirts of town.": 
            mine_image = pygame.transform.scale(mine_image, (screen_width, screen_height))
            screen.blit(mine_image, (0, 0))
        if str(current_event["description"]) == "You come across a small oasis in the middle of the desert.": 
            oasis_image = pygame.transform.scale(oasis_image, (screen_width, screen_height))
            screen.blit(oasis_image, (0, 0))
        if str(current_event["description"]) == "You enter an old, abandoned factory on the outskirts of town.": 
            factory_image = pygame.transform.scale(factory_image, (screen_width, screen_height))
            screen.blit(factory_image, (0, 0))
        if str(current_event["description"]) == "You board a riverboat traveling down a major river.": 
            riverboat_image = pygame.transform.scale(riverboat_image, (screen_width, screen_height))
            screen.blit(riverboat_image, (0, 0))
        if str(current_event["description"]) == "You ride into a small town in the Wild West.": 
            wildwest_image = pygame.transform.scale(wildwest, (screen_width, screen_height))
            screen.blit(wildwest_image, (0, 0))
        if str(current_event["description"]) == "You arrive at a bustling train station in a major city.": 
            train_image = pygame.transform.scale(train_image, (screen_width, screen_height))
            screen.blit(train_image, (0, 0))
        if str(current_event["description"]) == "You go on a camping trip in the mountains.": 
            camping_image = pygame.transform.scale(camping_image, (screen_width, screen_height))
            screen.blit(camping_image, (0, 0))
        pygame.display.flip()
        if str(current_event["description"]) == "You come across a fast-moving river.":
            for i in range(80):
                print("looping",i)
                                    # Update the animation
                current_time = pygame.time.get_ticks()
                if current_time - rt >= 100:
                    ri = (ri + 1) % len(river_images)
                    rt = current_time

                    # Present the animated background
                screen.blit(river_images[ri], (0, 0))
                pygame.display.flip()
                pygame.time.Clock().tick(60)
            screen.blit(river_images[ri], (0, 0))
        description_text = font.render(str(current_event["description"]), True, WHITE)
            
              # use the first background image
        screen.blit(description_text, (100, 100))
            #goblin
        if str(current_event["description"]) == "You encounter a group of goblins in the forest.":
            for _ in range(40):  # loop 20 times
                current_time = pygame.time.get_ticks()
                if current_time - goblin_timer >= 100:
                    goblin_index = (goblin_index + 1) % len(goblin_images)
                    goblin_timer = current_time
                        #(f"Showing goblin image {goblin_index}")  # # the current goblin image index
                        # Draw the last  image
                frame1 = character_images_run[-1]  
                frame1_rect = frame.get_rect()
                frame1_rect.center = (500, 700)
                screen.blit(background_images[background_index], (0, 0))  # use the first background image
                screen.blit(frame1, frame1_rect)
                
                description_text = font.render(str(current_event["description"]), True, WHITE)
                    
                screen.blit(description_text, (100, 100))
                frame = goblin_images[goblin_index]
                frame_rect = frame.get_rect()
                frame_rect.center = (1000, 700)
                screen.blit(frame, frame_rect)
                pygame.display.flip()
                pygame.time.Clock().tick(60)
            
        
        
        # Present the event and choices to the user
        choice_index = 0
        event_choices = current_event["choices"]
        print(event_choices)
        for choice in event_choices:
            pygame.draw.rect(screen, BLACK, (100,150 + choice_index * 50, 200, 40))
            choice_text = font.render(choice["text"], True, WHITE)
            screen.blit(choice_text, (110, 160 + choice_index * 50))
            choice_index += 1

        # Wait for the user to make a choice
        choice_made = False
        while not choice_made:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    choice_index = (mouse_y - 150) // 50
                    if choice_index >= 0 and choice_index < len(event_choices):
                        # Perform the chosen action
                        action = event_choices[choice_index]["action"]
                        

                        # Add game logic for the chosen action here
                        if action == "fight":
                            flag = 0
                            character_health -= 20
                            health_text = font.render(f"You fought the goblins and lost 20 health. Your current health is {character_health}.", True, WHITE)
                            screen.blit(health_text, (100, 350))
                            
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "reason":
                            flag = 0
                            character_intelligence += 5
                            intelligence_text = font.render(f"You tried to reason with the goblins and gained 5 intelligence. Your current intelligence is {character_intelligence}.", True, WHITE)
                            screen.blit(intelligence_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "run":
                            flag = 0
                            character_agility += 5
                            agility_text = font.render(f"You ran away from the goblins and gained 5 agility. Your current agility is {character_agility}.", True, WHITE)
                            screen.blit(agility_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "inn":
                            screen.blit(inn_image, (0, 0))
    
                            character_health += 10
                            health_text = font.render(f"You rested at the inn and gained 10 health. Your current health is {character_health}.", True, WHITE)
                            screen.blit(health_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "explore":
                            robbed= random.randint(1,10)
                            if robbed == 5:
                                flag = 1
                                current_event = events[0]
                                strength_text = font.render(f"You explored the village and were robbed!", True, WHITE)
                            else:
                                character_strength += 5
                                strength_text = font.render(f"You explored the village and gained 5 strength. Your current strength is {character_strength}.", True, WHITE)
                            screen.blit(strength_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "leave":
                            character_agility += 5
                            agility_text = font.render(f"You left the village and gained 5 agility. Your current agility is {character_agility}.", True, WHITE)
                            screen.blit(agility_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "torch":
                            character_intelligence += 5
                            intelligence_text = font.render(f"You lit a torch and gained 5 intelligence. Your current intelligence is {character_intelligence}.", True, WHITE)
                            screen.blit(intelligence_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "treasure":
                            character_strength += 10
                            strength_text = font.render(f"You found treasure and gained 10 strength. Your current strength is {character_strength}.", True, WHITE)
                            screen.blit(strength_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "outside":
                            character_health += 10
                            health_text = font.render(f"You went back outside and gained 10 health. Your current health is {character_health}.", True, WHITE)
                            screen.blit(health_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "swim":
                            character_strength += 5
                            strength_text = font.render(f"You tried to swim across the river and gained 5 strength. Your current strength is {character_strength}.", True, WHITE)
                            screen.blit(strength_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "shallow":
                            character_agility += 5
                            agility_text = font.render(f"You looked for a shallow point and gained 5 agility. Your current agility is {character_agility}.", True, WHITE)
                            screen.blit(agility_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "downstream":
                            character_health += 10
                            health_text = font.render(f"You followed the river downstream and gained 10 health. Your current health is {character_health}.", True, WHITE)
                            screen.blit(health_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "climb":
                            character_strength += 10
                            strength_text = font.render(f"You climbed the mountain and gained 10 strength. Your current strength is {character_strength}.", True, WHITE)
                            screen.blit(strength_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "path":
                            character_agility += 5
                            agility_text = font.render(f"You searched for a path and gained 5 agility. Your current agility is {character_agility}.", True, WHITE)
                            screen.blit(agility_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "turn_back":
                            character_health += 10
                            health_text = font.render(f"You turned back and gained 10 health. Your current health is {character_health}.", True, WHITE)
                            screen.blit(health_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "explore_castle":
                            character_strength += 10
                            strength_text = font.render(f"You explored the castle and gained 10 strength. Your current strength is {character_strength}.", True, WHITE)
                            screen.blit(strength_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "treasure_castle":
                            character_intelligence += 10
                            intelligence_text = font.render(f"You searched for treasure in the castle and gained 10 intelligence. Your current intelligence is {character_intelligence}.", True, WHITE)
                            screen.blit(intelligence_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "leave_castle":
                            character_health += 10
                            health_text = font.render(f"You left the castle and gained 10 health. Your current health is {character_health}.", True, WHITE)
                            screen.blit(health_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "press_on":
                            character_strength += 10
                            strength_text = font.render(f"You pressed on and gained 10 strength. Your current strength is {character_strength}.", True, WHITE)
                            screen.blit(strength_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "clearing":
                            character_agility += 5
                            agility_text = font.render(f"You searched for a clearing and gained 5 agility. Your current agility is {character_agility}.", True, WHITE)
                            screen.blit(agility_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "turn_back":
                            character_health += 10
                            health_text = font.render(f"You turned back and gained 10 health. Your current health is {character_health}.", True, WHITE)
                            screen.blit(health_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "talk":
                            character_intelligence += 5
                            intelligence_text = font.render(f"You talked to the stranger and gained 5 intelligence. Your current intelligence is {character_intelligence}.", True, WHITE)
                            screen.blit(intelligence_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "cautious":
                            character_agility += 5
                            agility_text = font.render(f"You were cautious and gained 5 agility. Your current agility is {character_agility}.", True, WHITE)
                            screen.blit(agility_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action== "ignore":
                            character_health -= 10
                            health_text = font.render(f"You ignored the stranger and lost 10 health. Your current health is {character_health}.", True, WHITE)
                            screen.blit(health_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "explore_mine":
                            character_strength += 10
                            strength_text = font.render(f"You explored the mine and gained 10 strength. Your current strength is {character_strength}.", True, WHITE)
                            screen.blit(strength_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "search_resources":
                            character_intelligence += 10
                            intelligence_text = font.render(f"You searched for resources in the mine and gained 10 intelligence. Your current intelligence is {character_intelligence}.", True, WHITE)
                            screen.blit(intelligence_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "leave_mine":
                            character_health += 10
                            health_text = font.render(f"You left the mine and gained 10 health. Your current health is {character_health}.", True, WHITE)
                            screen.blit(health_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "rest":
                            character_health += 20
                            health_text = font.render(f"You rested at the oasis and gained 20 health. Your current health is {character_health}.", True, WHITE)
                            screen.blit(health_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "explore_area":
                            character_strength += 5
                            strength_text = font.render(f"You explored the surrounding area and gained 5 strength. Your current strength is {character_strength}.", True, WHITE)
                            screen.blit(strength_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "continue_journey":
                            character_agility += 5
                            agility_text = font.render(f"You continued on your journey and gained 5 agility. Your current agility is {character_agility}.", True, WHITE)
                            screen.blit(agility_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "explore_factory":
                            character_intelligence += 10
                            intelligence_text = font.render(f"You explored the factory and gained 10 intelligence. Your current intelligence is {character_intelligence}.", True, WHITE)
                            screen.blit(intelligence_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "search_items":
                            character_strength += 10
                            strength_text = font.render(f"You searched for items in the factory and gained 10 strength. Your current strength is {character_strength}.", True, WHITE)
                            screen.blit(strength_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "leave_factory":
                            character_health += 10
                            health_text = font.render(f"You left the factory and gained 10 health. Your current health is {character_health}.", True, WHITE)
                            screen.blit(health_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "talk_captain":
                            character_intelligence += 5
                            intelligence_text = font.render(f"You talked to the captain and gained 5 intelligence. Your current intelligence is {character_intelligence}.", True, WHITE)
                            screen.blit(intelligence_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "explore_boat":
                            character_strength += 5
                            strength_text = font.render(f"You explored the boat and gained 5 strength. Your current strength is {character_strength}.", True, WHITE)
                            screen.blit(strength_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "get_off":
                            character_agility += 5
                            agility_text = font.render(f"You got off the boat and gained 5 agility. Your current agility is {character_agility}.", True, WHITE)
                            screen.blit(agility_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "visit_saloon":
                            character_health += 10
                            health_text = font.render(f"You visited the non-alchoholic saloon and gained 10 health. Your current health is {character_health}.", True, WHITE)
                            screen.blit(health_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "talk_sheriff":
                            character_intelligence += 5
                            intelligence_text = font.render(f"You talked to the sheriff and gained 5 intelligence. Your current intelligence is {character_intelligence}.", True, WHITE)
                            screen.blit(intelligence_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "leave_town":
                            character_agility += 5
                            agility_text = font.render(f"You left the town and gained 5 agility. Your current agility is {character_agility}.", True, WHITE)
                            screen.blit(agility_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "buy_ticket":
                            character_health += 10
                            health_text = font.render(f"You bought a ticket and gained 10 health. Your current health is {character_health}.", True, WHITE)
                            screen.blit(health_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "explore_station":
                            character_intelligence += 5
                            intelligence_text = font.render(f"You explored the station and gained 5 intelligence. Your current intelligence is {character_intelligence}.", True, WHITE)
                            screen.blit(intelligence_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "leave_station":
                            character_agility += 5
                            agility_text = font.render(f"You left the station and gained 5 agility. Your current agility is {character_agility}.", True, WHITE)
                            screen.blit(agility_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "set_up_camp":
                            character_health += 10
                            health_text = font.render(f"You set up camp and gained 10 health. Your current health is {character_health}.", True, WHITE)
                            screen.blit(health_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "go_hiking":
                            character_strength += 5
                            strength_text = font.render(f"You went hiking and gained 5 strength. Your current strength is {character_strength}.", True, WHITE)
                            screen.blit(strength_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds

                        elif action == "return_home":
                            character_agility += 5
                            agility_text = font.render(f"You returned home and gained 5 agility. Your current agility is {character_agility}.", True, WHITE)
                            screen.blit(agility_text, (100, 350))
                            pygame.display.flip()
                            pygame.time.Clock().tick(60)
                            pygame.time.delay(3000)  # wait for 3 seconds


                        # Break out of the inner loop
                        choice_made = True
                        

            # Update the screen
            pygame.display.flip()
            pygame.time.Clock().tick(60)

        # Move to the next event
        animation_start_time = 0  # reset the animation start time

    # Update the screen
    pygame.display.flip()
    pygame.time.Clock().tick(60)
