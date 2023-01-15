import csv
with open("question.csv","w",newline="")as f:
    w=csv.writer(f,delimiter=",")
    w.writerow(["1.Which one is the smallest ocean in the world?"])
    w.writerow(["2.Total number of ocean in the world?"])
    w.writerow(["3.The world longest straight road is located in?"])
    w.writerow(["4.Which one is the island in the world?"])
    w.writerow(["5.Emu bird is found in the country?"])
    w.writerow(["6.Which country is known as the 'Land of Rising Sun'?"])
    w.writerow(["7.Which country is the highest producer of wine in the world?"])
    w.writerow(["8.which country is known as the 'country of gold bird'?"])
    w.writerow(["9.Where is the world's longest sea bridge?"])
    w.writerow(["10.In which country was the TATA comany started?"])