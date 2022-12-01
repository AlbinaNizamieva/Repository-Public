class Client:
    def __init__(self,name,surname,city,balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'{self.name} {self.surname}. ' \
               f'{self.city}. Баланс: {self.balance} руб.'
    def name_city(self):
        return f'{self.name} {self.surname}. ' \
               f'{self.city}'

Albina = Client('Альбина','Морская','Казань',100)
print(Albina)

Ivan = Client('Иван','Петров','Екатеринбург',10)
Pyotr = Client('Петр','Иванов','Москва',50)
clients = [Albina, Ivan, Pyotr]
for client in clients:
    print(client)
