#!/usr/bin/python
# -*- coding: utf-8 -*-


class hotelManage:

    def __init__(
        self,
        rt='',
        s=0,
        p=0,
        r=0,
        t=0,
        a=1800,
        name='',
        address='',
        checkIn='',
        checkOut='',
        roomNo=101,
        ):

        print '''-------------------------------
WELCOME TO GRAND ELEGANCE HOTEL
-------------------------------'''

        self.rt = rt

        self.r = r

        self.t = t

        self.p = p

        self.s = s
        self.a = a
        self.name = name
        self.address = address
        self.checkIn = checkIn
        self.checkOut = checkOut
        self.roomNo = roomNo

    def inputdata(self):
        self.name = input('\nEnter your Name:')
        self.address = input('Enter your Address:')
        self.checkIn = input('Enter your Check-In Date:')
        self.checkOut = input('Enter your Check-Out Date:')
        print ('''
Thank You for choosing Grand Elegance Hotel,
Your Room Number is:''',
               self.roomNo, '\n')

    def roomrent(self):

        print 'We have following rooms available:- '

        print ' -------------------------------------'

        print "| 1.  Suite        ----> Rs 6000 PN\- |"

        print "| 2.  Deluxe Room  ----> Rs 5000 PN\- |"

        print "| 3.  Double Room  ----> Rs 4000 PN\- |"

        print "| 4.  Single Room  ----> Rs 3000 PN\- |"

        print ' -------------------------------------'

        x = int(input('\nEnter Your Choice Please: '))

        n = int(input('For How Many Nights would you like to stay: '))

        if x == 1:

            print '\nThank You for Choosing... You have selected Suite'

            self.s = 6000 * n
        elif x == 2:

            print '\nThank You for Choosing... You have selected Deluxe Room'

            self.s = 5000 * n
        elif x == 3:

            print '\nThank You for Choosing... You have selected Double Room'

            self.s = 4000 * n
        elif x == 4:

            print '\nThank You for Choosing... You have selected Single Room'

            self.s = 3000 * n
        else:

            print '\nPlease select a room'

        print ('Room Rent = Rs ', self.s, '\n')

    def restaurentbill(self):

        print '\n*****RESTAURANT MENU*****'

        print (
            ' __________________________________',
            '\n| 1.Water      ----->        Rs 20 |',
            '\n| 2.Tea        ----->        Rs 10 |',
            '\n| 3.Breakfast  ----->        Rs 90 |',
            '\n| 4.Lunch      ----->        Rs 110|',
            '\n| 5.Dinner     ----->        Rs 150|',
            '\n| 6.Exit                           |',
            '\n __________________________________',
            )

        while 1:

            c = int(input('\nEnter your choice: '))

            if c == 1:
                d = int(input('Enter the quantity: '))
                self.r = self.r + 20 * d
            elif c == 2:

                d = int(input('Enter the quantity:'))
                self.r = self.r + 10 * d
            elif 3 == c:

                d = int(input('Enter the quantity:'))
                self.r = self.r + 90 * d
            elif c == 4:

                d = int(input('Enter the quantity:'))
                self.r = self.r + 110 * d
            elif c == 5:

                d = int(input('Enter the quantity:'))
                self.r = self.r + 150 * d
            elif c == 6:

                break
            else:
                print 'Invalid option. Please choose valid option from the given list.'

        print ('\nTOTAL FOOD COST = Rs ', self.r, '\n')

    def laundrybill(self):
        print '\n******LAUNDRY MENU*******'

        print (
            ' __________________________\n| 1.Shorts     -----> Rs 3 |'
                ,
            '\n| 2.Trousers   -----> Rs 4 |',
            '\n| 3.Shirt      -----> Rs 5 |',
            '\n| 4.Jeans      -----> Rs 6 |',
            '\n| 5.Girl Suit  -----> Rs 8 |',
            '\n| 6.Exit                   |',
            '\n __________________________',
            )

        while 1:

            e = int(input('\nEnter your choice:'))

            if e == 1:
                f = int(input('Enter the quantity:'))
                self.t = self.t + 3 * f
            elif e == 2:

                f = int(input('Enter the quantity:'))
                self.t = self.t + 4 * f
            elif e == 3:

                f = int(input('Enter the quantity:'))
                self.t = self.t + 5 * f
            elif e == 4:

                f = int(input('Enter the quantity:'))
                self.t = self.t + 6 * f
            elif e == 5:

                f = int(input('Enter the quantity:'))
                self.t = self.t + 8 * f
            elif e == 6:
                break
            else:

                print 'Invalid option. Please choose valid option from the given list.'

        print ('\nTOTAL LAUNDRY COST = Rs ', self.t, '\n')

    def gamebill(self):
        print '\n******GAMES*******'

        print (
            ' _______________________________\n| 1.Table Tennis   -----> Rs 60 |'
                ,
            '\n| 2.Bowling        -----> Rs 80 |',
            '\n| 3.Snooker        -----> Rs 70 |',
            '\n| 4.Video games    -----> Rs 90 |',
            '\n| 5.Pool           -----> Rs 50 |',
            '\n| 6.Exit                        |',
            '\n _______________________________',
            )

        while 1:

            g = int(input('\nEnter your choice:'))

            if g == 1:
                h = int(input('No. of hours:'))
                self.p = self.p + 60 * h
            elif g == 2:

                h = int(input('No. of hours:'))
                self.p = self.p + 80 * h
            elif g == 3:

                h = int(input('No. of hours:'))
                self.p = self.p + 70 * h
            elif g == 4:

                h = int(input('No. of hours:'))
                self.p = self.p + 90 * h
            elif g == 5:

                h = int(input('No. of hours:'))
                self.p = self.p + 50 * h
            elif g == 6:
                break
            else:

                print 'Invalid option. Please choose valid option from the given list.'

        print ('\nTOTAL GAME BILL = Rs ', self.p, '\n')

    def display(self):
        print '\n******TOTAL BILL******'
        print '__________________________________________________'
        print 'CUSTOMER DETAILS'
        print ('Customer name:      ', self.name)
        print ('Customer address:   ', self.address)
        print '\nCHECK-IN/OUT DETAILS'
        print ('Check-In date:      ', self.checkIn)
        print ('Check-Out date:     ', self.checkOut)
        print '\nROOM & FACILITIES DETAILS'
        print ('Room No.:           ', self.roomNo)
        print ('Room Rent:          Rs ', self.s)
        print ('Food Bill:          Rs ', self.r)
        print ('Laundry Bill:       Rs ', self.t)
        print ('Game Bill :         Rs ', self.p)

        self.rt = self.s + self.t + self.p + self.r

        print ('\nSub-Total Bill:               Rs ', self.rt)
        print ('Additional Service Charges:   Rs ', self.a)
        print '\n==========================================='
        print ('GRAND TOTAL BILL:             Rs ', self.rt + self.a)
        print '==========================================='
        print '__________________________________________________\n'
        self.roomNo += 1


def main():
    a = hotelManage()

    while 1:

        print '\n****MAIN MENU****'

        print ' ________________________'

        print '| 1.Enter Customer Data  |'

        print '| 2.Room Selection       |'

        print '| 3.Restaurant           |'

        print '| 4.Laundry Service      |'

        print '| 5.Games                |'

        print '| 6.Total Bill           |'

        print '| 7.EXIT                 |'

        print ' ________________________'

        b = int(input('\nEnter your choice:'))
        if b == 1:
            a.inputdata()

        if b == 2:
            a.roomrent()

        if b == 3:
            a.restaurentbill()

        if b == 4:
            a.laundrybill()

        if b == 5:
            a.gamebill()

        if b == 6:
            a.display()

        if b == 7:
            quit()


main()
