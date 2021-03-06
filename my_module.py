author = "Nikhil Gopal"

import random
import numpy as np



def rand_seq(n):
    return ''.join([ random.choice('ACGT') for x in range(n) ])


#Honors Stats class functions, created 9/22

def zscore(list, index):  #finds zscore or standard score of a list
    indexminusone = index - 1
    mean = np.mean(list)
    numberminusmean = list[indexminusone] - mean
    array = np.array(list)
    stdev = np.std(array)
    z_score = numberminusmean / stdev

    return z_score

def mean(list):   #finds average of a list
    avg = np.mean(list)

    return avg

def stdev(list): #finds standard deviation of a list
    array = np.array(list)
    standard_deviation = np.std(array)

    return standard_deviation

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


def sumoflist(list, returnornot):
    tsum = sum(list)

    return tsum


def rule_of_68_95_99_point_7(list): #shows values within one, two and three standard deviations of the mean
    standarddev = stdev(list)
    avg = mean(list)

    one_stdev_plus = standarddev + avg
    one_stdev_minus = avg - standarddev

    two_stdev_plus = one_stdev_plus + standarddev
    two_stdev_minus = one_stdev_minus - standarddev

    three_stdev_plus = two_stdev_plus + standarddev
    three_stdev_minus = two_stdev_minus - standarddev

    print 'Mean: ' + str(avg)
    print 'Standard Deviation:' + str(standarddev)

    print 'One standard deviation: ' + str(one_stdev_minus) + ' to '  + str(one_stdev_plus)
    print 'Two standard deiation: ' + str(two_stdev_minus) + ' to ' + str(two_stdev_plus)
    print 'Three standard deiation: ' + str(three_stdev_minus) + ' to ' + str(three_stdev_plus)


# Environmental Science Functions


def solveforpopulationnumber(m, r, lower_case_n): #calculates the amount of individuals in a population

#M =  total number of marked individuals
#N  =  total population size (which we do not know)
#R  =  number of marked individuals recaptured
#n  =   total number of individuals (marked and unmarked) captured a second time

    lower_case_n_plus_one = lower_case_n + 1
    m_times_lower_case_n_plus_one = m * lower_case_n_plus_one
    r_plus_1 = r + 1
    total = float(m_times_lower_case_n_plus_one / r_plus_1)
    return total




sample_list = [18.7, 16.4, 13.2, 19.1, 12.3, 16.7, 15.8, 16.2, 18.6, 17.8, 14.3, 22.8, 16.4, 16.2, 16.6, 16.8, 15.7, 12.6, 9.4, 13.6, 18.3, 17.8, 18.2, 13.2, 14.6, 13.8, 13.2, 15.7, 15.8, 12.2, 13.6, 19.7, 14.9, 15.2, 15.3, 18.7, 17.6, 14.7, 16.1, 13.2, 12.2, 12.4, 13.5, 16.8]

rule_of_68_95_99_point_7(sample_list)