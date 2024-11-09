import telebot
from telebot import types
import random
import json
import os

# JSON file path
DATA_FILE = "player_data.json"


# Load player data from JSON file if it exists
token = "..."
bot = telebot.TeleBot(token)


class Player:
    def __init__(self, id):
        self.id = id
        self.health = 100
        self.energy = 20
        self.strength = 5
        self.timesila = 0
        self.armor = 0
        self.exp = 0
        self.lvl = 1
        self.maxhp = 100
        self.maxenergy = 20
        self.money = 0
        self.artefact = False

    def vsegosila(self):
        return self.strength + self.timesila

    def tratyenergy(self, kolichestvo):
        if self.energy >= kolichestvo:
            self.energy -= kolichestvo
            return True
        else:
            return False

    def level(self):
        self.lvl += 1
        self.exp = 0
        self.maxhp += 5
        self.strength += 5
        self.maxenergy += 10
        self.energy = self.maxenergy
        self.timesila = 0

    def exploot(self, expnow):
        self.exp += expnow
        if self.exp > self.lvl * 50:
            self.level()


class Monster:
    def __init__(self, name, hp, strength, exp, photo, maxhelth):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.exp = exp
        self.photo = photo
        self.money = self.exp * random.randint(5, 10)
        self.maxhelth = maxhelth
def load_data():
    global users
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            for user_id, player_data in data.items():
                user_id = int(user_id)  # Convert user_id back to integer
                player = Player(player_data['id'])
                player.health = player_data['health']
                player.energy = player_data['energy']
                player.strength = player_data['strength']
                player.timesila = player_data['timesila']
                player.armor = player_data['armor']
                player.exp = player_data['exp']
                player.lvl = player_data['lvl']
                player.maxhp = player_data['maxhp']
                player.maxenergy = player_data['maxenergy']
                player.money = player_data['money']
                player.artefact = player_data['artefact']
                users[user_id] = {"player": player, "enemy": None}
    else:
        users = {}


# Save player data to JSON file
def save_data():
    data = {}
    for user_id, info in users.items():
        player = info["player"]
        data[user_id] = {
            "id": player.id,
            "health": player.health,
            "energy": player.energy,
            "strength": player.strength,
            "timesila": player.timesila,
            "armor": player.armor,
            "exp": player.exp,
            "lvl": player.lvl,
            "maxhp": player.maxhp,
            "maxenergy": player.maxenergy,
            "money": player.money,
            "artefact": player.artefact
        }
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)


users = {}
# Initialize player data on bot start
load_data()


monsters = [Monster("Зомби", 25, 10, 10, "https://i.ibb.co/58KtcBJ/image.png", 25),
            Monster("Стражник", 30, 15, 25, "https://i.ibb.co/cYCKJW4/image.png", 30),]
monsters2 = [Monster("Заражённое существо", 45, 40, 40, "https://i.ibb.co/WgCwbxY/image.png", 45),
             Monster("Мутировавший зомби", 40, 30, 20, "https://i.ibb.co/BBHsTj7/image.png", 40)]
monsters3 = [Monster("Тень", 70, 45, 100, "https://i.ibb.co/fnCNBBz/image.png", 70),
             Monster("Демон", 100, 70, 200, "https://i.ibb.co/wzzj585/image.png", 100)]
minibosses = [Monster("Зомби-гигант", 120, 85, 400, "https://i.ibb.co/6W9k64B/image.png", 120),
              Monster("Таинственная тень", 150, 90, 500, "https://i.ibb.co/ZKJVMTG/image.png", 150)]
bosses = [Monster("Демон Ночи, БОСС", 500, 80, 1000, "https://i.ibb.co/tC1MQfM/image.png", 500),
          Monster("Стражник Катакомб", 1000, 400, 5000, "https://i.ibb.co/DLd43rY/image.png", 1000)]

