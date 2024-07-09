import random

İsim = input('İsminiz nedir?:  ').capitalize()
print('\nTaş kağıt makas oyununa hoş geldin {}!'.format(İsim))

user_score , computer_score = 0, 0

while True:

    print("\n1 - Taş\n2 - Kağıt\n3 - Makas")
 

    user_choice = input('Seçimin nedir taş ise 1''i kağıt ise 2''yi makas ise 3''ü yaz veya çıkmak için q yaz:  ').strip()

    if user_choice == 'q':
        break

    if user_choice not in ['1', '2', '3']:
        print('Lütfen geçerli bir seçenek giriniz!')
        continue

    computer_choice = random.choice(['1', '2', '3'])
    
    choices = {'1':'Taş', '2':'Kağıt', '3':'Makas'}
    print(f"\nBilgisyarın seçimi: {choices[computer_choice]}!")

    if computer_choice == user_choice:
        print('\nKazanan yok iki tarafda aynı hamleyi yaptı!')
        continue

    elif (user_choice == '1' and computer_choice == '3') or \
         (user_choice == '2' and  computer_choice == '1') or \
         (user_choice == '3' and computer_choice == '2'):
         user_score += 100
         computer_score -= 50
         print(f'\n{choices[user_choice]}, {choices[computer_choice]} ezer sen kazandın {İsim}') 
    else:
        print(f'\n{choices[computer_choice]},{choices[user_choice]} ezer bilgisayar kazandı')
        computer_score += 100
        user_score -= 50

    print(f'\n {İsim} skoru: {user_score } \n Bilgisayarın skoru : {computer_score}')

          




           

