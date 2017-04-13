from nltk import CFG

m_Grammer = CFG.fromstring("""

S -> VP NP
S -> VP ADJP
VP -> V
NP -> NN ADJP|Det+NN|NN|NN NP 
ADJP -> NN Adj|NP Det+Adj|NP Adj|Det+NN Det+Adj
 
V -> 'حضرت'| 'رأيت'|'فاز'
NN ->'كاتبة'|'قصص'|'حصان'|'صاحب'|'مارد'
Adj -> 'عملاق'|'وفي'|'رائع'|'رشيق'|'علاقية'
Det+Adj -> 'الرائعة'
Det+NN -> 'الحديقة'

""")
