from __future__ import unicode_literals
from nltk import CFG
from nltk.corpus import wordnet as wn
from nltk.parse import RecursiveDescentParser
from nltk.parse import ShiftReduceParser
from nltk.parse import LeftCornerChartParser
from nltk.parse import EarleyChartParser

m_Grammar = CFG.fromstring("""

S -> VP NP|NP VP|VP ADJP|NP ADJP
VP -> V
NP -> NN ADJP|NN|NN NP| Det NN 
ADJP -> NN Adj|NP|NP Adj|Det NN Adj|Det Adj 

V ->'is'|'barking'|'moving'|'burning'|'am'|'are'|'have'
NN ->'money'|'cat'|'car'|'dog'|'house'
Adj ->'cute'|'buffoon'|'bad'|'good'|'broke'|'poor'
Det -> 'the'|'a'|'an'|'no'
""")


def fn_RDP(sent,word):
    rd = RecursiveDescentParser (m_Grammar)
    for w in rd.parse(sent):
        print(w)
    fn_PP(sent,word)

def fn_PP(sent,word):
    #sentA=sent
    wordSyns=wn.synsets(word);
    for syn in wordSyns:
        wordLemmaNames=syn.lemma_names()
        for w in sent:
            if(w==word):
                sent[sent.index(w)]=wordLemmaNames[0]
                word = wordLemmaNames[0]
        print(sent)
def fn_SRP(sent):
    sr=ShiftReduceParser (m_Grammar)
    for w in sr.parse (sent):
        print (w)
def fn_LCP (sent):
    lcp=LeftCornerChartParser (m_Grammar)
    for w in lcp.parse (sent):
        print(w)
def fn_ECP(sent):
    ecp= EarleyChartParser (m_Grammar)
    for w in ecp.parse (sent):
        print (w)