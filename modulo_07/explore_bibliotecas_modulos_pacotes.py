from faker import Faker
import datetime


fake = Faker('pt_BR') 

print("\n--- Uso da Biblioteca Faker ---")
print(f"Nome Aleatório: {fake.name()}")
print(f"Endereço Aleatório: {fake.address()}")
print(f"Email Falso: {fake.email()}")