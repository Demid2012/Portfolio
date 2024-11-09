from tkinter import *
import random

window = Tk()
window.title("The correct choice of droids")
window.geometry("900x600")
window["bg"] = 'gray17'
tekst = Label(window, text="Добро пожаловать в игру 'The correct choice of droids'",
              bg="green2",
              font=('Courier New', 17, "bold"))
tekst2 = Label(window,
               text="В этой игре вы будете сталкиваться с различными задачами, \n их вы должны решать с помощью дроидов.",
               bg="bisque3",
               font=("Courier New", 16))

'''добавить вместо цифр задания в ковычках примерно 3 штуки'''
tasks = {"R2-D2": ["Ваше командование предполагает, что за тремя холмами расположился лагерь"
                   "противника. \n Вам приказали отправить дроида на разведку.", "На вашу базу напали!\n"
                   " Скорей отправьте дроида на защиту!", "Сапёры доложили, что соседнее с вашей"
                   " базой поле заминировано очень сильными минами\n"
                   " нужно разминировать мины с большой точностью,\n"
                   "если ошибиться, ударная волна может разрушить вашу базу. Отправьте туда дроида!"],
         "B1": ["Нужно спланировать строительство укреплений,\n"
                "это с высокой точностью может сделать дроид.",
                "Капитан приказал построить укрепления, чтобы в случае атаки враг не мог прорваться."],
         "H3-M": ["Один из ваших сослуживцев жалуется на здоровье,\n"
                  "отправьте к нему дроида, что бы понять насколько всё серьёзно,\n"
                  "и как это лечить.",
                  "Вашего боевого товарища ранило! Нужна операция, но она очень сложная.\n"
                  " Только дроид сможет провести ёё.",
                  "К вам в часть поступили новобранцы,\n с помощью дроида, нужно определить\n"
                  "состояние здоровья каждого."],
         "P-1": ["На склад привезли коробки с пойками для солдат.\n"
                 "Там просят помочь с разгрузкой поставки. Дроид с этим эффективно справится.",
                 "Соседней базе наших войск срочно нужны ресурсы!\n Вам приказали отправить туда курьера."]}


'''tasks = {"Капитан приказал построить укрепления, чтобы в случае атаки враг не мог прорваться.": "Дроид-строитель",
         "На вашу базу напали! Скорей отправьте дроида на защиту!": "Боевой дроид",
         "Вашего боевого товарища ранило! Нужна операция, но она очень сложная.\n Только дроид сможет провести ёё.": "Медицинский дроид",
         "Соседней базе наших войск срочно нужны ресурсы!\n Вам приказали отправить туда курьера.": "Дроид курьер"}'''
def new_task():
    if len(tasks) != 0:
        droid = random.choice(list(tasks.keys()))
        task = random.choice(tasks[droid])
        return droid,task
    else:
        return None, None
required_droid, current_task = new_task()

tekst3 = Label(window, text=current_task,
               bg="bisque3",
               font=("Impact", 14),
               pady="30")


def next():
    global current_task, required_droid
    if len(tasks) != 0:
        required_droid, current_task = new_task()
        tekst3["text"] = current_task
        result_label["text"] = "..."
    else:
        tekst["text"] = "Поздравляем! Вы выполнили все задания!"
        tekst2.pack_forget()
        tekst3.pack_forget()
        button_see_droids.pack_forget()
        button_choose_droid.pack_forget()
        button_next.pack_forget()
        result_label.pack_forget()

def new_task():
    if len(tasks) != 0:
        droid = random.choice(list(tasks.keys()))
        task = random.choice(tasks[droid])
        return droid,task
    else:
        return None, None
'''в droid list в кавычках к каждому дроиду дать ему описание после \n но чтобы игроку не было сразу понятно что это за дроид'''

def see_droid():
    droids_window = Toplevel(window)
    droids_window.title("Осмотр дроида")
    droids_window.geometry("900x400")
    droids_window["bg"] = "gray17"
    droids_list = ["R2-D2: \n Этот дроид предназначен для минимизации человеческих потерь "
                   "и выполнения задач,\n которые слишком опасны или сложны для солдат."
                   "Он может быть адаптирован под конкретные операционные требования.",
                   "B1: \n Этот дроид предназначен для повышения эффективности строительных процессов,\n"
                   " сокращения времени выполнения работ и минимизации человеческого фактора.\n"
                   "Он может быть адаптирован под конкретные задачи.",
                   "H3-M: \n Этот дроид оснащен специализированными инструментами и оборудованием,\n"
                   " способными проводить различные процедуры."
                   " Он предназначен для работы в ситуациях, требующих точности и быстроты,\n"
                   " часто оказываясь незаменимым в критических моментах.",
                   "P-1: \n Этот дроид предназначен для оптимизации процесса доставки, \n"
                   "сокращения времени ожидания и минимизации затрат на логистику. Также подходит для \n"
                   "оперативной разгрузки чего-либо."]
    for droid in droids_list:
        Label(droids_window, text=droid, bg="gray17", fg="white", font=("Arial", 12)).pack(pady=5)


def choose_droid():
    choose_window = Toplevel(window)
    choose_window.title("Выбор дроида")
    choose_window.geometry("400x300")
    choose_window["bg"] = 'gray17'
    Label(choose_window, text="Выберите дроида для выполнения задачи:", bg="gray17", fg="white",
          font=("Arial", 12)).pack(pady=10)
    droids_list = ["R2-D2", "B1", "H3-M", "P-1"]
    droid_var = StringVar(value=droids_list[0])
    for droid in droids_list:
        Radiobutton(choose_window, text=droid, variable=droid_var, value=droid, bg="gray17", fg="white",
                    font=("Arial", 12)).pack(anchor=W)

    def send_droid():
        selected_droid = droid_var.get()
        if selected_droid == required_droid:
            result_label.config(text=f"Вы сделали верный выбор!")
            tasks[required_droid].remove(current_task)
            if len(tasks[required_droid]) == 0:
                del tasks[required_droid]
        else:
            result_label.config(text=f"Вы выбрали неправильного дроида, миссия провалена!")

    Button(choose_window, text="Отправить", command=send_droid, bg="green2", font=("Arial", 12)).pack(pady=10)


button_see_droids = Button(window, text="Осмотреть дроидов", command=see_droid, bg="gold", font=("Arial", 12))

button_choose_droid = Button(window, text="Выбрать дроида к отправке", command=choose_droid, bg="gold",
                             font=("Arial", 12))

result_label = Label(window, text="", bg="gray17", fg="white", font=("Arial", 12))
result_label.pack(pady=10)

button_next = Button(window, text="Следующее задание", command=next, bg="blue2",
                     font=("Arial", 12))

tekst.pack(padx=20, pady=20)
tekst2.pack(padx=20, pady=20)
tekst3.pack(padx=15, pady=20)
button_see_droids.pack(pady=10)
button_choose_droid.pack(pady=10)
button_next.pack(pady=10)
window.mainloop()
