# f = open(r"C:\Users\mahes\Downloads\Telegram Desktop\F1xcfKMacAEhKQM.jpg",'rb')
# for e in f:
#     print(e)
#
# fim = open('new_pic','wb')
# for e in f:
#     fim.write(e)

fim = open('new_pic','rb')

for e in fim:
    fim.read(e)

f = open(r"C:\Users\mahes\Downloads\Telegram Desktop\F1xcfKMacAEhKQM.jpg",'rb')
f = open('new_pic','wb')
for e in f:
     f.read(e)