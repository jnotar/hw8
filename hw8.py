#!/usr/bin/python

from __future__ import division 

def get_at_content(dna, sig_figs): #define function w/ arguments for dna and significant figures
    length = len(dna) #calculate length of dna sequence
    a_count = dna.upper().count("A") #count A bases, even if lowercase
    t_count = dna.upper().count("T") #count T bases, even if lowercase
    at_content = (a_count + t_count) / length #calculate AT content
    return round(at_content, sig_figs) #return rounded AT content, to # of sig figs

