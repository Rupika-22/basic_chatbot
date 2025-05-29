import csv
with open("books.csv","r") as file:
    d=[]
    r=csv.reader(file)
    for i in r:
        d.append(i)
        
with open("chat.csv","w",newline="\n",encoding="utf8") as f:
    w=csv.writer(f)
    l=["User_input","chat_bot"]
    w.writerow(l)
    op="yes"
    while op=="yes":
        user=input("enter the task:").lower()
        if user=="bye":
            ch="bye! for any further clarification u can ask me...."
            print(ch)
            L=[user,ch]
            w.writerow(L)
            break
        elif user in ["hi","hello"]:
            ch="hi! how can i help you😁"
            print(ch)
        elif user=="list the book in with author":
            ch="sure! here are some books with author"
            print(ch)
            for r in d:
                print(r)
        elif user=="is there any shopes near by":
            ch="yes there are shops near by.but for a clearification can u provide your area location!😊"
            print(ch)
        elif user=="gdjheduhwid":
            ch="sorry i didn't get it"
            print(ch)
        elif user=="thank you for your help":
            ch="Your welcome!let me know if you want anythingelse do ask me....happy to help☺️"
            print(ch)
        else:
            ch="i am not sure wht u r saying....can u be clear with your wordings"
            print(ch)
        l1=[user,ch]
        w.writerow(l1)
             
