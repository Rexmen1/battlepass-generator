import os
import yaml
import random

# Configuration
QUEST_CONFIG = {
    'easy': {
        'progress_range': (5, 15),
        'points': 3,
        'exp_multiplier': '3x'
    },
    'medium': {
        'progress_range': (16, 30),
        'points': 4,
        'exp_multiplier': '4x'
    },
    'hard': {
        'progress_range': (31, 50),
        'points': 5,
        'exp_multiplier': '5x'
    }
}

def load_yaml_file(filename):
    with open(f'List/{filename}', 'r') as file:
        return yaml.safe_load(file)

# Load all data files
mobs_data = load_yaml_file('mobs.yml')
blocks_data = load_yaml_file('blocks.yml')
food_data = load_yaml_file('food.yml')
smeltable_data = load_yaml_file('smeltable.yml')
tamable_data = load_yaml_file('tamable.yml')
rideable_data = load_yaml_file('rideable.yml')

def get_quest_difficulty(progress):
    if progress <= 15:
        return 'easy'
    elif progress <= 30:
        return 'medium'
    else:
        return 'hard'

def get_quest_config(progress):
    difficulty = get_quest_difficulty(progress)
    return QUEST_CONFIG[difficulty]

def generate_quest_id(existing_ids, prefix=''):
    """Generate a unique quest ID"""
    while True:
        new_id = f"{prefix}{len(existing_ids) + 1}"
        if new_id not in existing_ids:
            return new_id

def generate_mob_quest(quest_id, mob_name):
    required_progress = random.randint(16, 40)  # Reduced max from 64 to 40
    config = get_quest_config(required_progress)
    
    quest = {
        quest_id: {
            'item': {
                'lore': [
                    "&8  &7To complete this quest, you must",
                    f"&8  &7kill &3{required_progress} {mob_name}&7.",
                    '',
                    '&e&lINFORMATION',
                    f"&8  &7EXP: &f{config['exp_multiplier']}",
                    "&8  &7%total_progress%&7/&e%required_progress%",
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)',
                ],
                'material': 'STONE_SWORD',
                'name': f'&e&lQUEST:&f {mob_name} Slayer'
            },
            'name': f'{mob_name} Hunter',
            'points': config['points'],
            'required-progress': required_progress,
            'type': 'kill-mob',
            'variable': mob_name
        }
    }
    return quest

def generate_mining_quest(quest_id, block_name):
    required_progress = random.randint(16, 40)  # Reduced max from 64 to 40
    config = get_quest_config(required_progress)

    quest = {
        quest_id: {
            'anti-abuse': True,
            'item': {
                'lore': [
                    "&8  &7To complete this quest, you must",
                    f"&8  &7Mine &3{required_progress} {block_name}&7.",
                    '',
                    '&e&lINFORMATION',
                    f"&8  &7EXP: &f{config['exp_multiplier']}",
                    "&8  &7%total_progress%&7/&e%required_progress%",
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)',
                ],
                'material': block_name,
                'name': f'&e&lQUEST:&f {block_name} Miner'
            },
            'name': f'{block_name} Miner',
            'points': config['points'],
            'required-progress': required_progress,
            'type': 'block-break',
            'variable': block_name
        }
    }
    return quest

def generate_placing_quest(quest_id, block_name):
    required_progress = random.randint(16, 40)  # Reduced max from 64 to 40
    config = get_quest_config(required_progress)

    quest = {
        quest_id: {
            'anti-abuse': True,
            'item': {
                'lore': [
                    "&8  &7To complete this quest, you must",
                    f"&8  &7Place &3{required_progress} {block_name}&7.",
                    '',
                    '&e&lINFORMATION',
                    f"&8  &7EXP: &f{config['exp_multiplier']}",
                    "&8  &7%total_progress%&7/&e%required_progress%",
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)',
                ],
                'material': block_name,
                'name': f'&e&lQUEST:&f {block_name} Builder'
            },
            'name': f'{block_name} Builder',
            'points': config['points'],
            'required-progress': required_progress,
            'type': 'block-place',
            'variable': block_name
        }
    }
    return quest

