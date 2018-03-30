Sbox = [
    '63' ,'7C' ,'77' ,'7B' ,'F2' ,'6B' ,'6F' ,'C5' ,'30' ,'01' ,'67' ,'2B' ,'FE' ,'D7' ,'AB' ,'76' ,
    'CA' ,'82' ,'C9' ,'7D' ,'FA' ,'59' ,'47' ,'F0' ,'AD' ,'D4' ,'A2' ,'AF' ,'9C' ,'A4' ,'72' ,'C0' ,
    'B7' ,'FD' ,'93' ,'26' ,'36' ,'3F' ,'F7' ,'CC','34' ,'A5' ,'E5' ,'F1' ,'71' ,'D8' ,'31' ,'15' ,
    '04' ,'C7' ,'23' ,'C3' ,'18' ,'96' ,'05' ,'9A' ,'07' ,'12' ,'80','E2'
    ,'EB' ,'27' ,'B2' ,'75',' 09' ,'83' ,'2C' ,'1A' ,'1B' ,'6E' ,'5A' ,'A0' ,'52' ,'3B' ,'D6' ,'B3' ,'29' ,'E3' ,'2F','84'
    ,'53' ,'D1' ,'00' ,'ED' ,'20' ,'FC' ,'B1' ,'5B' ,'6A' ,'CB' ,'BE' ,'39' ,'4A' ,'4C' ,'58' ,'CF','D0' ,'EF' ,'AA' ,'FB'
    ,'43' ,'4D' ,'33' ,'85' ,'45' ,'F9' ,'02' ,'7F' ,'50' ,'3C' ,'9F' ,'A8' ,'51' ,'A3' ,'40' ,'8F' ,'92' ,'9D' ,'38','F5'
    ,'BC' ,'B6' ,'DA' ,'21' ,'10' ,'FF' ,'F3' ,'D2','CD' ,'0C' ,'13' ,'EC' ,'5F' ,'97' ,'44' ,'17' ,'C4' ,'A7' ,'7E' ,'3D'
    ,'64' ,'5D' ,'19' ,'73' ,'60' ,'81' ,'4F' ,'DC','22' ,'2A' ,'90' ,'88' ,'46' ,'EE' ,'B8' ,'14' ,'DE' ,'5E' ,'0B' ,'DB'
    ,'E0' ,'32' ,'3A' ,'0A' ,'49' ,'06' ,'24' ,'5C' ,'C2' ,'D3' ,'AC' ,'62' ,'91' ,'95' ,'E4' ,'79' ,'E7' ,'C8' ,'37' ,'6D'
    ,'8D' ,'D5' ,'4E' ,'A9' ,'6C' ,'56' ,'F4' ,'EA' ,'65' ,'7A' ,'AE' ,'08','BA' ,'78' ,'25' ,'2E' ,'1C' ,'A6' ,'B4' ,'C6'
    ,'E8' ,'DD' ,'74' ,'1F' ,'4B' ,'BD' ,'8B' ,'8A' ,'70' ,'3E' ,'B5' ,'66' ,'48' ,'03' ,'F6' ,'0E' ,'61' ,'35' ,'57' ,'B9'
    ,'86' ,'C1' ,'1D' ,'9E','E1' ,'F8' ,'98' ,'11' ,'69' ,'D9' ,'8E' ,'94' ,'9B' ,'1E' ,'87' ,'E9' ,'CE' ,'55' ,'28' ,'DF'
    ,'8C' ,'A1' ,'89' ,'0D' ,'BF' ,'E6' ,'42' ,'68' ,'41' ,'99' ,'2D' ,'0F' ,'B0' ,'54' ,'BB' ,'16'
]

Sboxi = [ '52',' 09',' 6a',' d5',' 30',' 36',' a5',' 38',' bf',' 40',' a3',' 9e',' 81',' f3',' d7',' fb',' 7c',' e3',' 39',' 82',' 9b',' 2f',' ff',' 87',' 34',' 8e',' 43',' 44',' c4',' de',' e9',' cb',' 54',' 7b',' 94',' 32',' a6',' c2',' 23',' 3d',' ee',' 4c',' 95',' 0b',' 42',' fa',' c3',' 4e',' 08',' 2e',' a1',' 66',' 28',' d9',' 24',' b2',' 76',' 5b',' a2',' 49',' 6d',' 8b',' d1',' 25',' 72',' f8',' f6',' 64',' 86',' 68',' 98',' 16',' d4',' a4',' 5c',' cc',' 5d',' 65',' b6',' 92',' 6c',' 70',' 48',' 50',' fd',' ed',' b9',' da',' 5e',' 15',' 46',' 57',' a7',' 8d',' 9d',' 84',' 90',' d8',' ab',' 00',' 8c',' bc',' d3',' 0a',' f7',' e4',' 58',' 05',' b8',' b3',' 45',' 06',' d0',' 2c',' 1e',' 8f',' ca',' 3f',' 0f',' 02',' c1',' af',' bd',' 03',' 01',' 13',' 8a',' 6b',' 3a',' 91',' 11',' 41',' 4f',' 67',' dc',' ea',' 97',' f2',' cf',' ce',' f0',' b4',' e6',' 73',' 96',' ac',' 74',' 22',' e7',' ad',' 35',' 85',' e2',' f9',' 37',' e8',' 1c',' 75',' df',' 6e',' 47',' f1',' 1a',' 71',' 1d',' 29',' c5',' 89',' 6f',' b7',' 62',' 0e',' aa',' 18',' be',' 1b',' fc',' 56',' 3e',' 4b',' c6',' d2',' 79',' 20',' 9a',' db',' c0',' fe',' 78',' cd',' 5a',' f4',' 1f',' dd',' a8',' 33',' 88',' 07',' c7',' 31',' b1',' 12',' 10',' 59',' 27',' 80',' ec',' 5f',' 60',' 51',' 7f',' a9',' 19',' b5',' 4a',' 0d',' 2d',' e5',' 7a',' 9f',' 93',' c9',' 9c',' ef',' a0',' e0',' 3b',' 4d',' ae',' 2a',' f5',' b0',' c8',' eb',' bb',' 3c',' 83',' 53',' 99',' 61',' 17',' 2b',' 04',' 7e',' ba',' 77',' d6',' 26',' e1',' 69',' 14',' 63',' 55',' 21',' 0c',' 7d' ]

