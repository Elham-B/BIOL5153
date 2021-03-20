#!/usr/bin/env python



import os
# set a name of input DNA file
filename = 'dna.txt'


# In[122]:


# open the input file assign to file handel call infile
infile = open(filename, 'r')
# print(infile)


# In[123]:


# read the file
dna_sequence = infile.read().rstrip()

# dna-sequence = dna_sequence.rstrip()


# In[124]:


print(dna_sequence)


# In[125]:


# close the file
infile.close()
print(dna_sequence)


# In[126]:


seqlen = len(dna_sequence)


# In[127]:


print("lenght of DNA sequence", seqlen)


# In[128]:


print(dna_sequence.count('A'))
numA = dna_sequence.count('A')


# In[129]:


print(dna_sequence.count('G'))
numG = dna_sequence.count('G')


# In[130]:


print(numG)


# In[131]:


print(dna_sequence.count('T'))
numT = dna_sequence.count('T')


# In[132]:


print(dna_sequence.count('C'))
numC = dna_sequence.count('C')


# In[133]:


# G + C
print(numG + numC)


# In[134]:


print("the number of A's in", filename + ":", numA)


# In[135]:


print(numA / seqlen)
freqA = numA / seqlen


# In[136]:


print(numG / seqlen)
freqG = numG / seqlen


# In[137]:


print(numC / seqlen)
freqC = numC / seqlen


# In[138]:


print(numT / seqlen)
freqT = numT / seqlen


# In[139]:


print(freqG + freqC)


# In[140]:


print(freqG + freqC + freqA + freqT)


# In[141]:


outfile = open('my_first_output.txt', 'w')


# In[142]:


outfile.write('DNA sequence:'+ dna_sequence +'\n')
outfile.write('sequence lenght:' + str(seqlen) + 'nt'+ '\n')
outfile.write("Number of A's :" + str(numA) + '\n')


# In[143]:


outfile.close()


# In[ ]:




