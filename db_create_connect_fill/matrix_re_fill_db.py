from old_bot_cards import all_tarot_cards
import copy
from connection import connToDb


all_tarot_cards_revers = list(copy.deepcopy(all_tarot_cards))
for i in range(0, 78):
    all_tarot_cards_revers[i] += " (перевернутая)"
    
all_tarot_cards_revers = tuple(all_tarot_cards_revers)
    
camon = {}
love = {}
quest = {}
day_card = {}
sovet = {}
month = {}
work = {}
yes_or_no = {}

s = ""



# Добавление обычных значений карт
with open("../txt_files/Карты-Таро.txt", "r", encoding="utf16") as file:
    s = file.read()
with open("../txt_files/Карты-Таро.txt", "r", encoding="utf16") as file:
    count = 0
    for i in range(0, 3500):
        fr = file.readline()
        if "Перевернутое положение" in fr:
                
            camon[all_tarot_cards_revers[count]] = s[s.index("Перевернутое положение\n")+len(fr):s.index(f"{all_tarot_cards[count]}: Значение в любви и отношениях")].strip()
            if len(camon[all_tarot_cards_revers[count]]) > 950:
                camon[all_tarot_cards_revers[count]] = camon[all_tarot_cards_revers[count]][:950]
                camon[all_tarot_cards_revers[count]] = camon[all_tarot_cards_revers[count]][:camon[all_tarot_cards_revers[count]].rfind('.')+2]  
            #print(camon[all_tarot_cards_revers[count]])
            if count < 77:
                s = s[s.index(f"{all_tarot_cards[count+1]}"):]
            else:
                break
            count += 1

print(len(camon))


# Добавление значений карт в любви и отношениях
with open("../txt_files/Карты-Таро.txt", "r", encoding="utf16") as file:
    s = file.read()
with open("../txt_files/Карты-Таро.txt", "r", encoding="utf16") as file:
    count = 0
    for i in range(0, 3500):
        z = file.readline()
        if "Общее значение" in z:
            s = s[s.index("Значение в любви и отношениях"):]
        if "Значение в любви и отношениях" in z:
            z = file.readline()
            if "Прямое положение" in z:
                    
                love[all_tarot_cards_revers[count]] = s[s.index("Перевернутое положение\n")+len(fr):s.index(f"{all_tarot_cards[count]}: Значение в ситуации и вопросе")].strip()
                if len(love[all_tarot_cards_revers[count]]) > 950:
                    love[all_tarot_cards_revers[count]] = love[all_tarot_cards_revers[count]][:950]
                    love[all_tarot_cards_revers[count]] = love[all_tarot_cards_revers[count]][:love[all_tarot_cards_revers[count]].rfind('.')+2]  
                #print(love[all_tarot_cards_revers[count]])
                if count < 77:
                    s = s[s.index(f"{all_tarot_cards[count+1]}"):]
                else:
                    break
                count += 1
                

print(len(love))


# Добавление значений карт в ситуации и вопросе
with open("../txt_files/Карты-Таро.txt", "r", encoding="utf16") as file:
    s = file.read()
with open("../txt_files/Карты-Таро.txt", "r", encoding="utf16") as file:
    count = 0
    for i in range(0, 3500):
        z = file.readline()
        if "Общее значение" in z:
            s = s[s.index("Значение в любви и отношениях"):]
        if "Значение в любви и отношениях" in z:
            s = s[s.index("Значение в ситуации и вопросе"):]
        if "Значение в ситуации и вопросе" in z:
            z = file.readline()
            if "Прямое положение" in z:
                quest[all_tarot_cards_revers[count]] = s[s.index("Перевернутое положение\n")+len(fr):s.index(f"{all_tarot_cards[count]}: Значение карты дня")].strip()
                if len(quest[all_tarot_cards_revers[count]]) > 950:
                    quest[all_tarot_cards_revers[count]] = quest[all_tarot_cards_revers[count]][:950]
                    quest[all_tarot_cards_revers[count]] = quest[all_tarot_cards_revers[count]][:quest[all_tarot_cards_revers[count]].rfind('.')+2]  
                #print(quest[all_tarot_cards_revers[count]])
                if count < 77:
                    s = s[s.index(f"{all_tarot_cards[count+1]}"):]
                else:
                    break
                count += 1

