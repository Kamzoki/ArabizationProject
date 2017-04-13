from __future__ import unicode_literals
from nltk import CFG

m_Grammer = CFG.fromstring("""

S -> VP NP
S -> VP ADJP
VP -> V
NP -> NN ADJP|NN|NN NP| DetNN
ADJP -> NN Adj|NP|NP Adj|DetNN DetAdj| NP DetAdj
 
V -> 'حضرت'| 'رأيت'|'فاز'
NN ->'كاتبة'|'قصص'|'حصان'|'صاحب'|'مارد'
Adj -> 'عملاق'|'وفي'|'رائع'|'رشيق'|'علاقية'
DetAdj -> 'الرائعة'
DetNN -> 'الحديقة'
""")
