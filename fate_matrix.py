from db_create_connect_fill.connection import connToDb

def fate_matrix(birthday):
    day = birthday[0:2]
    month = birthday[3:5]
    year = birthday[6:10]
    #print(day, month, year)
    diag_square = []
    camon_square = []
    diag_square.append(int(day) if int(day) < 23 else int(day[0]) + int(day[1]))
    diag_square.append(int(month))
    diag_square.append(int(year[0]) + int(year[1]) + int(year[2]) + int(year[3]))
    if diag_square[2] > 22:
        diag_square[2] = int(str(diag_square[2])[0]) + int(str(diag_square[2])[1])
    
    diag_square.append(diag_square[0] + diag_square[1] + diag_square[2])
    if diag_square[3] > 22:
        diag_square[3] = int(str(diag_square[3])[0]) + int(str(diag_square[3])[1])
    
    diag_square.append(diag_square[0] + diag_square[1] + diag_square[2] + diag_square[3])
    if diag_square[4] > 22:
        diag_square[4] = int(str(diag_square[4])[0]) + int(str(diag_square[4])[1])
    
    camon_square.append(diag_square[0] + diag_square[1])
    if camon_square[0] > 22:
        camon_square[0] = int(str(camon_square[0])[0]) + int(str(camon_square[0])[1])
        
    camon_square.append(diag_square[2] + diag_square[1])
    if camon_square[1] > 22:
        camon_square[1] = int(str(camon_square[1])[0]) + int(str(camon_square[1])[1])
        
    camon_square.append(diag_square[2] + diag_square[3])
    if camon_square[2] > 22:
        camon_square[2] = int(str(camon_square[2])[0]) + int(str(camon_square[2])[1])
        
    camon_square.append(diag_square[0] + diag_square[3])
    if camon_square[3] > 22:
        camon_square[3] = int(str(camon_square[3])[0]) + int(str(camon_square[3])[1])
    
    mission = [diag_square[0], diag_square[1], diag_square[0] + diag_square[1]]
    if mission[2] > 22:
        mission[2] = int(str(mission[2])[0]) + int(str(mission[2])[1])
    
    status = [diag_square[4], diag_square[4], diag_square[4] + diag_square[4]]
    if status[2] > 22:
        status[2] = int(str(status[2])[0]) + int(str(status[2])[1])
    
    body = [diag_square[2], diag_square[3], diag_square[2] + diag_square[3]]
    if body[2] > 22:
        body[2] = int(str(body[2])[0]) + int(str(body[2])[1])
    
    funny = [body[0] + status[0], body[1] + status[1]]
    count = 0
    for el in funny:
        if el > 22:
            funny[count] = int(str(funny[count])[0]) + int(str(funny[count])[1])
        count += 1
    funny.append(funny[0] + funny[1])
    if funny[2] > 22:
        funny[2] = int(str(funny[2])[0]) + int(str(funny[2])[1])
    
    
    fate = [mission[0] + status[0], mission[1] + status[1]]
    count = 0
    for el in fate:
        if el > 22:
            fate[count] = int(str(fate[count])[0]) + int(str(fate[count])[1])
        count += 1
    fate.append(fate[0] + fate[1])
    if fate[2] > 22:
        fate[2] = int(str(fate[2])[0]) + int(str(fate[2])[1])
        
    world_card = [fate[0] + status[0], fate[1] + status[1]]
    count = 0
    for el in world_card:
        if el > 22:
            world_card[count] = int(str(world_card[count])[0]) + int(str(world_card[count])[1])
        count += 1
    world_card.append(world_card[0] + world_card[1])
    if world_card[2] > 22:
        world_card[2] = int(str(world_card[2])[0]) + int(str(world_card[2])[1])
        
    fate2 = [fate[0] + mission[0], fate[1] + mission[1]]
    count = 0
    for el in fate2:
        if el > 22:
            fate2[count] = int(str(fate2[count])[0]) + int(str(fate2[count])[1])
        count += 1
    fate2.append(fate2[0] + fate2[1])
    if fate2[2] > 22:
        fate2[2] = int(str(fate2[2])[0]) + int(str(fate2[2])[1])
    
    res = []
    for i in range(0, 3):
        res.append(mission[i] + status[i] + body[i] + funny[i] + fate[i] + world_card[i] + fate2[i])
        if res[i] > 22:
            res[i] = int(str(res[i])[0]) + int(str(res[i])[1])
    
    print(mission, status, body, funny, fate, world_card, fate2)
    print(diag_square, camon_square)
    print(res)
    
    n = diag_square + camon_square
    return n



if __name__ == "__main__":
    n = fate_matrix('15.09.2004')
    
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            count = 0
            for el in n:
                if el != 22:
                    cursor.execute(
                            f"SELECT card_text_camon FROM tarot_cards WHERE id = %s", (el+1,)
                        )
                else:
                    cursor.execute(
                            f"SELECT card_text_camon FROM tarot_cards WHERE id = %s", (1,)
                        )
                res = cursor.fetchall()[0][0]
                if count == 0:
                    print(f"положительная энергия таланта\n{res}\n")
                elif count == 1:
                    print(f"положительная энергия таланта\n{res}\n")
                elif count == 2:
                    print(f"задачи до 40 лет, финансы, здоровье\n{res}\n")
                elif count == 3:
                    print(f"главная задача души в нынешнем воплощении, источник основных проблем\n{res}\n")
                elif count == 4:
                    print(f"основное направление жизни, основные задачи, жизненный путь, внутренние качества\n{res}\n")
                elif count == 5:
                    print(f"линия мужского рода - активные, динамичные качества\n{res}\n")
                elif count == 6:
                    print(f"линия мужского рода - активные, динамичные качества\n{res}\n")
                elif count == 7:
                    print(f"линия женского рода - пасивные, интуитивные качества\n{res}\n")
                elif count == 8:
                    print(f"линия женского рода - пасивные, интуитивные качества\n{res}\n")
                count += 1

            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")

