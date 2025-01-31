import tkinter as tk
import requests
import pyperclip
import tkinter.messagebox as msgbox

window = tk.Tk()
window.title("Link Converter")
window.geometry('400x250')


#define a function
def shorten_link():

    API_KEY = '73f0187440f7d8a05ffc1cb4250ce70e25929'
    BASE_URL = 'https://cutt.ly/api/api.php'
    link_input = insert_link.get()
    name_input = insert_name.get()
    payload = {'key': API_KEY, 'short': link_input, 'name': name_input}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()


    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']


        print(f'Title : {title}')
        print(f'link : {short_link}')
        link_result.config(text = short_link)
        pyperclip.copy(short_link)
        msgbox.showinfo('Link Succes Generate', 'Your link has been generated and automatically copy\n you can paste the link in browser')


    except:
        status = data['url']['status']
        print(f'Error status {status}')
        if status == 1 :
            msgbox.showerror('Error', 'The link already been shortened \n please use another link')
        elif status == 2 :
            msgbox.showerror('Error', 'The link that you input is not a link')
        elif status == 3 :
            msgbox.showerror('Error', 'the name is already taken')
        elif status == 4 :
            msgbox.showerror('Error', 'Invalid API Key')
        elif status == 5 :
            msgbox.showerror('Error', 'Invalid Character')
        elif status == 6:
            msgbox.showerror('Error', 'The link is from a blocked domain')

#widget
title_label = tk.Label(window, text = 'Manage your link', font= ("Arial",20))
label_link = tk.Label(window, text = 'Insert your link : ', font=('Arial',15))
insert_link = tk.Entry(window, width=50)
label_name = tk.Label(window, text = 'Insert name for the link : ', font=('Arial',15))
insert_name = tk.Entry(window, width=50)
button_generate = tk.Button(window, text= 'generate link', command=shorten_link)
link_result = tk.Label(window)

#placement
title_label.pack()
label_link.pack()
insert_link.pack()
label_name.pack()
insert_name.pack()
button_generate.pack()
link_result.pack()



window.mainloop()