Rcon = [
    '00', '01', '02', '04', '08', '10', '20', '40',
    '80', '1B', '36', '6C', 'D8', 'AB', '4D' , '9A',
    '2F', '5E', 'BC', '63', 'C6', '97','35', '6A',
    'D4', 'B3', '7D', 'FA', 'EF', 'C5', '91' , '39']

mix = [['02' ,'03', '01' ,'01'],['01', '02', '03', '01'],['01' ,'01', '02' ,'03'] ,['03' ,'01', '01' ,'02']]
hex2bin_map = {
   "0":"0000",
   "1":"0001",
   "2":"0010",
   "3":"0011",
   "4":"0100",
   "5":"0101",
   "6":"0110",    
   "7":"0111",
   "8":"1000",
   "9":"1001",
   "A":"1010",
   "B":"1011",
   "C":"1100",
   "D":"1101",
   "E":"1110",
   "F":"1111",
}

matrix = [['63', 'EB', '9F', 'A0'], ['2F', '93', '92', 'C0'], ['AF', 'C7', 'AB', '30'], ['A2', '20', 'CB', '2B']]
    
def fix (bytearray) :
    a= []
    for i in range(16):
        if(len(bytearray[i])<2):
         a.append('0'+bytearray[i])
        else :
            a.append(bytearray[i])
    return a
    

#converts TEXT to HEX 128 bit
def into_hex(String):
    bytearray = []
    for c in String :
        bytearray.append("".join("{:02x}".format(ord(c)) ))
    return bytearray
 
#xors colmons 
def xor(hex1, hex2):
    xored = []
    for col in range (len(hex1)):
        xored.append("%x" % (int(hex1[col], 16) ^ int(hex2[col], 16)))
    a=[]    
    for i in range(len(xored)):
        if(len(xored[i])<2):
         a.append('0'+xored[i])
        else :
            a.append(xored[i])
    return a

def dot(string1,string2):
    dot=""
    a = int("".join(hex2bin_map[i] for i in string1),2)%255
    b = int("".join(hex2bin_map[i] for i in string2),2)%255
    if(a==1) :
        #print("t") 
        dot=string2

    if (a==2): 
       # print("t1")
        #print (a)
        #print (b)
        #print((b << 1)%255)
        dot=("%X" % ((b << a-1)%255))
    if (a==3) :
        #print (a)
        #print (b)
        #print (((b << a-2))%255)
        s=("%X" % ((b << a-2)%255))
      
        dot=("%X" % ((int(string2, 16) ^ int(s, 16))))
       
    return dot


def mixcolum(mix,matirx):
    result =[['00' ,'00', '00' ,'00'],['00', '00', '00', '00'],['00' ,'00', '00' ,'00'] ,['00' ,'00', '00' ,'00']]
    # result =[]
    # iterate th    [gh rows of X
    for i in range(len(mix)):
   # iterate through columns of Y
        for j in range(len(matirx[0])):
       # iterate through rows of Y
            for k in range(len(matirx)):
                #print (" "+str(i)+" "+str(j)+" "+str(k))
                #print ("res "+ result[i][j]+ "  XOR mix "+mix[i][k]+" . "+"matrx "+matirx[k][j]+ " = "+ dot(mix[i][k], matirx[k][j]))
            
                
                
                result[i][j] =("%X" % (int(result[i][j], 16) ^ int(dot(mix[i][k], matirx[k][j]), 16))) 
                #print (result[i][j])
               
    return (result)
    
#converts bytearray into matrix
def into_matrix(bytearray):
    a = []
    b = []
    c = []
    d = []
    matrix = [a,b,c,d]
    for i in range (16):
        if(i%4==0): a.append(bytearray[i])
        if(i%4==1): b.append(bytearray[i])
        if(i%4==2): c.append(bytearray[i])
        if(i%4==3): d.append(bytearray[i])
        
    return matrix

    