adventfraza = ["Вы совершили хорошую прогулку. На вашем пути ничего не было встречено.",
               "Во время прогулки на вас напал"
               "монстр, но вы его победили.",
               "На вашем пути был встречен бродячий торговец."]


def spawn(cpicok):
    return random.choice(cpicok)

def check(id):
    global users
    if id not in users:
        users[id] = {"player": Player(id), "enemy": None}
    print(users)
    return users[id]

@bot.message_handler(commands=["save"])
def safe(message):
    save_data()
    bot.send_message(message.chat.id, "Данные сохранены.")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Это бот CombatStrike! Здесь что-то по типу игры, но в телеграме!")
    player_info = check(message.from_user.id)
    player = player_info["player"]
    bot.send_message(message.chat.id, f"Твоё здоровье {player.health}, твой уровень {player.lvl}")


@bot.message_handler(commands=["statistic"])
def stata(message):
    player_info = check(message.from_user.id)
    player = player_info["player"]
    bot.send_message(message.chat.id,
                     f"Здоровье: {player.health}♥,\nЭнергия: {player.energy}⚡,\nСила: {player.vsegosila()}💪,\n"
                     f"Уровень: {player.lvl}🎂,\nТекущий прогресс опыта: {player.exp}✨, \nМонеты: {player.money}💰")


loot = ["Восстанавливающий эликсир", "Камень силы"]


def traderknoks(message):
    keyboard = types.InlineKeyboardMarkup()
    healthelexir = types.InlineKeyboardButton("Купить восстанавливающий эликсир.(100)", callback_data="elex")
    powerstone = types.InlineKeyboardButton("Kупить камень силы.(800)", callback_data="stone")
    keyboard.add(healthelexir)
    keyboard.add(powerstone)
    bot.send_message(message.chat.id, "Выбери, что ты хочешь купить?", reply_markup=keyboard)


def monsterss(signal):
    player_info = check(signal.from_user.id)
    player = player_info["player"]
    if player.lvl <= 4 and player_info["enemy"] is None:
        player_info["enemy"] = spawn(monsters)
    elif player.lvl <= 9 and player_info["enemy"] is None:
        player_info["enemy"] = spawn(monsters2)
    elif player.lvl <= 14 and player_info["enemy"] is None:
        player_info["enemy"] = spawn(monsters3)
    elif player.lvl >= 15 and player_info["enemy"] is None and player.artefact == False:
        player_info["enemy"] = spawn(minibosses)
    elif player_info["enemy"] is None and player.artefact:
        player_info["enemy"] = Monster("Демон Ночи", 500, 100, 1000, "https://i.ibb.co/tC1MQfM/image.png", 500)
    enemy = player_info["enemy"]
    bot.send_message(signal.message.chat.id, f"Вы встретили {enemy.name},"
                                             f" HP монстра: {enemy.hp}.")
    bot.send_photo(signal.message.chat.id, enemy.photo)
    battle(signal.message)


@bot.message_handler(commands=["maxhp"])
def mhp(message):
    player_info = check(message.from_user.id)
    player = player_info["player"]
    player.health = player.maxhp





def battle(message):
    keyboard = types.InlineKeyboardMarkup()
    attack = types.InlineKeyboardButton("Атаковать", callback_data="attak")
    goaway = types.InlineKeyboardButton("Отступить", callback_data="away")
    keyboard.add(attack)
    keyboard.add(goaway)
    bot.send_message(message.chat.id, "Твои действия?",
                     reply_markup=keyboard)


