import random
from old_bot_cards import all_tarot_cards, all_tarot_cards_revers
from db_create_connect_fill.connection import connToDb
from functions.simple_funcs import create_and_shuffle

def six_cards():
        cards_comon, cards_reversed, cards_up, n = create_and_shuffle()

        count_cards = 0
        
        while count_cards !=6:
            if random.randint(0, 10) // 4 != 0:
                n.append(cards_comon.pop())
                cards_reversed.remove(n[-1]+78)
                card_key = all_tarot_cards[n[-1]]
                cards_up.append(card_key) 
                count_cards += 1
        
            else:
                n.append(cards_reversed.pop())
                cards_comon.remove(n[-1]-78)
                card_key = all_tarot_cards_revers[n[-1]-78]
                cards_up.append(card_key) 
                count_cards += 1
        
        print(cards_up, n)

        try:
            connection = connToDb()
            connection.autocommit = True

            with connection.cursor() as cursor:
                for el in n:
                    cursor.execute(
                            f"SELECT card_text_love FROM tarot_cards WHERE id = %s", (el+1,)
                        )
                    res = cursor.fetchall()[0][0]
                    if el == n[0]:
                        print(f"Чего вы на самом деле хотите от отношений\n{cards_up[0]}: {res}\n")
                    elif el == n[1]:
                        print(f"Уроки, которые вы вынесли из прошлых связей\n{cards_up[1]}: {res}\n")
                    elif el == n[2]:
                        print(f"Проблемы, которые мешают вам открыться противоположному полу\n{cards_up[2]}: {res}\n")
                    elif el == n[3]:
                        print(f"Готово ли ваше сердце к новым отношениям\n{cards_up[3]}: {res}\n")
                    elif el == n[4]:
                        print(f"Готов ли ваш разум к новому роману\n{cards_up[4]}: {res}\n")
                    else:
                        print(f"Готовы ли вы к новым отношениям\n{cards_up[5]}: {res}\n")

                print(f"[INFO] Complied")

        except Exception as ex:
            print("[INFO] Error while working with PostgreSQL", ex)
        else:
            if connection:
                connection.close()
                print("[INFO] PosgreSQL connection closed")
        return cards_up, n
