try:
    name = str(input("Введи своё имя\n"))
    age = int(input("Введи свой возраст\n"))
    if age > 0 and age < 10:
       print(f"Привет, шкет {name}")
    elif age > 9 and age <= 18:
       print(f"Как жизнь {name}?")
    elif age > 18 and age < 100:
       print(f"Что желаете {name}?")
    elif age >= 100:
       print(f"{name}, вы лжёте - в настоящее время столько не живут...")
    else:
       print("Ошибка, повторите ввод")
except ValueError:
    print("Ошибка, повторите ввод")