@bot.message_handler(commands=["adventure"])
def adventure(message):
    player_info = check(message.from_user.id)
    player = player_info["player"]
    if player.tratyenergy(5):
        bot.send_message(message.chat.id,
                         f"Вы отправляетесь в путешествие. Ваша энергия: {player.energy} / {player.maxenergy}")
        keyboard = types.InlineKeyboardMarkup()
        one = types.InlineKeyboardButton("Пойти по первой дороге", callback_data="first")
        two = types.InlineKeyboardButton("Пойти по второй дороге", callback_data="second")
        three = types.InlineKeyboardButton("Пойти по третьей дороге", callback_data="third")
        keyboard.add(one)
        keyboard.add(two)
        keyboard.add(three)
        bot.send_message(message.chat.id, "Куда пойдёшь?",
                         reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Вы слишком устали. Вам нужно отдохнуть.")


@bot.message_handler(commands=["sleep"])
def otdyx(message):
    player_info = check(message.from_user.id)
    player = player_info["player"]
    player.energy = player.maxenergy
    bot.send_message(message.chat.id, "Вы отдохнули, ваша энергия восстановлена.")


def chance(signal):
    procent = random.random()
    if procent < 0.5:
        monsterss(signal)
    elif procent <= 0.7:
        bot.send_message(signal.message.chat.id, "На вашем пути был встречен бродячий торговец.")
        traderknoks(signal.message)
    else:
        bot.send_message(signal.message.chat.id,
                         "Вы совершили хорошую прогулку. На вашем пути ничего не было встречено.")


@bot.callback_query_handler(func=lambda call: True)
def knok(signal):
    player_info = check(signal.from_user.id)
    player = player_info["player"]
    if signal.data == "attak":
        if player.tratyenergy(2):
            enemy = player_info["enemy"]
            if enemy is None:
                bot.send_message(signal.message.chat.id, "Нет врага для атаки!")
                return
            enemy.hp -= player.vsegosila()
            bot.send_message(signal.message.chat.id,
                             f"Вы нанесли врагу {player.strength} урона, у него осталось {enemy.hp} HP.")
            if enemy.hp > 0:
                player.health -= enemy.strength
                bot.send_message(signal.message.chat.id,
                                 f"Тебя атаковал монстр. Он нанёс тебе {enemy.strength} урона. У тебя осталось {player.health} HP.")
            if player.health <= 0:
                bot.send_message(signal.message.chat.id, "ВЫ УМЕРЛИ!")
                player.exp -= enemy.exp
                player_info["enemy"] = None
                if player.exp < 0:
                    player.exp = 0
            elif enemy.hp <= 0:
                bot.send_message(signal.message.chat.id, "ВЫ УБИЛИ МОНСТРА!")
                player.money += enemy.money
                enemy.hp = enemy.maxhelth
                if enemy in minibosses:
                    artefchance = random.random()
                    if artefchance <= 0.1:
                        player.artefact = True
                player.exploot(enemy.exp)
                player_info["enemy"] = None
        else:
            bot.send_message(signal.message.chat.id, "Недостаточно энергии!")
        battle(signal.message)
    elif signal.data == "away":
        bot.send_message(signal.message.chat.id, "Вы отступили!")
    elif signal.data == "first":
        bot.send_message(signal.message.chat.id, "Вы попали в лес!")
        bot.send_photo(signal.message.chat.id, "https://ibb.co/Kxs28My")
        chance(signal)
    elif signal.data == "second":
        bot.send_message(signal.message.chat.id, "Вы попали на равнины!")
        bot.send_photo(signal.message.chat.id, "https://ibb.co/k9sTMJt")
        chance(signal)
    elif signal.data == "third":
        bot.send_message(signal.message.chat.id, "Вы попали в рощу!")
        bot.send_photo(signal.message.chat.id, "https://ibb.co/dbwcsD3")
        chance(signal)
    elif signal.data == "elex":
        if player.money >= 100:
            player.health = player.maxhp
            player.money -= 100
            bot.send_message(signal.message.chat.id, "Вы купили восстанавливающий эликсир за 100 монет.")
        else:
            bot.send_message(signal.message.chat.id, "У вас недостаточно денег!")
    elif signal.data == "stone":
        if player.money >= 800:
            player.timesila += player.strength * 10
            player.money -= 800
            bot.send_message(signal.message.chat.id, "Вы купили камень силы за 800 монет.")
        else:
            bot.send_message(signal.message.chat.id, "У вас недостаточно денег!")


bot.polling()