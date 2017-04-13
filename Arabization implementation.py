from __future__ import unicode_literals
from nltk import CFG
from nltk.parse import RecursiveDescentParser

m_Grammar = CFG.fromstring("""

S -> VP NP|NP VP|VP ADJP|NP ADJP
VP -> V
NP -> NN ADJP|NN|NN NP| DetNN
ADJP -> NN Adj|NP|NP Adj|DetNN DetAdj| NP DetAdj

V -> 'حضرت'| 'رأيت'|'فاز'
NN ->'كاتبة'|'قصص'|'حصان'|'صاحب'|'مارد'
Adj -> 'عملاق'|'وفي'|'رائع'|'رشيق'|'علاقية'
DetAdj -> 'الرائعة'
DetNN -> 'الحديقة'
""")

def fn_RDP(sent):
    sent.split()
    rd = RecursiveDescentParser (m_Grammar)
    for w in rd.parse(sent):
        print(w)