def generate_eating_quest(quest_id, food_name):
    required_progress = random.randint(10, 30)  # Reduced for food items
    config = get_quest_config(required_progress)
    
    quest = {
        quest_id: {
            'type': 'consume',
            'name': f'{food_name} Consumer',
            'variable': food_name,
            'required-progress': required_progress,
            'points': config['points'],
            'item': {
                'material': food_name,
                'name': f'&e&lQUEST:&f {food_name} Consumer',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Eat &3{required_progress} {food_name}&7.',
                    '',
                    '&e&lINFORMATION',
                    f"&8 » &7EXP: &f{config['exp_multiplier']}",
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_smelting_quest(quest_id, smeltable_item):
    required_progress = random.randint(16, 40)
    config = get_quest_config(required_progress)
    
    quest = {
        quest_id: {
            'type': 'smelt',
            'name': f'{smeltable_item} Smelter',
            'variable': smeltable_item,
            'required-progress': required_progress,
            'points': config['points'],
            'item': {
                'name': f'&e&lQUEST:&f {smeltable_item} Smelter',
                'material': smeltable_item,
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Smelt items to create &3{required_progress} {smeltable_item}&7.',
                    '',
                    '&e&lINFORMATION',
                    f"&8 » &7EXP: &f{config['exp_multiplier']}",
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_taming_quest(quest_id, tamable_mob):
    required_progress = random.randint(3, 8)  # Reduced for taming
    config = get_quest_config(required_progress)
    
    quest = {
        quest_id: {
            'type': 'tame',
            'name': f'{tamable_mob} Tamer',
            'variable': tamable_mob,
            'required-progress': required_progress,
            'points': config['points'],
            'item': {
                'name': f'&e&lQUEST:&f {tamable_mob} Tamer',
                'material': 'LEAD',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Tame &3{required_progress} {tamable_mob}&7.',
                    '',
                    '&e&lINFORMATION',
                    f"&8 » &7EXP: &f{config['exp_multiplier']}",
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_riding_quest(quest_id, rideable_mob):
    required_progress = random.randint(100, 500)  # Distance in blocks
    config = get_quest_config(required_progress)
    
    quest = {
        quest_id: {
            'type': 'ride-mob',
            'name': f'{rideable_mob} Rider',
            'variable': rideable_mob,
            'required-progress': required_progress,
            'points': config['points'],
            'item': {
                'name': f'&e&lQUEST:&f {rideable_mob} Rider',
                'material': 'SADDLE',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Ride a {rideable_mob} for &3{required_progress} blocks&7.',
                    '',
                    '&e&lINFORMATION',
                    f"&8 » &7EXP: &f{config['exp_multiplier']}",
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_shearing_quest(quest_id):
    required_progress = random.randint(10, 30)
    config = get_quest_config(required_progress)
    
    quest = {
        quest_id: {
            'type': 'shear',
            'name': 'Sheep Shearer',
            'required-progress': required_progress,
            'points': config['points'],
            'item': {
                'name': '&e&lQUEST:&f Sheep Shearer',
                'material': 'SHEARS',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Shear &3{required_progress} sheep&7.',
                    '',
                    '&e&lINFORMATION',
                    f"&8 » &7EXP: &f{config['exp_multiplier']}",
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_milk_quest(quest_id):
    required_progress = random.randint(10, 30)
    config = get_quest_config(required_progress)
    
    quest = {
        quest_id: {
            'type': 'milk',
            'name': 'Cow Milker',
            'required-progress': required_progress,
            'points': config['points'],
            'item': {
                'name': '&e&lQUEST:&f Cow Milker',
                'material': 'BUCKET',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Milk &3{required_progress} cows&7.',
                    '',
                    '&e&lINFORMATION',
                    f"&8 » &7EXP: &f{config['exp_multiplier']}",
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_move_quest(quest_id):
    required_progress = random.randint(1000, 3000)  # Reduced from 5000
    config = get_quest_config(required_progress)
    
    quest = {
        quest_id: {
            'type': 'move',
            'name': 'Adventurous Traveller',
            'required-progress': required_progress,
            'points': config['points'],
            'item': {
                'name': '&e&lQUEST:&f Adventurous Traveller',
                'material': 'COMPASS',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Move a distance of &3{required_progress} blocks&7.',
                    '',
                    '&e&lINFORMATION',
                    f"&8 » &7EXP: &f{config['exp_multiplier']}",
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_swim_quest(quest_id):
    required_progress = random.randint(300, 1000)  # Reduced from 2000
    config = get_quest_config(required_progress)
    
    quest = {
        quest_id: {
            'type': 'swim',
            'name': 'Water Explorer',
            'required-progress': required_progress,
            'points': config['points'],
            'item': {
                'name': '&e&lQUEST:&f Water Explorer',
                'material': 'WATER_BUCKET',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Swim a distance of &3{required_progress} blocks&7.',
                    '',
                    '&e&lINFORMATION',
                    f"&8 » &7EXP: &f{config['exp_multiplier']}",
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_sprint_quest(quest_id):
    required_progress = random.randint(100, 300)  # Reduced from 500
    config = get_quest_config(required_progress)
    
    quest = {
        quest_id: {
            'type': 'sprint',
            'name': 'Speed Demon',
            'required-progress': required_progress,
            'points': config['points'],
            'item': {
                'name': '&e&lQUEST:&f Speed Demon',
                'material': 'SUGAR',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Sprint a distance of &3{required_progress} blocks&7.',
                    '',
                    '&e&lINFORMATION',
                    f"&8 » &7EXP: &f{config['exp_multiplier']}",
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_sneak_quest(quest_id):
    required_progress = random.randint(300, 1000)  # Reduced from 2000
    config = get_quest_config(required_progress)
    
    quest = {
        quest_id: {
            'type': 'sneak',
            'name': 'Stealthy Ninja',
            'required-progress': required_progress,
            'points': config['points'],
            'item': {
                'name': '&e&lQUEST:&f Stealthy Ninja',
                'material': 'LEATHER_BOOTS',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Sneak for &3{required_progress} seconds&7.',
                    '',
                    '&e&lINFORMATION',
                    f"&8 » &7EXP: &f{config['exp_multiplier']}",
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_glide_quest(quest_id):
    required_progress = random.randint(300, 1000)  # Reduced from 2000
    config = get_quest_config(required_progress)
    
    quest = {
        quest_id: {
            'type': 'glide',
            'name': 'Sky Diver',
            'required-progress': required_progress,
            'points': config['points'],
            'item': {
                'name': '&e&lQUEST:&f Sky Diver',
                'material': 'ELYTRA',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Glide a distance of &3{required_progress} blocks&7.',
                    '',
                    '&e&lINFORMATION',
                    f"&8 » &7EXP: &f{config['exp_multiplier']}",
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_fly_quest(quest_id):
    required_progress = random.randint(500, 2000)  # Reduced from 5000
    config = get_quest_config(required_progress)
    
    quest = {
        quest_id: {
            'type': 'fly',
            'name': 'Aviator',
            'required-progress': required_progress,
            'points': config['points'],
            'item': {
                'name': '&e&lQUEST:&f Aviator',
                'material': 'FEATHER',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Fly a distance of &3{required_progress} blocks&7.',
                    '',
                    '&e&lINFORMATION',
                    f"&8 » &7EXP: &f{config['exp_multiplier']}",
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_gain_experience_quest(quest_id):
    required_progress = random.randint(500, 2000)  # Reduced from 5000
    config = get_quest_config(required_progress)
    
    quest = {
        quest_id: {
            'type': 'gain-experience',
            'name': 'Experience Hunter',
            'required-progress': required_progress,
            'points': config['points'],
            'item': {
                'name': '&e&lQUEST:&f Experience Hunter',
                'material': 'EXPERIENCE_BOTTLE',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Gain a total of &3{required_progress} experience points&7.',
                    '',
                    '&e&lINFORMATION',
                    f"&8 » &7EXP: &f{config['exp_multiplier']}",
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

# Generate quests using mob names from mobs.yml
generated_mob_quests = {}
for mob_name in mobs_data:
    quest_id = generate_quest_id(generated_mob_quests, 'mob_')
    generated_mob_quests.update(generate_mob_quest(quest_id, mob_name))

# Generate quests using block names from blocks.yml
generated_mining_quests = {}
for block_name in blocks_data:
    quest_id = generate_quest_id(generated_mining_quests, 'mine_')
    generated_mining_quests.update(generate_mining_quest(quest_id, block_name))

# Generate quests using block names from blocks.yml
generated_placing_quests = {}
for block_name in blocks_data:
    quest_id = generate_quest_id(generated_placing_quests, 'place_')
    generated_placing_quests.update(generate_placing_quest(quest_id, block_name))

# Generate quests using food names from food.yml
generated_food_quests = {}
for food_name in food_data:
    quest_id = generate_quest_id(generated_food_quests, 'food_')
    generated_food_quests.update(generate_eating_quest(quest_id, food_name))

# Generate quests using smeltable item names
generated_smelting_quests = {}
for smeltable_item in smeltable_data:
    quest_id = generate_quest_id(generated_smelting_quests, 'smelt_')
    generated_smelting_quests.update(generate_smelting_quest(quest_id, smeltable_item))

# Generate quests using tamable mobs names
generated_taming_quests = {}
for tamable_mob in tamable_data:
    quest_id = generate_quest_id(generated_taming_quests, 'tame_')
    generated_taming_quests.update(generate_taming_quest(quest_id, tamable_mob))

# Generate quests using rideable mobs names
generated_riding_quests = {}
for rideable_mob in rideable_data:
    quest_id = generate_quest_id(generated_riding_quests, 'ride_')
    generated_riding_quests.update(generate_riding_quest(quest_id, rideable_mob))

# Generate single instance quests
generated_shearing_quests = {generate_quest_id(['1'], 'shear_'): generate_shearing_quest('1')['1']}
generated_milk_quests = {generate_quest_id(['1'], 'milk_'): generate_milk_quest('1')['1']}
generated_move_quests = {generate_quest_id(['1'], 'move_'): generate_move_quest('1')['1']}
generated_swim_quests = {generate_quest_id(['1'], 'swim_'): generate_swim_quest('1')['1']}
generated_sprint_quests = {generate_quest_id(['1'], 'sprint_'): generate_sprint_quest('1')['1']}
generated_sneak_quests = {generate_quest_id(['1'], 'sneak_'): generate_sneak_quest('1')['1']}
generated_glide_quests = {generate_quest_id(['1'], 'glide_'): generate_glide_quest('1')['1']}
generated_fly_quests = {generate_quest_id(['1'], 'fly_'): generate_fly_quest('1')['1']}
generated_gain_experience_quests = {generate_quest_id(['1'], 'exp_'): generate_gain_experience_quest('1')['1']}

# Create 'Quests' folder if it doesn't exist
os.makedirs('Quests', exist_ok=True)

# Function to save quest file
def save_quest_file(filename, data):
    with open(f'Quests/{filename}', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

# Save all quest files
save_quest_file('mobs.yml', generated_mob_quests)
save_quest_file('mining.yml', generated_mining_quests)
save_quest_file('building.yml', generated_placing_quests)
save_quest_file('foods.yml', generated_food_quests)
save_quest_file('smelting.yml', generated_smelting_quests)
save_quest_file('taming.yml', generated_taming_quests)
save_quest_file('riding.yml', generated_riding_quests)
save_quest_file('shearing.yml', generated_shearing_quests)
save_quest_file('milk.yml', generated_milk_quests)
save_quest_file('move.yml', generated_move_quests)
save_quest_file('swim.yml', generated_swim_quests)
save_quest_file('sprint.yml', generated_sprint_quests)
save_quest_file('sneak.yml', generated_sneak_quests)
save_quest_file('glide.yml', generated_glide_quests)
save_quest_file('fly.yml', generated_fly_quests)
save_quest_file('gain_experience.yml', generated_gain_experience_quests)

# Combine all generated quests into a single dictionary
all_generated_quests = {}
all_generated_quests.update(generated_mob_quests)
all_generated_quests.update(generated_mining_quests)
all_generated_quests.update(generated_placing_quests)
all_generated_quests.update(generated_food_quests)
all_generated_quests.update(generated_smelting_quests)
all_generated_quests.update(generated_taming_quests)
all_generated_quests.update(generated_riding_quests)
all_generated_quests.update(generated_shearing_quests)
all_generated_quests.update(generated_milk_quests)
all_generated_quests.update(generated_move_quests)
all_generated_quests.update(generated_swim_quests)
all_generated_quests.update(generated_sprint_quests)
all_generated_quests.update(generated_sneak_quests)
all_generated_quests.update(generated_glide_quests)
all_generated_quests.update(generated_fly_quests)
all_generated_quests.update(generated_gain_experience_quests)

# Save all generated quests into a single file
save_quest_file('extra.yml', all_generated_quests)

print("Generated quests have been saved in their respective files.")