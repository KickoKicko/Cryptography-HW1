eng_freq = {
        'A': 0.072, 'B': 0.013, 'C': 0.024, 'D': 0.037,
        'E': 0.112, 'F': 0.020, 'G': 0.018, 'H': 0.054,
        'I': 0.061, 'J': 0.001, 'K': 0.007, 'L': 0.035,
        'M': 0.024, 'N': 0.059, 'O': 0.066, 'P': 0.017,
        'Q': 0.001, 'R': 0.053, 'S': 0.056, 'T': 0.080,
        'U': 0.024, 'V': 0.009, 'W': 0.021, 'X': 0.001,
        'Y': 0.017, 'Z': 0.131
    }
eng_freq_modified = {
        'A': 0.072, 'B': 0.013, 'C': 0.024, 'D': 0.037,
        'E': 0.112, 'F': 0.020, 'G': 0.018, 'H': 0.054,
        'I': 0.061, 'J': 0.001, 'K': 0.007, 'L': 0.035,
        'M': 0.024, 'N': 0.059, 'O': 0.066, 'P': 0.017,
        'Q': 0.001, 'R': 0.053, 'S': 0.056, 'T': 0.080,
        'U': 0.024, 'V': 0.009, 'W': 0.021, 'X': 0.001,
        'Y': 0.017, 'Z': 0.231
    }

def kasiski_test(text,length):
    temp = ""
    ranges={}
    for i in range(len(text)-length+1):
        temp = text[i:i+length]
        for j in range(i+1,len(text)-length+1):
            if text[j:j+length] == temp:
                print(temp)
                if j-i in ranges: ranges[j-i] += 1
                else: ranges[j-i] = 1
    for key, value in sorted(ranges.items(), key=lambda item: item[1], reverse=True):
        print(key, value)


def decrypt(text,key):
    new_text= ""
    row= ""
    for i in range(len(text)):
        temp= chr((ord(text[i]) - 65 - (ord(key[i % len(key)]) - 65)) % 26 + 65)
        new_text += temp
        if temp == "Z": row+=" "
        else: row+=temp
        if(i%(len(key))==17): row = ""
    return new_text

def print_columns(text, length):
    for i in range(length):
        temp = ""
        for j in range(len(text)):
            if j%18==i:
                temp+=text[j]
        print(temp)

def print_rows(text,length):
    for i in range(int(len(text)/18)):
        print(text[i*18:(i+1)*18])
    print(text[len(text)-11:len(text)])

def english_score(text):
    counts = {chr(i): 0 for i in range(65, 91)}

    for c in text:
        counts[c] += 1

    distance = 0.0
    for letter in counts:
        observed = counts[letter] / len(text)
        expected = eng_freq[letter]
        distance += (observed - expected) ** 2 / expected

    return distance

def bigram_score(text):
    bigrams={"TH":0.036,"HE":0.031,"IN":0.024,"ER":0.021,"AN":0.020,"RE":0.019,"ON":0.018,
             "AT":0.015,"EN":0.015,"ND":0.014,"TI":0.013,"ES":0.013,"OR":0.013,"TE":0.012,
             "OF":0.012,"ED":0.012,"IS":0.011,"IT":0.011,"AL":0.011,"AR":0.011,"ST":0.011,
             "TO":0.011,"NT":0.010,"NG":0.010,"SE":0.009,"HA":0.009,"AS":0.009,"OU":0.009,
             "IO":0.008,"LE":0.008,"VE":0.008,"CO":0.008,"ME":0.008,"DE":0.008,"HI":0.008,
             "RI":0.007,"RO":0.007,"IC":0.007,"NE":0.007,"EA":0.007,"RA":0.007,"CE":0.007}
    
    counted = {"TH":0,"HE":0,"IN":0,"ER":0,"AN":0,"RE":0,"ON":0,
             "AT":0,"EN":0,"ND":0,"TI":0,"ES":0,"OR":0,"TE":0,
             "OF":0,"ED":0,"IS":0,"IT":0,"AL":0,"AR":0,"ST":0,
             "TO":0,"NT":0,"NG":0,"SE":0,"HA":0,"AS":0,"OU":0,
             "IO":0,"LE":0,"VE":0,"CO":0,"ME":0,"DE":0,"HI":0,
             "RI":0,"RO":0,"IC":0,"NE":0,"EA":0,"RA":0,"CE":0}

    for i in range(len(text)-1):
        temp = text[i:i+2]
        if temp in bigrams:
            counted[temp] +=1

    distance = 0.0
    for bi in bigrams:
        observed = counted[bi] / (len(text)-1)
        expected = bigrams[bi]
        distance += (observed - expected) ** 2 / expected
    return distance*2 # To make it more impactful

def trigram_score(text):
    trigrams={"THE":0.018,"AND":0.007,"THA":0.003,"ENT":0.004,"ING":0.007,"ION":0.004,"TIO":0.003,"FOR":0.003,"OFT":0.002,"STH":0.002}
    
    counted={"THE":0,"AND":0,"THA":0,"ENT":0,"ING":0,"ION":0,"TIO":0,"FOR":0,"OFT":0,"STH":0}

    for i in range(len(text)-2):
        temp = text[i:i+3]
        if temp in trigrams:
            counted[temp] +=1

    distance = 0.0
    for bi in trigrams:
        observed = counted[bi] / (len(text)-2)
        expected = trigrams[bi]
        distance += (observed - expected) ** 2 / expected
    return distance*10 # To make it more impactful


