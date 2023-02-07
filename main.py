# This is a sample Python script.
import sqlite3
import uuid

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # Conectar no banco de dados
    connection = sqlite3.connect('db.sqlite')

    # Criar executor de queries
    cursor = connection.cursor()
    p_name: str = "Vinicius Delecrode"
    p_age: int = 20
    p_id: str = uuid.uuid4().hex

    # Criar uma nova pessoa no banco de dados
    cursor.execute(f"""
        INSERT INTO person (id, name, age) 
        VALUES ("{p_id}", "{p_name}", "{p_age}")
    """)

    # Buscar pessoas no banco de dados
    cursor.execute("""
        SELECT * FROM person
    """)

    # Deletar uma pessoa no banco de dados
    for index, row in enumerate(cursor):
        print(f'ID: {row[0]} | Name: {row[1]} | Age: {row[2]}')

    # Selecionar uma pessoa com ID específico
    pessoa_recem_nascida = cursor.execute(f"""
        SELECT id, name, age FROM person WHERE id = "{p_id}"
    """)

    print("\nINFORMAÇÔES DO RECÈM NASCIDO:\n")
    for row in pessoa_recem_nascida:
        print(f'ID: {row[0]} | Name: {row[1]} | Age: {row[2]}')

    # Deletar a pessoa recém criada
    cursor.execute(f"""
        DELETE FROM person WHERE id = "dsfbcv"
    """)

    for index, row in enumerate(cursor):
        print(f'ID: {row[0]} | Name: {row[1]} | Age: {row[2]}')

    # Atualizar uma pessoa no banco de dados
    cursor.execute(f"""
        UPDATE person SET name = "VINICIN ATUALIZADO", age = "21" WHERE id = "d2343"
    """)


    for index, row in enumerate(cursor):
        print(f'ID: {row[0]} | Name: {row[1]} | Age: {row[2]}')

    # Salva as mudanças no banco de dados
    connection.commit()

    # Fechar conexão
    connection.close()


def add_two_numbers(a: int, b: int) -> int:
    return a + b


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Vinicius')
    print(add_two_numbers(1, 2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
