class Main_sub:
    N_O_MS=0
    def __init__(self,fname,lname,_P,_C,_M):
        self.fname=fname
        self.lname=lname
        self._P=_P
        self._C=_C
        self._M=_M
        Main_sub.N_O_MS+=1
    @classmethod
    def from_str(cls,emp_string):
        fname,lname,_P,_C,_M=emp_string.split("-")
        return cls(fname,lname,_P,_C,_M)
M1=Main_sub.from_str("Name1-Sname1   -A1-B1-C1")
M2=Main_sub.from_str("Name2-Sname2   -D1-E1-F1")
M3=Main_sub.from_str("Name3-Sname3   -G1-H1-I1")
M4=Main_sub.from_str("Name4-Sname4   -J1-K1-L1")
M5=Main_sub.from_str("Name5-Sname5   -M1-N1-O1")
M6=Main_sub.from_str("Name6-Sname6   -P1-Q1-R1")
M7=Main_sub.from_str("Name7-Sname7   -S1-T1-U1")
M8=Main_sub.from_str("Name8-Sname8   -V1-W1-X1")
T_N_O_S=[M1,M2,M3,M4,M5,M6,M7,M8]
# Please don't write anything below this comment.
P_W_1=int(input("Enter class passcode: "))    #[P A S S C O D E = "12345678"]
if P_W_1==int(0b101111000110000101001110):
    S_1=input("Type 'yes' for accessing data: ")
    if S_1=="yes":
        for i in T_N_O_S:
            print(i.fname,i.lname,"//","Physics:",i._P,"Chemistry:",i._C,"Maths:",i._M)
        print("Total number of Students in Main Subject:",Main_sub.N_O_MS)
else:
    print("You are not allowed to view Data")

class Additional_sub(Main_sub):
    N_O_AS=0
    def __init__(self, fname, lname, _P, _C, _M, _Com, _Eng):
        super().__init__(fname, lname, _P, _C, _M)
        self._Com=_Com
        self._Eng=_Eng
        Additional_sub.N_O_AS+=1
    @classmethod
    def from_str1(cls,emp_string):
        fname,lname,_P,_C,_M,_Com,_Eng=emp_string.split("-")
        return cls(fname,lname,_P,_C,_M,_Com,_Eng)
A1=Additional_sub.from_str1("Name1-Sname1   -Y1-Z1-A2-B2-C2")
A2=Additional_sub.from_str1("Name2-Sname2   -D2-E2-F2-G2-H2")
A3=Additional_sub.from_str1("Name3-Sname3   -I2-J2-K2-L2-M2")
A4=Additional_sub.from_str1("Name4-Sname4   -N2-O2-P2-Q2-R2")
T_N_O_AS=[A1,A2,A3,A4]
for i in T_N_O_AS:
    print(i.fname,i.lname,"//","Physics:",i._P,"Chemistry:",i._C,"Maths:",i._M,"Computer:",i._Com,"English:",i._Eng)
print("Total number of Students in all Subject:",Additional_sub.N_O_AS)