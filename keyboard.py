from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

rus = KeyboardButton("Русь") # infantry
rome = KeyboardButton("Рим") # infantry
chin = KeyboardButton("Китай") # arches
jap = KeyboardButton("Япония") # infantry
vel = KeyboardButton("Британия") # archers
fra = KeyboardButton("Франция") # infantry
vik = KeyboardButton("Викинги") # infantry
arav = KeyboardButton("Аравия") #arches
gre = KeyboardButton("Греция") # infantry
osman = KeyboardButton("Османская империя") # arches
viz = KeyboardButton("Византия") # cavalery
ind = KeyboardButton("Индейцы") # arches
spa = KeyboardButton("Испания") # cavalery
mon = KeyboardButton("Монголы") # cavalery
vkl = KeyboardButton("Великое княжество Литовское") # cavalery
ger = KeyboardButton("Германия") # cavelery

civilizations = ReplyKeyboardMarkup(resize_keyboard=True).row(rus, rome, jap).row(fra, vik, gre).row(osman, chin, vel).row(arav, ind).row(viz, spa, ger).row(vkl, mon)


atack = KeyboardButton("Атака на город")
progress = KeyboardButton("Посмотреть статистику")
# tren = KeyboardButton("Тренировка армии")
update = KeyboardButton("Улучшить город")
teh = KeyboardButton("Изучить технологию")
# farm = KeyboardButton("Фарм")
update = KeyboardButton("Собрать войска с тренировок | Ресурсы")

panel = ReplyKeyboardMarkup(resize_keyboard=True).row(atack, progress).row(update, teh).row(update)

