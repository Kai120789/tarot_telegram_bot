from connection import connToDb

try:
    connection = connToDb()
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE tarot_cards(
            id serial PRIMARY KEY,
            card_name varchar(500) NOT NULL,
            card_text_camon varchar(950) NOT NULL,
            card_text_love varchar(950) NOT NULL,
            card_text_quest varchar(950) NOT NULL,
            card_text_work varchar(950) NOT NULL,
            card_text_day_card varchar(950) NOT NULL,
            card_text_month varchar(950) NOT NULL,
            card_text_sovet varchar(950) NOT NULL,
            card_text_yes_or_no varchar(950) NOT NULL
            )"""
        )

        print(f"[INFO] Table created")

except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", ex)
else:
    if connection:
        connection.close()
        print("[INFO] PosgreSQL connection closed")
