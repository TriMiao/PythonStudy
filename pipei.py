#encoding:utf-8
# f = open('/home/ben/文档/男主角1.txt','r')
# print(f.read())

f = open('/home/ben/文档/太空旅客1.txt','r')
print(f.read())

word_lst = []
word_dict= {}
with open('/home/ben/文档/男主角.txt') as wf,open('/home/ben/文档/男主角1.txt','w') as wf2:

    for word in wf:
        word_lst.append(word.split('\n'))
        for item in word_lst:
             for item2 in item:
                if item2 not in word_dict:
                    word_dict[item2] = 0
                else:
                    word_dict[item2] += 1

    for key in word_dict:
        print key,word_dict[key]
        wf2.write(key+' '+str(word_dict[key])+'\n')

