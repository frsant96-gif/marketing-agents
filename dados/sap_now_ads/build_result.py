import json

names = json.load(open('chunk_01.json', encoding='utf-8'))

data = {
0: ("atem.com.br","high"),
1: ("audi.com.br","high"),
2: ("auren.com.br","high"),
3: ("auren.com.br","high"),
4: ("pecicero.com.br","medium"),
5: ("automob.com.br","high"),
6: ("portodesantos.com.br","high"),
7: ("avipam.com.br","high"),
8: (None,"not_found"),
9: ("avos.com.br","low"),
10: (None,"not_found"),
11: ("axia.com.br","high"),
12: ("azzas2154.com.br","high"),
13: ("azzas2154.com.br","high"),
14: ("azzas2154.com.br","high"),
15: ("zilor.com","high"),
16: ("b3.com.br","high"),
17: ("baerlocher.com","high"),
18: ("baldan.com.br","high"),
19: ("baldan.com.br","high"),
20: ("bradesco.com.br","high"),
21: ("btgpactual.com","high"),
22: ("bv.com.br","high"),
23: ("c6bank.com.br","high"),
24: ("daycoval.com.br","high"),
25: ("bancointer.com.br","high"),
26: ("itau.com.br","high"),
27: ("pine.com","medium"),
28: ("rendimento.com.br","medium"),
29: ("safra.com.br","high"),
30: ("santander.com.br","high"),
31: (None,"low"),
32: (None,"low"),
33: ("bat.com","medium"),
34: ("moura.com.br","high"),
35: ("bauducco.com.br","high"),
36: ("bauschlomb.com","medium"),
37: (None,"low"),
38: (None,"low"),
39: ("bbmlogistica.com.br","medium"),
40: (None,"low"),
41: (None,"low"),
42: ("be8.com.br","medium"),
43: ("befly.com.br","medium"),
44: ("belgoarames.com.br","medium"),
45: (None,"not_found"),
46: (None,"not_found"),
47: (None,"low"),
48: ("berneck.com.br","high"),
49: (None,"low"),
50: ("bettanin.com.br","high"),
51: (None,"not_found"),
52: ("bichara.adv.br","medium"),
53: (None,"not_found"),
54: ("bio.fiocruz.br","high"),
55: (None,"low"),
56: ("bionovis.com.br","medium"),
57: ("blau.com.br","high"),
58: ("blum.com","medium"),
59: ("blum.com","medium"),
60: ("bndes.gov.br","high"),
61: (None,"not_found"),
62: ("boasafra.agr.br","medium"),
63: ("bobst.com","high"),
64: (None,"low"),
65: (None,"low"),
66: (None,"low"),
67: ("borgwarner.com","high"),
68: ("bosch.com.br","high"),
69: ("boticario.com.br","high"),
70: (None,"not_found"),
71: (None,"low"),
72: (None,"low"),
73: ("bracell.com","high"),
74: ("bracell.com","high"),
75: ("bracell.com","high"),
76: ("bradescoseguros.com.br","high"),
77: ("brainfarma.com.br","medium"),
78: ("hypera.com.br","high"),
79: (None,"low"),
}

result = []
for i, name in enumerate(names):
    domain, conf = data[i]
    result.append({"name": name, "domain": domain, "confidence": conf})

with open('result_01.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("total:", len(result))
high = sum(1 for r in result if r["confidence"]=="high")
medium = sum(1 for r in result if r["confidence"]=="medium")
low = sum(1 for r in result if r["confidence"]=="low")
nf = sum(1 for r in result if r["confidence"]=="not_found")
print("high:", high, "medium:", medium, "low:", low, "not_found:", nf)
