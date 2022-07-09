from pessoa import Pessoa

p1 = Pessoa("Luiz", 29)
p2 = Pessoa("John", 59)
p1.comer("banana")
p1.parar_comer()
p2.comer("carne")
p1.comer("chocolate")
p2.parar_falar()
p2.falar("programação")
p2.parar_comer()
p2.falar("carros")
p2.parar_falar()
p1.parar_comer()
p1.falar("animais")
p1.comer("banana")
p1.parar_falar()
print(p1.ano_nascimento())
print(p2.ano_nascimento())
print(p1.gera_id())