def leftshift(s) :
    return [s[1],s[2],s[3],s[0]]

def to_int(char):
    if(ord(char)-ord('0')<=9):
        return ord(char)-ord('0')
    else :
        return ord(char)-ord('A')+10

def s_box(hex1):
    sboxed = []
    for i in range (len(hex1)):
        a= to_int(hex1[i][0])
        b= to_int(hex1[i][1])

        sboxed.append(Sbox[(a*16)+b])

    return sboxed
def g(hex1,roundNO):
    x = [Rcon[roundNO],'00','00','00']
    #x[0][1]=
  
    return xor(s_box(leftshift(hex1)),x)


def into_w(bytearray):
  a = []
  b = []
  c = []
  d = []
  w = [a,b,c,d]
  for i in range (16):
      if(i in range(0,4)): a.append(bytearray[i])
      if(i in range(4,8)): b.append(bytearray[i])
      if(i in range(8,12)): c.append(bytearray[i])
      if(i in range(12,16)): d.append(bytearray[i])
      
        
  return w
    
def key_round(bytearray,roundNO):
    w = into_w(bytearray)
    key_round = []
    g_w3 = g(w[3],roundNO)
    
    
    w4= xor(w[0],g_w3)
    w5= xor(w4,w[1])
    w6= xor(w5,w[2])
    w7=xor(w6,w[3])
    
    key_round.extend(w4)
    key_round.extend(w5)
    key_round.extend(w6)
    key_round.extend(w7)
    
    z=[x.upper() for x in key_round]
    
    return fix(z)

def key_roundat(key0):
  key_roundat=[]
  key_roundat.append(key0)
  for i in range (1,11):
    key_roundat.append(key_round(key_roundat[(i-1)],i))
  return key_roundat
  
  
def AddRoundkey(matrix,key_roundat,roundNO):
  added=[]
  for i in range (4) :
    added.append(xor(key_roundat[i],statematrix[i]))
  return added
  
def SubstitutionBytes (matrix):
  subed=[]
  for i in range (4) :
    subed.append(s_box(matrix[i]))
  return subed
  
def Shiftrow(matrix):
  a=[matrix[0][0],matrix[0][1],matrix[0][2],matrix[0][3]]
  b=[matrix[1][1],matrix[1][2],matrix[1][3],matrix[1][0]]
  c=[matrix[2][2],matrix[2][3],matrix[2][0],matrix[2][1]]
  d=[matrix[3][3],matrix[3][0],matrix[3][1],matrix[3][2]]
  shifted= [a,b,c,d]
  return shifted
  
#hex1=['67', '20', '46', '75']
#sboxed = g(hex1)
#print(sboxed) : 56 08 20 07 C7 1A B1 8F 76 43 55 69 A0 3A F7 FA
with open('Key', 'r') as f:
    key = f.read().rstrip()

with open('Message', 'r') as f:
    plaintext =f.read().rstrip()


key0= (into_hex(key))
key_roundat=key_roundat(key0)

statematrix= into_matrix(into_hex(plaintext))

key00 = into_matrix(key0)

xored0=[]
for i in range (4) :
    xored0.append(xor(key00[i],statematrix[i]))
xored00=[]    
for i in range(4):    
  z=[x.upper() for x in xored0[i]]
  xored00.append(z)

with open('aes', 'w') as fw:
    fw.write (str(key_roundat)+ '\n')
    fw.write (str(xored00)+ '\n')
    fw.write (str(SubstitutionBytes(xored00))+ '\n')
    fw.write (str(Shiftrow(SubstitutionBytes(xored00)))+ '\n')
    fw.write (str(mixcolum(mix,Shiftrow(SubstitutionBytes(xored00))))+ '\n')



 #   4 73 20 6D 79 20 4B 75 6E 67 20 46 75
#Round 1: E2 32 FC F1 91 12 91 88 B1 59 E4 E6 D6 79 A2 93
# Round 2: 56 08 20 07 C7 1A B1 8F 76 43 55 69 A0 3A F7 FA
# Round 3: D2 60 0D E7 15 7A BC 68 63 39 E9 01 C3 03 1E FB
# Round 4: A1 12 02 C9 B4 68 BE A1 D7 51 57 A0 14 52 49 5B
# Round 5: B1 29 3B 33 05 41 85 92 D2 10 D2 32 C6 42 9B 69
# Round 6: BD 3D C2 B7 B8 7C 47 15 6A 6C 95 27 AC 2E 0E 4E
# Round 7: CC 96 ED 16 74 EA AA 03 1E 86 3F 24 B2 A8 31 6A
# Round 8: 8E 51 EF 21 FA BB 45 22 E4 3D 7A 06 56 95 4B 6C
# Round 9: BF E2 BF 90 45 59 FA B2 A1 64 80 B4 F7 F1 CB D8
# Round 10: 28 FD DE F8 6D A4 24 4A CC C0 A4 FE 3B 31 6F 26

