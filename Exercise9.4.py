import pickle
import time

def readfile(fname):
    while True:
        try:
            reader = open(fname,'rb')
            content = pickle.load(reader)
            reader.close()
            return content
        except IOError:
            createfile(fname)
            print("No default notebook was found, created one.")

def writefile(note, fname):
    try:
        writer = open(fname, 'wb')
        pickle.dump(note, writer)
        writer.close()
    except IOError:
        return False

def createfile(fname):
    try:
        writer = open(fname,'wb')
        note=[]
        pickle.dump(note, writer)
        writer.close()
    except IOError:
        return False

def edit(note):
    print("The list has", len(note),"notes.")
    try:
        toEdit = int(input("Which of them will be changed?:"))
        print(note[toEdit])
        newNote = input("Give the new note: ")
        newNote = newNote+":::"
        newNote += time.strftime("%X %x")
        note[toEdit] = newNote
        return note
    except Exception:
        print("Incorrect value.")

def delete(note):
    print("The list has", len(note),"notes.")
    try:
        toDelete = int(input("Which of them will be deleted?: "))
        toDelete -= 1
        print("Deleted note", note[toDelete])
        note.pop(toDelete)

        return note
    except Exception:
        print("Incorrect value.")

def main():
    note = []
    fname = "notebook.dat"
    note = readfile(fname)
    while True:
        selection = int(input('''(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: '''))
        if selection == 1:
            for i in note:
                print(i)
        elif selection == 2:
            newNote=input("Write a new note: ")
            newNote = newNote+":::"
            newNote += time.strftime("%X %x")
            note.append(newNote)
        elif selection == 3:
            note = edit(note)
        elif selection == 4:
            note = delete(note)
        elif selection == 5:
            writefile(note, fname)
            print("Notebook shutting down, thank you.")
            break

if __name__ == "__main__":
        main()
