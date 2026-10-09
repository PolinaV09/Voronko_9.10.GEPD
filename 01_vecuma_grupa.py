vecums = int(input("Ievadi savu vecumu: ").strip())

if vecums < 0:
    print("Kļūda: vecums nevar būt negatīvs.")
elif vecums <= 12:
     print("bērns")
elif vecums <= 17:
     print("pusaudzis")
elif vecums <= 64:
    print("pieaugušais")
else:
    print("seniors")
