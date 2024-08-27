import random
from old_bot_cards import all_tarot_cards, all_tarot_cards_revers
from db_create_connect_fill.connection import connToDb
from functions.simple_funcs import create_and_shuffle

def three_cards(category, podclass):
        cards_comon, cards_reversed, cards_up, n = create_and_shuffle()

        count_cards = 0
        
        while count_cards != 3:
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
                            f"SELECT {category} FROM tarot_cards WHERE id = %s", (el+1,)
                        )
                    res = cursor.fetchall()[0][0]
                    # Переделать на свитч
                    if category == 'card_text_camon':
                        if podclass == 'soul':
                            if el == n[0]:
                                print(f"Ваш разум\n{cards_up[0]}: {res}\n")
                            elif el == n[1]:
                                print(f"Ваше тело\n{cards_up[1]}: {res}\n")
                            else:
                                print(f"Ваша душа\n{cards_up[2]}: {res}\n")
                        elif podclass == 'physic':
                            if el == n[0]:
                                print(f"Физическое состояние\n{cards_up[0]}: {res}\n")
                            elif el == n[1]:
                                print(f"Эмоциональное состояниео\n{cards_up[1]}: {res}\n")
                            else:
                                print(f"Душевное состояние\n{cards_up[2]}: {res}\n")
                        elif podclass == 'past':
                            if el == n[0]:
                                print(f"Ваше прошлое\n{cards_up[0]}: {res}\n")
                            elif el == n[1]:
                                print(f"Ваше настоящее\n{cards_up[1]}: {res}\n")
                            else:
                                print(f"Ваше будущее\n{cards_up[2]}: {res}\n")
                        elif podclass == 'think':
                            if el == n[0]:
                                print(f"Что вы думаете\n{cards_up[0]}: {res}\n")
                            elif el == n[1]:
                                print(f"Что вы чувствуете\n{cards_up[1]}: {res}\n")
                            else:
                                print(f"Что вам нужно делать\n{cards_up[2]}: {res}\n")
                    elif category == 'card_text_quest':
                        if el == n[0]:
                            print(f"Ситуация\n{cards_up[0]}: {res}\n")
                        elif el == n[1]:
                            print(f"Действие\n{cards_up[1]}: {res}\n")
                        else:
                            print(f"Исход\n{cards_up[2]}: {res}\n")
                    elif category == 'card_text_love':
                        if el == n[0]:
                            print(f"Вы\n{cards_up[0]}: {res}\n")
                        elif el == n[1]:
                            print(f"Ваши отношения\n{cards_up[1]}: {res}\n")
                        else:
                            print(f"Ваш партнер\n{cards_up[2]}: {res}\n")
                    elif category == 'card_text_work':
                        if el == n[0]:
                            print(f"Текущая ситуация\n{cards_up[0]}: {res}\n")
                        elif el == n[1]:
                            print(f"Решение\n{cards_up[1]}: {res}\n")
                        else:
                            print(f"Результат\n{cards_up[2]}: {res}\n")

                print(f"[INFO] Complied")

        except Exception as ex:
            print("[INFO] Error while working with PostgreSQL", ex)
        else:
            if connection:
                connection.close()
                print("[INFO] PosgreSQL connection closed")
        return cards_up, n, category, podclass, cards_comon, cards_reversed
