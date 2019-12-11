import csv

report = open("report.txt", "w")

with open('raw_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    data = 0
    for row in csv_reader:
      if line_count == 0:
        line_count = 1
      elif line_count == 1:
        line_count = 2
      elif line_count == 2:
        max1 = int(row[0])
        max2 = int(row[1])
        max3 = int(row[2])
        max4 = int(row[3])
        max5 = int(row[4])
        min1 = int(row[0])
        min2 = int(row[1])
        min3 = int(row[2])
        min4 = int(row[3])
        min5 = int(row[4])
        sum1 += int(row[0])
        sum2 += int(row[1])
        sum3 += int(row[2])
        sum4 += int(row[3])
        sum5 += int(row[4])
        data += 1
        line_count = 3
      else:
        sum1 += int(row[0])
        sum2 += int(row[1])
        sum3 += int(row[2])
        sum4 += int(row[3])
        sum5 += int(row[4])
        if max1 < int(row[0]):
          max1 = int(row[0])
        elif min1 > int(row[0]):
          min1 = int(row[0])
        if max2 < int(row[1]):
          max2 = int(row[1])
        elif min2 > int(row[1]):
          min2 = int(row[1])
        if max3 < int(row[2]):
          max3 = int(row[2])
        elif min3 > int(row[2]):
          min3 = int(row[2])
        if max4 < int(row[3]):
          max4 = int(row[3])
        elif min4 > int(row[3]):
          min4 = int(row[3])
        if max5 < int(row[4]):
          max5 = int(row[4])
        elif min5 > int(row[4]):
          min5 = int(row[4])
        data += 1
    avg1 = sum1/float(data)
    avg2 = sum2/float(data)
    avg3 = sum3/float(data)
    avg4 = sum4/float(data)
    avg5 = sum5/float(data)
    report.write("\t\t\tSummary of Raw Data from Sensors\n")
    report.write("\t\tAverage\tMinimum Reading\tMaximum Reading\n")
    report.write("Sensor 1\t%.3f\t\t%i\t\t%i\n" % (avg1,min1,max1))
    report.write("Sensor 2\t%.3f\t\t%i\t\t%i\n" % (avg2,min2,max2))
    report.write("Sensor 3\t%.3f\t\t%i\t\t%i\n" % (avg3,min3,max3))
    report.write("Sensor 4\t%.3f\t\t%i\t\t%i\n" % (avg4,min4,max4))
    report.write("Sensor 5\t%.3f\t\t%i\t\t%i\n" % (avg5,min5,max5))
    report.close() 
