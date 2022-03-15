class Element:
    def __init__(self):
        self.text = self.type = self.prior = None

a = input().split()

elms = []
for i in range(len(a)):
    el = Element()
    el.text = a[i]
    if 'a' <= a[i].lower() <= 'z':
        el.type, el.prior = 'val', 3
    if a[i] in ['+', '-', '*', '/']:
        el.type, el.prior  = 'oper', 2 if a[i] in ['*', '/'] else 1
    elms.append(el)


i = 0
while len(elms) != 1:
    if elms[i].type == elms[i+1].type == 'val' and elms[i+2].type == 'oper':
        if elms[i].prior < elms[i+2].prior:
            elms[i].text = '(' + elms[i].text + ')'
        if elms[i+1].prior <= elms[i+2].prior:
            elms[i+1].text = '(' + elms[i+1].text + ')'
        elms[i].text = elms[i].text + ' ' + elms[i+2].text + ' ' + elms[i+1].text
        elms[i].prior = elms[i+2].prior
        elms.pop(i + 1)
        elms.pop(i + 1)
        i = 0
    else:
        i += 1

print(elms[0].text)