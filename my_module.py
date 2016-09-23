author = "Nikhil Gopal"

import random
import numpy as np



def rand_seq(n):
    return ''.join([ random.choice('ACGT') for x in range(n) ])


#Honors Stats class functions, created 9/22

def zscore(list, index, returnornot):  #finds zscore or standard score of a list
    indexminusone = index - 1
    mean = np.mean(list)
    numberminusmean = list[indexminusone] - mean
    array = np.array(list)
    stdev = np.std(array)
    zscore = numberminusmean / stdev

    if returnornot == True:
        return zscore
    else:
        print 'zscore: ' + str(zscore)

def mean(list, returnornot):   #finds average of a list
    avg = np.mean(list)
    if returnornot == True:
        return float(avg)
    else:
        print "Mean: " + str(avg)

def stdev(list, returnornot): #finds standard deviation of a list
    import numpy as np
    array = np.array(list)
    standarddeviation = np.std(array)

    if returnornot == True:
        return float(standarddeviation)
    else:
        print 'standard deviation: ' + str(standarddeviation)

def median(list, returnornot): #finds the median or q2 of a list
    list_length_divded_by_two = len(list) / 2

    if len(list) % 2 == 0:
        number_1 = list[list_length_divded_by_two]
        number_2 = list[list_length_divded_by_two - 1]
        list_to_average = [number_1, number_2]
        mediaan = mean(list_to_average, True)
    else:
        mediaan = list[list_length_divded_by_two]

    if returnornot == True:
        return mediaan
    else:
        print "median: " + str(mediaan)

def q1(list, returnornot): #finds quartile 1 or q1 of a list
    list_length_divded_by_two = len(list) / 2
    if len(list) % 2 == 0:
        number_2 = list[list_length_divded_by_two - 1]
        new_list = list[0:number_2]
        quartile_one = median(new_list, True)
    else:
        new_list = list[:list_length_divded_by_two]
        quartile_one = median(new_list, True)

    if returnornot == True:
        return quartile_one
    else:
        print quartile_one

def q3(list,returnornot): #finds quartile 3 or q3 of a list
    list_length_divded_by_two = len(list) / 2
    if len(list) % 2 == 0:
        number_2 = list[list_length_divded_by_two - 1]
        new_list = list[number_2:]
        quartile_one = median(new_list, True)
    else:
        new_list = list[list_length_divded_by_two:]
        quartile_one = median(new_list, True)

    if returnornot == True:
        return quartile_one
    else:
        print quartile_one

def iqr(list, returnornot): #finds the interquartile range of a list
    quartile_3 = q3(list, True)
    quartile_1 = q1(list, True)
    inter_quartile_range = quartile_3 - quartile_1
    if returnornot == True:
        return inter_quartile_range
    else:
        print "IQR: " + inter_quartile_range

def range(list, returnornot): #finds the range of a list
    length_of_list = len(list) - 1
    first_value = list[0]
    last_value = list[length_of_list]
    rannge = last_value - first_value

    if returnornot == True:
        return rannge
    else:
        print "range: " + range

def describeadistribution(list): #lists all the values in one place
    average = mean(list, True)
    standard_deviation = stdev(list, True)
    mediann = median(list, True)
    quart1 = q1(list, True)
    quart3 = q3(list, True)
    interqr = iqr(list, True)
    rangge = range(list, True)

    print "Mean: " + str(average)
    print "Standard Deviation: " + str(standard_deviation)
    print "Median: " + str(mediann)
    print "Q1: " + str(quart1)
    print "Q3: " + str(quart3)
    print "IQR: " + str(interqr)
    print "Range: " + str(rangge)


def leasttogreatest(list, returnornot): #sorts a list from least to greatest
    list.sort()
    if returnornot == True:
        return list
    else:
        print list

def greatesttoleast(list, returnornot): #sorts a list from greatest to least
    list.sort()
    list.reverse()
    if returnornot == True:
        return list
    else:
        print list


