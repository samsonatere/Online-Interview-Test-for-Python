import psycopg2
import os
from random import randint, random


DATABASE_URL = os.environ.get('postgres://gxovqvcysupqqr:9a0a7d5448107978d5bebf40e70027aa847d08de6d73cf1536bf0b9a3c6b76ba@ec2-44-196-68-164.compute-1.amazonaws.com:5432/d993s5k3if43oa')

raw_colors =  ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN', 'ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN', 'GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']

color = {
    'GREEN' : 0, 'WHITE' : 0, 'BROWN' : 0, 'BLUE' :  0, 'BLACK' : 0, 'ORANGE' : 0, 'RED' : 0, 'YELLOW' : 0, 'PINK' : 0, 'CREAM' : 0, 'ARSH' : 0, 'BLEW' : 0
}

for i in raw_colors:
    if i in color:
        color[i] += 1

con = psycopg2.connect(DATABASE_URL)

cur = con.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS color (
# 	id serial PRIMARY KEY,
# 	color text  NOT NULL,
# 	frequency VARCHAR (2) NOT NULL
# );""")
# count = 0
# for key, value in color.items():
#     count =  count + 1
#     cur.execute("INSERT INTO color VALUES (%s, %s, %s)", (count, key, value ))

# con.commit()

cur.execute("SELECT * from color")
result = cur.fetchall()

cur.execute("SELECT frequency from color where color=%s ", ('RED',))
red_value = cur.fetchone()

total = 0   #   total frequency of all colors
length = len(result)    #   Number of colors
max = 0 #   color with the highest occurence 

for i in result:
    total += int(i[2])
    if int(i[2]) > max:
        max = int(i[2])


class BincomTest():

    def __init__(self, raw_colors, total, length):
        self.raw_colors = raw_colors
        self.total = total
        self.length = length

    def median(self):
        median = (self.total + 1 )/ 2
        median = self.raw_colors[int(median)]
        return median
    
    def mean(self):
        mean_shirt = []
        data = self.total/self.length
        mean_shirt.append(data)
        mean_shirt.append(self.raw_colors[int(data)])
        return mean_shirt

    def mostly_worn(self, max):
        return self.raw_colors[max]

    def variance(self, result):
        deviations = []
        square_deviation = []
        mean_ = self.mean()
        for i in result:
            deviations.append( int(i[2]) - int(mean_[0]))

        for num in deviations:
            square_deviation.append( num * num)
        
        sum_of_squares = sum(square_deviation)

        variance_ = sum_of_squares/ (self.length - 1)
        return variance_

    def probability_of_red(self, red_value):
        probability = int(red_value[0])/self.total
        return probability

    def random_digit(self):
        random_ = 0
        binary = []
        for _ in range(4):
            value = randint(0, 1)
            binary.append(value)
        
        for num in range(len(binary)):
            for i in binary:
                if i == 0:
                    continue
                else:
                    random_ +=  i ** num 
        
        return random_

    def fibonacci(self):
        num = 50
        a, b = 1, 1
        for _ in range(num - 1):
            a, b = b, a + b
        return a


example_code = BincomTest(raw_colors, total, length)

print('mean color shirt is', example_code.mean()[1])
print('color mostly worn is', example_code.mostly_worn(max))
print('median color is', example_code.median())
print('The variance of colors is', example_code.variance(result))
print('The probability that color chosen at random is', example_code.probability_of_red(red_value))
print('converting random 4 digit to decimal',  example_code.random_digit())
print('sum of first 50 fibonacci series is', example_code.fibonacci())