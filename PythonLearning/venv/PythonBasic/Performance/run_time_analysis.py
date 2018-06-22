import cProfile
import time

str1 = 'Hello everyone'
str2 = 'Glade to meet you ALL'
str3 = 'And now let me introduce myself firstly'
str6 = 'And now let me introduce myself firstly'
str7 = 'And now let me introduce myself firstly'
str8 = 'And now let me introduce myself firstly'
str9 = 'And now let me introduce myself firstly'
str10 = 'And now let me introduce myself firstly'
str11 = 'And now let me introduce myself firstly'
str12 = 'And now let me introduce myself firstly'
str13 = 'And now let me introduce myself firstly'
str14 = 'And now let me introduce myself firstly'


def str_concatenation_plussign():
    str4 = str1 + str2 + str3 + str6 + str7\
           + str8 + str9 + str10 + str11\
           + str12 + str13 + str14
    # str4 = str1 + ',' + str2 + ',' + str3 + ',' + str6 + ',' + str7 \
    #        + ',' + str8 + ',' + str9 + ',' + str10 + ',' + str11 + ',' \
    #        + str12 + ',' + str13 + ',' + str14
    #
    print(str4)


def str_concatenation_join():
    str5 = ','.join([str1, str2, str3, str6, str7, str8, str9, str10, str11, str12, str13, str14])
    #
    print(str5)


def str_concatenation_format():
    str15 = '{0},{1},{2},{3},{5},{6},{7},{8},{9},{10},{11}'.format(str1, str2, str3,
                                                                   str6, str7, str8, str9, str10,
                                                                   str11, str12, str13, str14)
    # ,{12}
    #
    print(str15)


cProfile.run('str_concatenation_plussign')


cProfile.run('str_concatenation_join')

start1 = time.clock()
str_concatenation_plussign()
end1 = time.clock()
print('the running time of method str_concatenation_plussign is:\n {0} seconds\n'.format((end1 - start1)))

start2 = time.clock()
str_concatenation_join()
end2 = time.clock()
print('the running time of method str_concatenation_join is:\n {0} seconds\n'.format((end2 - start2)))

start3 = time.clock()
str_concatenation_format()
end3 = time.clock()
print('the running time of method str_concatenation_format is:\n {0} seconds\n'.format((end3 - start3)))
