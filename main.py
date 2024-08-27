import random
import psycopg2
from db_create_connect_fill.config import host, user, password, db_name, port
from old_bot_cards import all_tarot_cards, all_tarot_cards_revers


class Gadanie():
    def one_card(category):
    
    
        deck_rand = list(range(0, 78))
        deck_rand2 = list(range(78, 156))
        random.shuffle(deck_rand)
        random.shuffle(deck_rand2)
        n = 0

        cards_up = []

        if random.randint(0, 10) // 4 != 0:
            n = deck_rand.pop()
            deck_rand2.remove(n+78)
            card_key = all_tarot_cards[n]
            cards_up.append(card_key)

        else:
            n = deck_rand2.pop()
            deck_rand.remove(n-78)
            card_key = all_tarot_cards_revers[n-78]
            cards_up.append(card_key)
            
        print(cards_up, n)
        
        def connToDb ():
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
                port=port
            )
            return connection
    
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
                
                
    def three_cards(category, podclass):
        # cards = list(range(0, 78))
        # inverted_cards = list(range(78, 156))
        deck_rand = list(range(0, 78))
        deck_rand2 = list(range(78, 156))
        random.shuffle(deck_rand)
        random.shuffle(deck_rand2)
        n = []

        count_cards = 0
        cards_up = []
        
        while count_cards != 3:
            if random.randint(0, 10) // 4 != 0:
                n.append(deck_rand.pop())
                deck_rand2.remove(n[-1]+78)
                card_key = all_tarot_cards[n[-1]]
                cards_up.append(card_key) 
                count_cards += 1
        
            else:
                n.append(deck_rand2.pop())
                deck_rand.remove(n[-1]-78)
                card_key = all_tarot_cards_revers[n[-1]-78]
                cards_up.append(card_key) 
                count_cards += 1
        
        print(cards_up, n)

        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
                port=port
            )
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
        return cards_up, n, category, podclass, deck_rand, deck_rand2


    def six_cards():
        deck_rand = list(range(0, 78))
        deck_rand2 = list(range(78, 156))
        random.shuffle(deck_rand)
        random.shuffle(deck_rand2)
        n = []

        count_cards = 0
        cards_up = []
        
        while count_cards !=6:
            if random.randint(0, 10) // 4 != 0:
                n.append(deck_rand.pop())
                deck_rand2.remove(n[-1]+78)
                card_key = all_tarot_cards[n[-1]]
                cards_up.append(card_key) 
                count_cards += 1
        
            else:
                n.append(deck_rand2.pop())
                deck_rand.remove(n[-1]-78)
                card_key = all_tarot_cards_revers[n[-1]-78]
                cards_up.append(card_key) 
                count_cards += 1
        
        print(cards_up, n)

        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
                port=port
            )
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


    def seven_cards():
        deck_rand = list(range(0, 78))
        deck_rand2 = list(range(78, 156))
        random.shuffle(deck_rand)
        random.shuffle(deck_rand2)
        n = []

        count_cards = 0
        cards_up = []
        
        while count_cards !=7:
            if random.randint(0, 10) // 4 != 0:
                n.append(deck_rand.pop())
                deck_rand2.remove(n[-1]+78)
                card_key = all_tarot_cards[n[-1]]
                cards_up.append(card_key) 
                count_cards += 1
        
            else:
                n.append(deck_rand2.pop())
                deck_rand.remove(n[-1]-78)
                card_key = all_tarot_cards_revers[n[-1]-78]
                cards_up.append(card_key) 
                count_cards += 1
        
        print(cards_up, n)

        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
                port=port
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                for el in n:
                    cursor.execute(
                            f"SELECT card_text_love FROM tarot_cards WHERE id = %s", (el+1,)
                        )
                    res = cursor.fetchall()[0][0]
                    if el == n[0]:
                        print(f"Настоящие причины проблем между партнерами\n{cards_up[0]}: {res}\n")
                    elif el == n[1]:
                        print(f"Поверхностные причины конфликтов, на которые тоже стоит обратить внимание\n{cards_up[1]}: {res}\n")
                    elif el == n[2]:
                        print(f"Ваши отношения с партнером в данный момент\n{cards_up[2]}: {res}\n")
                    elif el == n[3]:
                        print(f"Что вас ждет в ближайшем будущем\n{cards_up[3]}: {res}\n")
                    elif el == n[4]:
                        print(f"Что необходимо сделать, чтобы улучшить отношения\n{cards_up[4]}: {res}\n")
                    elif el == n[5]:
                        print(f"Действия (ваши или партнера), которые негативно влияют на вашу связь\n{cards_up[5]}: {res}\n")
                    else:
                        print(f"Есть ли у вас шанс спасти отношения и укрепить связь\n{cards_up[6]}: {res}\n")

                print(f"[INFO] Complied")

        except Exception as ex:
            print("[INFO] Error while working with PostgreSQL", ex)
        else:
            if connection:
                connection.close()
                print("[INFO] PosgreSQL connection closed")
        return cards_up, n


    def eight_cards():
        deck_rand = list(range(0, 78))
        deck_rand2 = list(range(78, 156))
        random.shuffle(deck_rand)
        random.shuffle(deck_rand2)
        n = []

        count_cards = 0
        cards_up = []
        
        while count_cards !=8:
            if random.randint(0, 10) // 4 != 0:
                n.append(deck_rand.pop())
                deck_rand2.remove(n[-1]+78)
                card_key = all_tarot_cards[n[-1]]
                cards_up.append(card_key) 
                count_cards += 1
        
            else:
                n.append(deck_rand2.pop())
                deck_rand.remove(n[-1]-78)
                card_key = all_tarot_cards_revers[n[-1]-78]
                cards_up.append(card_key) 
                count_cards += 1
        
        print(cards_up, n)

        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
                port=port
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                for el in n:
                    cursor.execute(
                            f"SELECT card_text_camon FROM tarot_cards WHERE id = %s", (el+1,)
                        )
                    res = cursor.fetchall()[0][0]
                    if el == n[0]:
                        print(f"Сильные стороны человека\n{cards_up[0]}: {res}\n")
                    elif el == n[1]:
                        print(f"Слабые стороны человека\n{cards_up[1]}: {res}\n")
                    elif el == n[2]:
                        print(f"Что человек тщательно старается скрыть от остальных\n{cards_up[2]}: {res}\n")
                    elif el == n[3]:
                        print(f"Что вызывает у человека крайне негативные чувства, эмоции и мысли\n{cards_up[3]}: {res}\n")
                    elif el == n[4]:
                        print(f"Что может человека радует и дарит позитивный настрой\n{cards_up[4]}: {res}\n")
                    elif el == n[5]:
                        print(f"Чувства и эмоции по отношению к вам\n{cards_up[5]}: {res}\n")
                    elif el == n[6]:
                        print(f"Что человеку нравится в вас, что привлекает\n{cards_up[6]}: {res}\n")
                    elif el == n[7]:
                        print(f"Что его отталкивает, абсолютно точно не нравится в вас\n{cards_up[7]}: {res}\n")
                    

                print(f"[INFO] Complied")

        except Exception as ex:
            print("[INFO] Error while working with PostgreSQL", ex)
        else:
            if connection:
                connection.close()
                print("[INFO] PosgreSQL connection closed")
                
        return cards_up, n


    def ten_cards():
        deck_rand = list(range(0, 78))
        deck_rand2 = list(range(78, 156))
        random.shuffle(deck_rand)
        random.shuffle(deck_rand2)
        n = []

        count_cards = 0
        cards_up = []
        
        while count_cards !=10:
            if random.randint(0, 10) // 4 != 0:
                n.append(deck_rand.pop())
                deck_rand2.remove(n[-1]+78)
                card_key = all_tarot_cards[n[-1]]
                cards_up.append(card_key) 
                count_cards += 1
        
            else:
                n.append(deck_rand2.pop())
                deck_rand.remove(n[-1]-78)
                card_key = all_tarot_cards_revers[n[-1]-78]
                cards_up.append(card_key) 
                count_cards += 1
        
        print(cards_up, n)

        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
                port=port
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                for el in n:
                    cursor.execute(
                            f"SELECT card_text_quest FROM tarot_cards WHERE id = %s", (el+1,)
                        )
                    res = cursor.fetchall()[0][0]
                    if el == n[0]:
                        print(f"Актуальные обстоятельства данного вопроса\n{cards_up[0]}: {res}\n")
                    elif el == n[1]:
                        print(f"Содействующая сила, либо препятствия\n{cards_up[1]}: {res}\n")
                    elif el == n[2]:
                        print(f"Прошлый опыт в решении поставленного вопроса\n{cards_up[2]}: {res}\n")
                    elif el == n[3]:
                        print(f"Недавнее прошлое\n{cards_up[3]}: {res}\n")
                    elif el == n[4]:
                        print(f"Возможное будущее за оговоренный при постановке вопроса период\n{cards_up[4]}: {res}\n")
                    elif el == n[5]:
                        print(f"Ближайшее будущее\n{cards_up[5]}: {res}\n")
                    elif el == n[6]:
                        print(f"Отношение к ситуации и то, каким он себя при этом ощущает\n{cards_up[6]}: {res}\n")
                    elif el == n[7]:
                        print(f"Окружение или другая точка зрения\n{cards_up[7]}: {res}\n")
                    elif el == n[8]:
                        print(f"Надежды и опасения\n{cards_up[8]}: {res}\n")
                    elif el == n[9]:
                        print(f"Конечный исход ситуации\n{cards_up[9]}: {res}\n")
                    

                print(f"[INFO] Complied")

        except Exception as ex:
            print("[INFO] Error while working with PostgreSQL", ex)
        else:
            if connection:
                connection.close()
                print("[INFO] PosgreSQL connection closed")
        return cards_up, n


    def add_two_cards(cards_up, n, category, podclass, deck_rand, deck_rand2):
        random.shuffle(deck_rand)
        random.shuffle(deck_rand2)

        count_cards = 3
        
        while count_cards !=5:
            if random.randint(0, 10) // 4 != 0:
                n.append(deck_rand.pop())
                deck_rand2.remove(n[-1]+78)
                card_key = all_tarot_cards[n[-1]]
                cards_up.append(card_key) 
                count_cards += 1
        
            else:
                n.append(deck_rand2.pop())
                deck_rand.remove(n[-1]-78)
                card_key = all_tarot_cards_revers[n[-1]-78]
                cards_up.append(card_key) 
                count_cards += 1
        
        print(cards_up, n)

        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
                port=port
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                for el in n:
                    cursor.execute(
                            f"SELECT {category} FROM tarot_cards WHERE id = %s", (el+1,)
                        )
                    res = cursor.fetchall()[0][0]
                    if category == 'card_text_camon':
                        if podclass == 'soul':
                            if el == n[0]:
                                print(f"Ваш разум\n{cards_up[0]}: {res}\n")
                            elif el == n[1]:
                                print(f"Ваше тело\n{cards_up[1]}: {res}\n")
                            elif el == n[2]:
                                print(f"Ваша душа\n{cards_up[2]}: {res}\n")
                            elif el == n[3]:
                                print(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                            else:
                                print(f"Ваше будущее\n{cards_up[4]}: {res}\n")
                        elif podclass == 'physic':
                            if el == n[0]:
                                print(f"Физическое состояние\n{cards_up[0]}: {res}\n")
                            elif el == n[1]:
                                print(f"Эмоциональное состояниео\n{cards_up[1]}: {res}\n")
                            elif el == n[2]:
                                print(f"Душевное состояние\n{cards_up[2]}: {res}\n")
                            elif el == n[3]:
                                print(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                            else:
                                print(f"Ваше будущее\n{cards_up[4]}: {res}\n")
                        elif podclass == 'past':
                            if el == n[0]:
                                print(f"Ваше прошлое\n{cards_up[0]}: {res}\n")
                            elif el == n[1]:
                                print(f"Ваше настоящее\n{cards_up[1]}: {res}\n")
                            elif el == n[2]:
                                print(f"Ваше будущее\n{cards_up[2]}: {res}\n")
                            elif el == n[3]:
                                print(f"Далекое прошлое\n{cards_up[3]}: {res}\n")
                            else:
                                print(f"Далекое будущее\n{cards_up[4]}: {res}\n")
                        elif podclass == 'think':
                            if el == n[0]:
                                print(f"Что вы думаете\n{cards_up[0]}: {res}\n")
                            elif el == n[1]:
                                print(f"Что вы чувствуете\n{cards_up[1]}: {res}\n")
                            elif el == n[2]:
                                print(f"Что вам нужно делать\n{cards_up[2]}: {res}\n")
                            elif el == n[3]:
                                print(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                            else:
                                print(f"Ваше будущее\n{cards_up[4]}: {res}\n")
                    
                        if el == n[0]:
                            print(f"Текущая ситуация\n{cards_up[0]}: {res}\n")
                        elif el == n[1]:
                            print(f"Решение\n{cards_up[1]}: {res}\n")
                        elif el == n[2]:
                            print(f"Результат\n{cards_up[2]}: {res}\n")
                        elif el == n[3]:
                            print(f"Прошлое\n{cards_up[3]}: {res}\n")
                        else:
                            print(f"Будущее\n{cards_up[4]}: {res}\n")


                print(f"[INFO] Complied")

        except Exception as ex:
            print("[INFO] Error while working with PostgreSQL", ex)
        else:
            if connection:
                connection.close()
                print("[INFO] PosgreSQL connection closed")
                
        return n, cards_up
        

    def five_cards(category, podclass):
        deck_rand = list(range(0, 78))
        deck_rand2 = list(range(78, 156))
        random.shuffle(deck_rand)
        random.shuffle(deck_rand2)
        n = []

        count_cards = 0
        cards_up = []
        
        while count_cards !=5:
            if random.randint(0, 10) // 4 != 0:
                n.append(deck_rand.pop())
                deck_rand2.remove(n[-1]+78)
                card_key = all_tarot_cards[n[-1]]
                cards_up.append(card_key) 
                count_cards += 1
        
            else:
                n.append(deck_rand2.pop())
                deck_rand.remove(n[-1]-78)
                card_key = all_tarot_cards_revers[n[-1]-78]
                cards_up.append(card_key) 
                count_cards += 1
        
        print(cards_up, n)

        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
                port=port
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                for el in n:
                    cursor.execute(
                            f"SELECT {category} FROM tarot_cards WHERE id = %s", (el+1,)
                        )
                    res = cursor.fetchall()[0][0]
                    if category == 'card_text_camon':
                        if podclass == 'soul':
                            if el == n[0]:
                                print(f"Ваш разум\n{cards_up[0]}: {res}\n")
                            elif el == n[1]:
                                print(f"Ваше тело\n{cards_up[1]}: {res}\n")
                            elif el == n[2]:
                                print(f"Ваша душа\n{cards_up[2]}: {res}\n")
                            elif el == n[3]:
                                print(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                            else:
                                print(f"Ваше будущее\n{cards_up[4]}: {res}\n")
                        elif podclass == 'physic':
                            if el == n[0]:
                                print(f"Физическое состояние\n{cards_up[0]}: {res}\n")
                            elif el == n[1]:
                                print(f"Эмоциональное состояниео\n{cards_up[1]}: {res}\n")
                            elif el == n[2]:
                                print(f"Душевное состояние\n{cards_up[2]}: {res}\n")
                            elif el == n[3]:
                                print(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                            else:
                                print(f"Ваше будущее\n{cards_up[4]}: {res}\n")
                        elif podclass == 'past':
                            if el == n[0]:
                                print(f"Ваше прошлое\n{cards_up[0]}: {res}\n")
                            elif el == n[1]:
                                print(f"Ваше настоящее\n{cards_up[1]}: {res}\n")
                            elif el == n[2]:
                                print(f"Ваше будущее\n{cards_up[2]}: {res}\n")
                            elif el == n[3]:
                                print(f"Далекое прошлое\n{cards_up[3]}: {res}\n")
                            else:
                                print(f"Далекое будущее\n{cards_up[4]}: {res}\n")
                        elif podclass == 'think':
                            if el == n[0]:
                                print(f"Что вы думаете\n{cards_up[0]}: {res}\n")
                            elif el == n[1]:
                                print(f"Что вы чувствуете\n{cards_up[1]}: {res}\n")
                            elif el == n[2]:
                                print(f"Что вам нужно делать\n{cards_up[2]}: {res}\n")
                            elif el == n[3]:
                                print(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                            else:
                                print(f"Ваше будущее\n{cards_up[4]}: {res}\n")
                    elif category == 'card_text_quest':
                        if el == n[0]:
                            print(f"Ситуация\n{cards_up[0]}: {res}\n")
                        elif el == n[1]:
                            print(f"Действие\n{cards_up[1]}: {res}\n")
                        elif el == n[2]:
                            print(f"Исход\n{cards_up[2]}: {res}\n")
                        elif el == n[3]:
                            print(f"Прошлое\n{cards_up[3]}: {res}\n")
                        else:
                            print(f"Будущее\n{cards_up[4]}: {res}\n")
                    elif category == 'card_text_love':
                        if el == n[0]:
                            print(f"Вы\n{cards_up[0]}: {res}\n")
                        elif el == n[1]:
                            print(f"Ваши отношения\n{cards_up[1]}: {res}\n")
                        elif el == n[2]:
                            print(f"Ваш партнер\n{cards_up[2]}: {res}\n")
                        elif el == n[3]:
                            print(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                        else:
                            print(f"Ваше будущее\n{cards_up[4]}: {res}\n")
                    elif category == 'card_text_work':
                        if el == n[0]:
                            print(f"Текущая ситуация\n{cards_up[0]}: {res}\n")
                        elif el == n[1]:
                            print(f"Решение\n{cards_up[1]}: {res}\n")
                        elif el == n[2]:
                            print(f"Результат\n{cards_up[2]}: {res}\n")
                        elif el == n[3]:
                            print(f"Прошлое\n{cards_up[3]}: {res}\n")
                        else:
                            print(f"Будущее\n{cards_up[4]}: {res}\n")


                print(f"[INFO] Complied")

        except Exception as ex:
            print("[INFO] Error while working with PostgreSQL", ex)
        else:
            if connection:
                connection.close()
                print("[INFO] PosgreSQL connection closed")
        return cards_up, n, category, podclass


    def add_one_card(category):
        deck_rand = list(range(0, 78))
        deck_rand2 = list(range(78, 156))
        random.shuffle(deck_rand)
        random.shuffle(deck_rand2)
        n = 0

        cards_up = []

        if random.randint(0, 10) // 4 != 0:
            n = deck_rand.pop()
            deck_rand2.remove(n+78)
            card_key = all_tarot_cards[n]
            cards_up.append(card_key)

        else:
            n = deck_rand2.pop()
            deck_rand.remove(n-78)
            card_key = all_tarot_cards_revers[n-78]
            cards_up.append(card_key)
            
        print(cards_up, n)
        
    
    
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
                port=port
            )
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
        return cards_up