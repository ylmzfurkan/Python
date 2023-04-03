import os
import sys
from peewee import *

db = SqliteDatabase('notes.db')


class Note(Model):
    content = TextField()

    class Meta:
        database = db


def initialize_db():
    db.connect()
    db.create_tables([Note], safe=True)


def menu_loop():
    choice = None
    while choice != 'q':
        print("Notlarınız için ne yapmak istersiniz?")
        print("q: Çıkış")
        print("n: Yeni not ekle")
        print("l: Notları listele")
        print("d: Not sil")
        choice = input('Eylem: ').lower().strip()
        if choice == 'n':
            add_note()
        elif choice == 'l':
            list_notes()
        elif choice == 'd':
            delete_note()


def add_note():
    print("Yeni notunuzu yazın. Çıkmak için 'q' yazın.")
    data = input('> ')
    if data != 'q':
        Note.create(content=data)
        print("Not eklendi.")


def list_notes():
    notes = Note.select().order_by(Note.id.desc())
    for note in notes:
        print(f"\nID: {note.id}\n{note.content}\n{'*' * 40}")


def delete_note():
    id_to_delete = input("Silmek istediğiniz notun ID'sini girin: ")
    try:
        note_to_delete = Note.get(Note.id == int(id_to_delete))
        note_to_delete.delete_instance()
        print("Not silindi.")
    except Note.DoesNotExist:
        print("Not bulunamadı.")


if __name__ == '__main__':
    initialize_db()
    menu_loop()
    db.close()