print(len(quest))


# Добавление значений карт в карте дня
with open("../txt_files/Карты-Таро.txt", "r", encoding="utf16") as file:
    s = file.read()
with open("../txt_files/Карты-Таро.txt", "r", encoding="utf16") as file:
    count = 0
    for i in range(0, 3500):
        z = file.readline()
        if count < 78 and f"{all_tarot_cards[count]}: Значение карты дня\n" in z:
            fr = file.readline()
                
            day_card[all_tarot_cards_revers[count]] = s[s.index(f"Значение карты дня\n"):s.index(f"{all_tarot_cards[count]}: Совет карты\n")].strip()
            if len(day_card[all_tarot_cards_revers[count]]) > 950:
                day_card[all_tarot_cards_revers[count]] = day_card[all_tarot_cards_revers[count]][:950]
                day_card[all_tarot_cards_revers[count]] = day_card[all_tarot_cards_revers[count]][:day_card[all_tarot_cards_revers[count]].rfind('.')+2]  
            #print(camon[all_tarot_cards[count]])
            if count < 77:
                s = s[s.index(f"{all_tarot_cards[count+1]}"):]
            count += 1

print(len(day_card))


# Добавление значений карт в совет карты
with open("../txt_files/Карты-Таро.txt", "r", encoding="utf16") as file:
    s = file.read()
with open("../txt_files/Карты-Таро.txt", "r", encoding="utf16") as file:
    count = 0
    for i in range(0, 3500):
        z = file.readline()
        if count < 78 and f"{all_tarot_cards[count]}: Значение карты дня\n" in z:
            fr = file.readline()
            if count < 77:
                sovet[all_tarot_cards_revers[count]] = s[s.index(f"Совет карты"):s.index(f"{all_tarot_cards[count+1]}")].strip()
                s = s[s.index(f"{all_tarot_cards[count+1]}"):]
            if count == 77:
                sovet[all_tarot_cards_revers[count]] = s[s.index(f"Совет карты\n"):].strip()
            
            if len(sovet[all_tarot_cards_revers[count]]) > 950:
                sovet[all_tarot_cards_revers[count]] = sovet[all_tarot_cards_revers[count]][:950]
                sovet[all_tarot_cards_revers[count]] = sovet[all_tarot_cards_revers[count]][:sovet[all_tarot_cards_revers[count]].rfind('.')+2]  
            #print(camon[all_tarot_cards[count]])
                  
            count += 1

print(len(sovet))


with open("../txt_files/Месяц.txt", "r", encoding="utf16") as file:
    s = file.read()
with open("../txt_files/Месяц.txt", "r", encoding="utf16") as file:
    count = 0
    for i in range(0, 633):
        z = file.readline()
        if count < 78 and f"{all_tarot_cards[count]} - общие события месяца" in z:
            fr = file.readline()
            if count < 77:
                month[all_tarot_cards_revers[count]] = s[s.index(f"{all_tarot_cards[count]} - общие события месяца"):s.index(f"{all_tarot_cards[count+1]}")].strip()
                s = s[s.index(f"{all_tarot_cards[count+1]}"):]
            if count == 77:
                month[all_tarot_cards_revers[count]] = s[s.index(f"{all_tarot_cards[count]} - общие события месяца"):].strip()
            
            if len(month[all_tarot_cards_revers[count]]) > 950:
                month[all_tarot_cards_revers[count]] = month[all_tarot_cards_revers[count]][:950]
                month[all_tarot_cards_revers[count]] = month[all_tarot_cards_revers[count]][:month[all_tarot_cards_revers[count]].rfind('.')+2]  
            #print(month[all_tarot_cards[count]])
                
            count += 1

print(len(month))


with open("../txt_files/Да_Нет.txt", "r", encoding="utf16") as file:
    s = file.read()