def best_for_index(text,ind):
    key = "AAAAAAAAAAAAAAAAAA"
    scores={}
    for i in range(26):
        key = key[:ind]+chr(i+65)+key[ind+1:]
        scores[chr(i+65)] = english_score(decrypt(text,key)) + bigram_score(decrypt(text,key)) + trigram_score(decrypt(text,key))

    bottom_3 = dict(sorted(scores.items(), key=lambda item: item[1])[:5])

    print(bottom_3)

def manual_slideshow(text,iter):
    plaintext = open("unknown2.txt").read()
    letter =["MFURN","AEYRM","MTFAH","UIGNP","QBNUW","EQXSJ","GUMYK","FKYTN","PGITE","FTYXC","RMFIA","FCXEO","GMIYR","YERXQ","FMTWA","ZGXSL","RFDKW","PIWBG"]
    #letter =["MFURN","AEYRM","TTTTT","UIGNP","QBNUW","EQXSJ","GUMYK","FKYTN","PGITE","FTYXC","RMFIA","FCXEO","GMIYR","YERXQ","FMTWA","UUUUU","RFDKW","PIWBG"]
    mini = 1000
    bestkey=""
    for a in range(iter):
        for b in range(iter):
            for c in range(iter):
                for d in range(iter):
                    for e in range(iter):
                        for f in range(iter):
                        #key = letter[0][a]+letter[1][b]+letter[2][c]+letter[3][d]+letter[4][e]+ "AAAAAAAAAAA"
                                #key = letter[0][a]+letter[1][b]+letter[2][c]+letter[3][d]+letter[4][e]+letter[5][f]+letter[6][g]+letter[7][h]+letter[8][i]+"AAAAAAA"
                            key = letter[0][a]+letter[1][b]+letter[2][c]+letter[3][d]+letter[4][e]+letter[5][f]+"AAAAAAAAAAAA"
                            #key = "AAAAAAAAAAAA"+letter[12][a]+letter[13][b]+letter[14][c]+letter[15][d]+letter[16][e]+letter[17][f]
                            #key = "AAAAAA"+letter[6][a]+letter[7][b]+letter[8][c]+letter[9][d]+letter[10][e]+letter[11][f]+"AAAAAA"
#
                            decrypted_text = decrypt(plaintext,key)
                            val = english_score(decrypted_text)+ bigram_score(decrypted_text) + trigram_score(decrypted_text)
                            if val < mini: 
                                mini = val
                                bestkey = key
#
                        #input()
    
    print(mini)
    print(bestkey)

def manual_slideshow2():
    plaintext = open("unknown2.txt").read()
    mini = 1000
    bestkey=""
    for a in range(26):
        for b in range(26):
            for c in range(26):
                #   UEMUQXGMEXTFZRFGRP
                key = "UEMUQXGMEXTFZRF"+chr(a+65)+chr(b+65)+chr(c+65)+ ""
                decrypted_text = decrypt(plaintext,key)
                val = english_score(decrypted_text)+ bigram_score(decrypted_text) + trigram_score(decrypted_text)
                if val < mini: 
                    mini = val
                    bestkey = key
#    
    print(mini)
    print(bestkey)




plaintext = open("unknown2.txt").read()

testKey = "EELHJKQXOPEBKNEKJO" 
testKey2 = "GNDWNIBFLWBIGNDWBI"
testKey3 = "VZEYRYHOFGFGHGVBAF"
testKey4 = "VZEYRYGYAGFGHGVPAF"
testKey5 = "URPLQEGNXTIFGYASLW"
testKey6 = "MUVUQVJHEXPYAFRGAW"
testKey7 = "TQAAQTPRTGXFGXTSRV"
testKey8 = "NYHIQXHGXXNFZGATAX"

tempKey = "NYHIQWHAAAAFNFRGML"
tempKey2 = "NYHIQWYNLGNFNFRGML"
tempKey3 = "NZZIQWYGLGNFRYULAF" # 0.01515833333333333
tempKey4 = "MEMUQXGFTFFFIYRGRS" # 0.8615864436458807  New
#"UEMUQXGMEXTFZRFGRP" 1.711 with all three
bestKey = "UEMUQXGMEXTFZRFGRP"

buildKey ="MEMUQXGFPFRCGYFZRP"




manualkey="UEMUQXGMEXTFZRFGRP"
decrypted_text = decrypt(plaintext,bestKey)
#print_columns(decrypted_text,18)
#print()

print_rows(decrypted_text.replace("Z", " "),18)
print(english_score(decrypted_text))
print(bigram_score(decrypted_text))
print(trigram_score(decrypted_text))
print(english_score(decrypted_text)+bigram_score(decrypted_text)+trigram_score(decrypted_text))




#best_for_index("ABC",0)

#for i in range(18):
#    best_for_index(plaintext,i)

#manual_slideshow(decrypted_text,5)
#manual_slideshow2()


#kasiski_test(plaintext,10)

#print(bigram_score(plaintext))
#
#print()
#print(english_score(decrypted_text))
#print(bigram_score(decrypted_text))
#print(trigram_score(decrypted_text))
#

