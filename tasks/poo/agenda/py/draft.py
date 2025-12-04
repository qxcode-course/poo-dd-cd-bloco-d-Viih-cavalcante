class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id
        self.__number = number

    def isValid(self):
        return self.__number.isdigit()
    
    def getId(self):
        return self.__id
    
    def getNumber(self):
        return self.__number
    
    def __str__(self):
        return f"{self.__id}:{self.__number}"
    
class Contact:
    def __init__(self, name: str):
        self.__name = name
        self.__fones: list[Fone] = []
        self.__favorited = False

    def addFone(self, id: str, number: str):
        fone = Fone(id, number)
        if fone.isValid():
            self.__fones.append(fone)
        else:
            print("fail: fone invalido")

    def rmFone(self, index: int):
        if 0 <= index < len(self.__fones):
            self.__fones.pop(index)
        else:
            print("fail: indice invalido")

    def toogleFavorited(self):
        self.__favorited = not self.__favorited
        
    def isFavorited(self):
        return self.__favorited
        
    def getName(self):
        return self.__name
        
    def getFones(self):
        return self.__fones
        
    def setName(self, name: str):
        self.__name = name

    def __str__(self):
        fav = "@" if self.__favorited else "-"
        fones_str = ", ".join(str(fone) for fone in self.__fones)
        return f"{fav} {self.__name} [{fones_str}]"
        
class Agenda:
    def __init__(self):
        self.__contacts: list[Contact] = []

    def __findPosByName(self, name: str) -> int:
        for i, contact in enumerate(self.__contacts):
            if contact.getName() == name:
                return i
        return -1
    
    def addContact(self, name: str, fones: list[list[str]]):
        pos = self.__findPosByName(name)

        if pos == -1:
            contact = Contact(name)
            for fone_list in fones:
                id = fone_list[0]
                number = fone_list[1]
                contact.addFone(id, number)
            self.__contacts.append(contact)
            self.__contacts.sort(key = lambda c: c.getName())
        else:
            contact = self.__contacts[pos]
            for fone_list in fones:
                id = fone_list[0]
                number = fone_list[1]
                contact.addFone(id, number)

    def getContact(self, name: str):
        pos = self.__findPosByName(name)
        return self.__contacts[pos] if pos != -1 else None
    
    def rmContact(self, name: str):
        pos = self.__findPosByName(name)
        if pos != -1:
            self.__contacts.pop(pos)

    def search(self, pattern: str) -> list[Contact]:
        results: list[Contact] = []
        pattern_lower: str = pattern.lower()
        for contact in self.__contacts:
            if pattern_lower in contact.getName().lower():
                results.append(contact)
                continue
            for fone in contact.getFones():
                if (pattern_lower in fone.getId().lower() or pattern_lower in fone.getNumber()):
                    results.append(contact)
                    break

        return results
        
    def getFavorited(self) -> list[Contact]:
        return [contact for contact in self.__contacts if contact.isFavorited()]
    
    def getContacts(self) -> list[Contact]:
        return self.__contacts

    def __str__(self):
        if not self.__contacts:
            return ""
        result: list[str] = []
        for contact in self.__contacts:
            result.append(str(contact))
        return "\n".join(result)
        
def main():
    agenda = Agenda()

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(agenda)
        elif args[0] == "add":
            name = args[1]
            fones: list[list[str]] = []
            for fone_str in args[2:]:
                id, number = fone_str.split(":")
                fones.append([id, number])
            agenda.addContact(name, fones)
        elif args[0] == "rmFone":
            name = args[1]
            index = int(args[2])
            contact = agenda.getContact(name)
            if contact:
                contact.rmFone(index)
        elif args[0] == "rm":
            nome = args[1]
            agenda.rmContact(nome)
        elif args[0] == "search":
            pattern = args[1]
            results = agenda.search(pattern)
            for contact in results:
                print(contact)
        elif args[0] == "tfav":
            name = args[1]
            contact = agenda.getContact(name)
            if contact:
                contact.toogleFavorited()
        elif args[0] == "favs":
            favs = agenda.getFavorited()
            for contact in favs:
                print(contact)

main()