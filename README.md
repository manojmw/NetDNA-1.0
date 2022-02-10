# NetDNA-1.0
This is a basic python script for the web-based tool (I call it NetDNA-1.0). It can easily run on Streamlit, and generates basic biological data from the query DNA sequence.<br/><br/>

<p align = "center">
  <img src = "https://user-images.githubusercontent.com/74168582/144679110-785d104f-2806-4708-91c1-2d8019f9ddcd.jpeg" width="600" height="350">
</p>

<br/><br/>

## Following details are obtained from the query DNA sequence:
 - Length of the Sequence
 - Count of Non-bases(if any)
 - Nucleotide Base-Count & its visualization
 - GC Content(%)
 - Melting Temperature(Tm)
 - Reverse Complement
 - Transcribed Sequence
 - Translated Sequence


## Configuration and running the script
Please refer to the following guide - [Streamlit Documentation](https://docs.streamlit.io/library/get-started/installation) to configure **Streamlit**.

<br/>

Once streamlit is configured, download the above files and place it in a directory.

<br/>

Go to the above directory and run the script using the command:
> streamlit run NetDNA-1.0.py
<br/>

This will open the tool in the browser as a web-based tool!

<br/>

## Below figure shows an example of random DNA sequence (length = 1000 bp) as an input to the tool</b>

<img src = "https://user-images.githubusercontent.com/74168582/144680572-3b5c2059-12bf-4810-aab5-583d285be716.png" width="450" height="300">
<br/>

## Output of the tool

<img src="https://user-images.githubusercontent.com/74168582/144681464-a0fb438e-3e22-42d6-8003-209dd6e0a6f7.png" width="950" height="375">

<br/>

<img src="https://user-images.githubusercontent.com/74168582/144681902-14c4540e-fada-4b5c-a716-26d06a9d4bf3.png" width="950" height="375">

**Note:** Calculation of Melting Temperature(Tm) is just an example, because Tm is usually calculated for primers (typically 18-30 bp in length) and not the whole DNA sequence as in the below example.
<br/><br/>
