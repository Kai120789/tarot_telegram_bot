import random
from old_bot_cards import all_tarot_cards, all_tarot_cards_revers
from db_create_connect_fill.connection import connToDb
from functions.simple_funcs import create_and_shuffle

def one_card(category):
    
    cards_comon, cards_reversed, cards_up, n = create_and_shuffle()
    n = 0

    if random.randint(0, 10) // 4 != 0:
        n = cards_comon.pop()
        cards_reversed.remove(n+78)
        card_key = all_tarot_cards[n]
        cards_up.append(card_key)

    else:
        n = cards_reversed.pop()
        cards_comon.remove(n-78)
        card_key = all_tarot_cards_revers[n-78]
        cards_up.append(card_key)
        
    print(cards_up, n)

    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                    f"SELECT {category} FROM tarot_cards WHERE id = %s", (n+1,)
                )
            res = cursor.fetchall()[0][0]
            print(f"{cards_up[0]}\n{res}")

            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
            
    return cards_up, res, n