with open("../txt_files/Да_Нет.txt", "r", encoding="utf16") as file:
    count = 0
    for i in range(0, 313):
        z = file.readline()
        if count < 78 and f'Перевернутая "{all_tarot_cards[count]}" - значение "да или нет"' in z:
            fr = file.readline()
            if count < 77:
                yes_or_no[all_tarot_cards_revers[count]] = s[s.index(f'Перевернутая "{all_tarot_cards[count]}" - значение "да или нет"'):s.index(f'"{all_tarot_cards[count+1]}" - значение в прямом положении на вопрос "да или нет"')].strip()
                s = s[s.index(f'Перевернутая "{all_tarot_cards[count+1]}" - значение "да или нет"'):]
            if count == 77:
                yes_or_no[all_tarot_cards_revers[count]] = s[s.index(f'Перевернутая "{all_tarot_cards[count]}" - значение "да или нет"'):].strip()
            
            if len(yes_or_no[all_tarot_cards_revers[count]]) > 950:
                yes_or_no[all_tarot_cards_revers[count]] = yes_or_no[all_tarot_cards_revers[count]][:950]
                yes_or_no[all_tarot_cards_revers[count]] = yes_or_no[all_tarot_cards_revers[count]][:yes_or_no[all_tarot_cards_revers[count]].rfind('.')+2]  
            #print(yes_or_no[all_tarot_cards[count]])
                
            count += 1

print(len(yes_or_no))


with open("../txt_files/Работа_и_финансы.txt", "r", encoding="utf16") as file:
    s = file.read()
with open("../txt_files/Работа_и_финансы.txt", "r", encoding="utf16") as file:
    count = 0
    for i in range(0, 1291):
        z = file.readline()
        if count < 78 and f'Перевернутая "{all_tarot_cards[count]}" в работе и финансах: значение' in z:
            fr = file.readline()
            if count < 77:
                work[all_tarot_cards_revers[count]] = s[s.index(f'Перевернутая "{all_tarot_cards[count]}" в работе и финансах: значение'):s.index(f'Значение карты "{all_tarot_cards[count+1]}" в прямом положении в работе и финансах')].strip()
                s = s[s.index(f'Перевернутая "{all_tarot_cards[count+1]}" в работе и финансах: значение'):]
            
            
            if count == 77:
                work[all_tarot_cards_revers[count]] = s[s.index(f'Перевернутая "{all_tarot_cards[count]}" в работе и финансах: значение'):].strip()
            
            if len(work[all_tarot_cards_revers[count]]) > 950:
                work[all_tarot_cards_revers[count]] = work[all_tarot_cards_revers[count]][:950]
                work[all_tarot_cards_revers[count]] = work[all_tarot_cards_revers[count]][:work[all_tarot_cards_revers[count]].rfind('.')+2]
            #print(work[all_tarot_cards_revers[count]])
            count += 1

print(len(work))

try:
    connection = connToDb()
    connection.autocommit = True

    with connection.cursor() as cursor:
        for j in range(1, 79):
            #print(j, all_tarot_cards[j-1], camon[all_tarot_cards[j-1]])
            cards = [j+78, all_tarot_cards_revers[j-1], camon[all_tarot_cards_revers[j-1]], love[all_tarot_cards_revers[j-1]], quest[all_tarot_cards_revers[j-1]], work[all_tarot_cards_revers[j-1]], day_card[all_tarot_cards_revers[j-1]], month[all_tarot_cards_revers[j-1]], sovet[all_tarot_cards_revers[j-1]], yes_or_no[all_tarot_cards_revers[j-1]],]
            cursor.execute(
                "INSERT INTO tarot_cards (id, card_name, card_text_camon, card_text_love, card_text_quest, card_text_work, card_text_day_card, card_text_month, card_text_sovet, card_text_yes_or_no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", cards
            )

        print(f"[INFO] Values appended")

except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", ex)
else:
    if connection:
        connection.close()
        print("[INFO] PosgreSQL connection closed")