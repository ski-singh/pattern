from time import sleep

#sleep is used to to hault the flow of the program.

class pattern:

    def rightTriangle(self, no):
        """will print something like this
                    *
                    **
                    ***
                    ****
                    *****
            :param no: int value for no of rows
            :return: nothing"""
        self.no=no
        for i in range(0,no):
            for k in range(0, i+1):
                print("*", end="")
            sleep(0.3)
            print()

    def invertedRightTriangel(self,no):
        """
                    will print something like this
                    *****
                    ****
                    ***
                    **
                    *
            :param no: int value for no of rows
            :return: nothing"""

        self.no=no
        for i in range(0,no):
            for i in range(i,no):
                print("*",end="")
            sleep(0.3)
            print()

    def after180RotationRightTriangle(self,no):
        """ will print something like this
                   *
                  **
                 ***
                ****
               *****

            :param no:int value for no of rows
            :return:nothing"""
        for i in range(0,no):
            for k in range(no-1,i,-1):
                print(" ",end="")
            for j in range(0,i+1):
                print("*", end="")
                sleep(0.3)
            print()

    def invertedMirroredRightTraingle(self,no):
        """ will print something like this
                    *****
                     ****
                      ***
                       **
                        *

            :param no:int value for no of rows
            :return:nothing
                """
        self.no=no
        for i in range(0,no):
            for j in range(0,i):
                print(" ",end="")
            for k in range(i,no):
                print("*",end="")
                sleep(0.3)
            print()

    def pyramid(self,no):
        """ will print something like this
             *
            * *
           * * *
          * * * *
         * * * * *

            :param no:int value for no of rows
            :return:nothing"""

        self.no=no
        for i in range(0,no):
            for j in range(i+1,no):
                print(" ",end="")
            for k in range(0,i+1):
                print("* ",end="")
            sleep(0.3)
            print()

    def inversePyramid(self,no):
        """ will print something like this
                     * * * * *
                      * * * *
                       * * *
                        * *
                         *

            :param no:int value for no of rows
            :return:nothing
                                """

        for i in range(0,no):
            for j in range(0,i):
                print(" ",end="")
            for k in range(i,no):
                print("* ",end="")
            sleep(0.3)
            print()

    def numberRightTrinagle(self,no):
        """ will print something like this
            1
            22
            333
            4444
            55555

            :param no:int value for no of rows
            :return:nothing
                                        """
        self.no=no
        for i in range(0,self.no):
            for j in range(0,i+1):
                print(i+1,end="")
            sleep(0.3)
            print()

    def numberRightTrinagleTwo(self,no):
        """ will print something like this
        1
        12
        123
        1234
        12345


            :param no:int value for no of rows
            :return:nothing
                                                """
        self.no=no
        for i in range(0,self.no):
            for j in range(0,i+1):
                print(j+1,end="")
            sleep(0.3)
            print()

    def numberRightTrinagleThree(self,no):
        """ will print something like this
        1
        21
        321
        4321
        54321

            :param no:int value for no of rows
            :return:nothing"""
        self.no=no
        for i in range(0,self.no):
            for j in range(i+1,0,-1):
                print(j,end="")
            sleep(0.3)
            print()

    def numberRightTrinagleFour(self,no):
        """ will print something like this
                1
                2 1
                4 2 1
                8 4 2 1
                16 8 4 2 1

            :param no:int value for no of rows
            :return:nothing"""
        self.no=no
        for i in range(0,self.no):
            for j in range(i,-1,-1):
                print(2**j,end=" ")
            sleep(0.3)
            print()

    def numberRightTrinagleFive(self, no):
        """ will print something like this
        1
        1 2
        1 2 4
        1 2 4 8
        1 2 4 8 16

            :param no:int value for no of rows
            :return:nothing"""
        self.no = no
        for i in range(0, self.no):
            for j in range(0, i+1):
                print(2 ** j, end=" ")
            sleep(0.3)
            print()

    def numberRightTrinagleSix(self, no):
        """ will print something like this
            1
            1 2 1
            1 2 4 2 1
            1 2 4 8 4 2 1
            1 2 4 8 16 8 4 2 1

            :param no:int value for no of rows
            :return:nothing"""
        self.no = no
        for i in range(0, self.no):
            for j in range(0,i+1):
                print(2 ** j, end=" ")
            for k in range(i-1,-1,-1):
                print(2**k,end=" ")
            sleep(0.3)
            print()

    def numberRightTrinagleSeven(self, no):
        """ will print something like this
            1
            2 3
            4 5 6
            7 8 9 10
            11 12 13 14 15

            :param no:int value for no of rows
            :return:nothing"""

        self.no = no
        self.count=1
        for i in range(0, self.no):
            for j in range(0,i+1):
                print(self.count, end=" ")
                self.count=self.count+1
            sleep(0.3)
            print()

    def numberPyramid(self,no):
        """ will print something like this

        5 6 7 8 9 8 7 6 5
          4 5 6 7 6 5 4
            3 4 5 4 3
              2 3 2
                1
              2 3 2
            3 4 5 4 3
          4 5 6 7 6 5 4
        5 6 7 8 9 8 7 6 5

        :param no:int value for no of rows
        :return:nothing"""
        self.no=no
        for i in range(self.no,0,-1):
            for l in range(self.no-i,0,-1):
                print("  ",end="")
            for j in range(i,i+i):
                print(j,end=" ")
            for k in range(i+i-2,i-1,-1):
                print(k,end=" ")
            sleep(0.3)
            print()
        for i in range(2,self.no+1):
            for k in range(i,self.no):
                print("  ",end="")
            for l in range(i,i+i):
                print(l,end=" ")
            for m in range(i+i-2,i-1,-1):
                print(m,end=" ")
            sleep(0.3)
            print()






