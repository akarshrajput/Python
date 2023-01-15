import pickle			# imports the pickle library
Students = {"India":7}
fst = open("students.dat",'wb')
pickle.dump(Students, fst)		# Write each student 
fst.close()				# Close the output filr
fst = open("students.dat", 'rb')		# Open the file as input binary
data = pickle.load(fst)			# Read the first record
try:														# The Endof file is indicated as EOFError exception, we need to catch this exception
  while(True):
    print(data)
    data = pickle.load(fst)
except:
  print("Bye")