#!/usr/bin/python

####This is a python script for a web-based tool - NetDNA-1.0, that will generate useful biological data from the query DNA sequence#####

####Importing Libraries and python modules####
import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image
from Bio.Seq import Seq

###Creating a Page title, logo and information about the web application###
Picture  = Image.open('DNA.jpeg')

####Displaying and Extending the image along the column width###
st.image(Picture, use_column_width=True)

###Writing a header about the web program###
st.write("""
***
# NetDNA-1.0
This is a web-based tool that uses the query DNA sequence to generate basic biological data:
\n- Length of the Sequence
\n- Count of Non-bases(if any)
\n- Nucleotide Base-Count & its visualization
\n- GC Content(%)
\n- Melting Temperature(Tm)
\n- Reverse Complement
\n- Transcribed Sequence
\n- Translated Sequence
***
""")

###Creating a Text-box to get user input###

#Header for the input sequence
st.header("Please enter your DNA sequence:")

user_input = ''
DNA_Sequence = st.text_area("Input", user_input, height = 275)
st.write("**Note**: Entering a Non-DNA sequence might display wrong results from step-7 (Results section)")

st.write("""
***
""")

###Converting the data to Upper case###
DNA_Sequence = DNA_Sequence.upper()

###Removing All White Spaces###
DNA_Sequence = ''.join(DNA_Sequence.split())

###Displaying unknown characters(i.e any character other than 'A|T|G|C') in the query sequence###
for a in range(len(DNA_Sequence)):
    if DNA_Sequence[a] not in 'ATGC':
        st.write("**WARNING**: Your DNA sequence contains unknown character '**%s**' at position %d\n" % (DNA_Sequence[a],a))

st.write("""
***
""")

st.header("This is your DNA sequence:")
DNA_Sequence

st.write("""
***
""")

###Displaying the Results###
st.header("--**RESULTS**--")

#Displaying the length of the given DNA Sequence
length_DNA = len(DNA_Sequence)
st.subheader("[1] Length of the given DNA sequence: ")
st.write(length_DNA," bases")

st.write("""
***
""")

###Counting Non-bases in the sequence###
Base_Count = (DNA_Sequence.count('A') + DNA_Sequence.count('T') + DNA_Sequence.count('G') + DNA_Sequence.count('C'))
Non_Bases = (length_DNA - Base_Count)

#Displaying the count of Non-bases
st.subheader("[2] Number of Non-Bases in the given DNA Sequence: ")
st.write(Non_Bases, " Non bases")

st.write("""
***
""")

#Displaying the Nucleotide Base Count in the given DNA Sequence
st.subheader("[3] Nucleotide Base Count of the given DNA Sequence:")
st.write("- Number of Adenine(A):", DNA_Sequence.count('A'))
st.write("- Number of Thymine(T):", DNA_Sequence.count('T'))
st.write("- Number of Guanine(G):", DNA_Sequence.count('G'))
st.write("- Number of Cytosine(C):", DNA_Sequence.count('C'))

st.write("""
***
""")

###Creating a dataframe of the Nucleotide base count for Graphical visualization###
data = {
            'Nucleotide Base':  ['A', 'T', 'G', 'C'],
            'Count': [DNA_Sequence.count('A'), DNA_Sequence.count('T'), DNA_Sequence.count('G'), DNA_Sequence.count('C')]
        }
df = pd.DataFrame (data, columns = ['Nucleotide Base','Count'])


###Graphical Representation of the base count###
st.subheader("[4] Graphical Representation of the Nucleotide Base count")
Graph = alt.Chart(df).mark_bar().encode(x = 'Nucleotide Base', y = 'Count')

#Adjusting the size of the bars in the Graph
Graph = Graph.properties(width = alt.Step(75))

#Displaying the Graph
st.write(Graph)

st.write("""
***
""")

###GC Content of the given DNA Sequence###
C_count = DNA_Sequence.count('C') ####Counting Cytosine###
G_count = DNA_Sequence.count('G') ####Counting Guanine###

try:
    GC_content = (C_count+G_count)/length_DNA*100
except:
    GC_content = 0

st.subheader("[5] GC content of the given DNA Sequence")
st.write("-The GC content in the given DNA Sequence: %5.2f%%" % GC_content)

st.write("""
***
""")

###Melting Temperature(Tm)###
st.subheader("[6] Melting Temperature (Tm)")
if (length_DNA<14):
      try:
          Tm_less = (DNA_Sequence.count('A') + DNA_Sequence.count('T'))*2 + (DNA_Sequence.count('C') + DNA_Sequence.count('G')) * 4
      except:
          Tm_less = 0
      st.write("-The Melting Temperature(Tm) of the given DNA sequence: ", Tm_less, "°C")
else:
      try:
          Tm_more = 64.9 +41*(DNA_Sequence.count('G')+DNA_Sequence.count('C')-16.4)/(DNA_Sequence.count('A')+DNA_Sequence.count('T')+DNA_Sequence.count('G')+DNA_Sequence.count('C'))
      except:
          Tm_more = 0
      st.write("-The Melting Temperature(Tm) of the given DNA sequence: ", Tm_more, "°C")

st.write("""
***
""")

###Reverse Complement of the given DNA Sequence###
DNA_Sequence = Seq(DNA_Sequence)

st.subheader("[7] Reverse Complement of the given DNA Sequence")
st.write(DNA_Sequence.reverse_complement())

st.write("""
***
""")

###Transcribed Sequence of the given data###
st.subheader("[8] Transcribed Sequence (DNA -> RNA)")
st.write(DNA_Sequence.transcribe())

st.write("""
***
""")

###Translated Sequence of the given data###
st.subheader("[9] Translated Sequence (RNA -> Protein)")
st.write(DNA_Sequence.translate())

st.write("""
***
""")

###Displaying the Amino acid codes###
AA_Code  = Image.open('AA-Codes.jpeg')
st.image(AA_Code, use_column_width=True)
st.write("(* or asterisk) = 'Stop codon' or 'Termination codon' ")

###END###
