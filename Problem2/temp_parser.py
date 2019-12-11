import sys

def main():
  file = open(sys.argv[1], 'r')
  mini = sys.argv[2]
  totalval = 0;
  it = 0;
  underval = 0;
  for line in file.read().split('\n')[2:-1]:
    if int(line) < int(mini):
      underval += 1
    totalval += int(line)
    it += 1
  avg = float(totalval)/float(it)
  print("\tCPE 422/522 Final Exam")
  print("File name of sensor temperatures: " + str(sys.argv[1]))
  print("Number of tempreatures below " + str(mini) + " degrees C: " + str(underval))
  print("Average temperature: " + str(avg))

if __name__ == "__main__":
    main()
